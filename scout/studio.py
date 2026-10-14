"""Local recording library and FFmpeg export for the workspace studio."""

import json
import math
import re
import shutil
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

from scout import config


MAX_UPLOAD_BYTES = 2 * 1024 * 1024 * 1024
MIME_EXTENSIONS = {
    'video/webm': '.webm',
    'video/mp4': '.mp4',
    'video/quicktime': '.mov',
}
ASPECT_SIZES = {'wide': (1280, 720), 'vertical': (720, 1280), 'square': (1080, 1080)}


class StudioError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


def _number(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise StudioError(400, f'{name} must be a number')
    if not low <= value <= high:
        raise StudioError(400, f'{name} must be between {low} and {high}')
    return float(value)


def _probe(path):
    if not shutil.which('ffprobe'):
        raise StudioError(503, 'FFmpeg and ffprobe are required for the studio')
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries',
             'format=duration:stream=codec_type,width,height', '-of', 'json', str(path)],
            capture_output=True, text=True, timeout=20, check=True,
        )
        data = json.loads(result.stdout)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        raise StudioError(400, f'Could not read this video: {exc}') from exc
    video = next((item for item in data.get('streams', []) if item.get('codec_type') == 'video'), None)
    if not video:
        raise StudioError(400, 'The file does not contain a video track')
    try:
        duration = float(data.get('format', {}).get('duration') or 0)
    except (ValueError, TypeError):
        duration = 0
    return {
        'duration': duration if math.isfinite(duration) and duration > 0 else 0,
        'width': int(video.get('width') or 0),
        'height': int(video.get('height') or 0),
        'has_audio': any(item.get('codec_type') == 'audio' for item in data.get('streams', [])),
    }


class StudioLibrary:
    def __init__(self, root=None):
        self.root = Path(root or config.DATA / 'studio')
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / 'exports').mkdir(exist_ok=True)

    def status(self):
        return {'ready': bool(shutil.which('ffmpeg') and shutil.which('ffprobe')),
                'message': 'FFmpeg ready' if shutil.which('ffmpeg') and shutil.which('ffprobe')
                else 'Install FFmpeg to save and export recordings'}

    def _meta_path(self, recording_id):
        if not re.fullmatch(r'[a-f0-9]{32}', recording_id):
            raise StudioError(404, 'recording not found')
        return self.root / f'{recording_id}.json'

    def get(self, recording_id):
        path = self._meta_path(recording_id)
        if not path.is_file():
            raise StudioError(404, 'recording not found')
        metadata = json.loads(path.read_text(encoding='utf-8'))
        if not (self.root / f'{recording_id}{metadata["extension"]}').is_file():
            raise StudioError(404, 'recording file is missing')
        metadata.setdefault('project_id', None)
        return metadata

    def list(self):
        rows = []
        for path in self.root.glob('*.json'):
            try:
                rows.append(self.get(path.stem))
            except (StudioError, ValueError, KeyError, json.JSONDecodeError):
                continue
        return sorted(rows, key=lambda item: item['created_at'], reverse=True)

    def file_path(self, recording_id):
        metadata = self.get(recording_id)
        return self.root / f'{recording_id}{metadata["extension"]}', metadata

    def save(self, source, length, content_type, title='Recording', duration_hint=0, project_id=None):
        mime = content_type.split(';', 1)[0].strip().lower()
        if mime not in MIME_EXTENSIONS:
            raise StudioError(415, 'Upload a WebM, MP4, or MOV video')
        if length <= 0 or length > MAX_UPLOAD_BYTES:
            raise StudioError(413, 'Video must be between 1 byte and 2 GB')
        title = title.strip()[:120] or 'Recording'
        duration_hint = _number(duration_hint, 'duration', 0, 24 * 60 * 60)
        if project_id is not None and (not isinstance(project_id, str) or
                                       not re.fullmatch(r'[a-f0-9]{32}', project_id)):
            raise StudioError(400, 'invalid project_id')
        recording_id = uuid.uuid4().hex
        extension = MIME_EXTENSIONS[mime]
        partial = self.root / f'{recording_id}.part'
        target = self.root / f'{recording_id}{extension}'
        try:
            remaining = length
            with partial.open('wb') as out:
                while remaining:
                    chunk = source.read(min(1024 * 1024, remaining))
                    if not chunk:
                        raise StudioError(400, 'Upload ended before the file was complete')
                    out.write(chunk)
                    remaining -= len(chunk)
            info = _probe(partial)
            if info['width'] < 2 or info['height'] < 2:
                raise StudioError(400, 'Invalid video dimensions')
            partial.replace(target)
            metadata = {
                'id': recording_id, 'title': title, 'extension': extension,
                'mime_type': mime, 'size': length,
                'duration': info['duration'] or duration_hint,
                'width': info['width'], 'height': info['height'],
                'has_audio': info['has_audio'],
                'project_id': project_id,
                'created_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            }
            self._meta_path(recording_id).write_text(json.dumps(metadata, ensure_ascii=False), encoding='utf-8')
            return metadata
        except Exception:
            partial.unlink(missing_ok=True)
            target.unlink(missing_ok=True)
            raise

    def update(self, recording_id, changes):
        if not isinstance(changes, dict) or not changes or set(changes) - {'title', 'project_id'}:
            raise StudioError(400, 'provide title or project_id')
        metadata = self.get(recording_id)
        if 'title' in changes:
            title = changes['title']
            if not isinstance(title, str) or not title.strip() or len(title) > 120:
                raise StudioError(400, 'title must be 1–120 characters')
            metadata['title'] = title.strip()
        if 'project_id' in changes:
            project_id = changes['project_id']
            if project_id is not None and (not isinstance(project_id, str) or
                                           not re.fullmatch(r'[a-f0-9]{32}', project_id)):
                raise StudioError(400, 'invalid project_id')
            metadata['project_id'] = project_id
        self._meta_path(recording_id).write_text(json.dumps(metadata, ensure_ascii=False), encoding='utf-8')
        return metadata

    def rename(self, recording_id, title):
        return self.update(recording_id, {'title': title})

    def clear_project(self, project_id):
        for recording in self.list():
            if recording['project_id'] == project_id:
                self.update(recording['id'], {'project_id': None})

    def delete(self, recording_id):
        path, _ = self.file_path(recording_id)
        path.unlink()
        self._meta_path(recording_id).unlink(missing_ok=True)

    def export(self, recording_id, options):
        if not shutil.which('ffmpeg'):
            raise StudioError(503, 'FFmpeg is required to export videos')
        if not isinstance(options, dict):
            raise StudioError(400, 'body must be a JSON object')
        allowed = {'format', 'start', 'end', 'aspect', 'padding', 'background', 'zoom', 'focus_x', 'focus_y', 'speed'}
        if set(options) - allowed:
            raise StudioError(400, f'unknown export field: {sorted(set(options) - allowed)[0]}')
        path, metadata = self.file_path(recording_id)
        duration = metadata['duration']
        if duration <= 0:
            raise StudioError(400, 'The video duration is unavailable')
        fmt = options.get('format', 'mp4')
        if fmt not in ('mp4', 'gif'):
            raise StudioError(400, 'format must be mp4 or gif')
        start = _number(options.get('start', 0), 'start', 0, duration)
        end = _number(options.get('end', duration), 'end', 0, duration + 0.5)
        if end - start < 0.1:
            raise StudioError(400, 'Select at least 0.1 seconds to export')
        aspect = options.get('aspect', 'source')
        if aspect not in ('source', *ASPECT_SIZES):
            raise StudioError(400, 'invalid aspect ratio')
        zoom = _number(options.get('zoom', 1), 'zoom', 1, 3)
        focus_x = _number(options.get('focus_x', 0.5), 'focus_x', 0, 1)
        focus_y = _number(options.get('focus_y', 0.5), 'focus_y', 0, 1)
        speed = _number(options.get('speed', 1), 'speed', 0.5, 2)
        padding = options.get('padding', 0)
        if isinstance(padding, bool) or not isinstance(padding, int) or not 0 <= padding <= 200:
            raise StudioError(400, 'padding must be an integer between 0 and 200')
        background = options.get('background', '#111827')
        if not isinstance(background, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', background):
            raise StudioError(400, 'background must be a six-digit hex color')
        if aspect == 'source':
            scale = min(1, 1920 / metadata['width'], 1080 / metadata['height'])
            width = max(2, int(metadata['width'] * scale) // 2 * 2)
            height = max(2, int(metadata['height'] * scale) // 2 * 2)
        else:
            width, height = ASPECT_SIZES[aspect]
        if padding * 2 >= min(width, height):
            raise StudioError(400, 'padding is too large for this aspect ratio')
        filters = []
        if zoom > 1:
            filters.append(f'crop=trunc(iw/{zoom}/2)*2:trunc(ih/{zoom}/2)*2:(iw-ow)*{focus_x}:(ih-oh)*{focus_y}')
        filters += [
            f'scale={width - 2 * padding}:{height - 2 * padding}:force_original_aspect_ratio=decrease:force_divisible_by=2',
            f'pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=0x{background[1:]}',
            'setsar=1',
        ]
        if speed != 1:
            filters.append(f'setpts=PTS/{speed}')
        output = self.root / 'exports' / f'{uuid.uuid4().hex}.{fmt}'
        command = ['ffmpeg', '-y', '-nostdin', '-hide_banner', '-loglevel', 'error',
                   '-ss', str(start), '-t', str(end - start), '-i', str(path)]
        if fmt == 'gif':
            chain = ','.join(filters + ['fps=12'])
            command += ['-filter_complex', f'[0:v]{chain},split[a][b];[a]palettegen[p];[b][p]paletteuse[v]',
                        '-map', '[v]', '-an', str(output)]
        else:
            command += ['-vf', ','.join(filters), '-c:v', 'libx264', '-preset', 'medium',
                        '-crf', '20', '-pix_fmt', 'yuv420p']
            if metadata['has_audio']:
                command += ['-af', f'atempo={speed}', '-c:a', 'aac', '-b:a', '160k']
            else:
                command += ['-an']
            command += ['-movflags', '+faststart', str(output)]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired as exc:
            output.unlink(missing_ok=True)
            raise StudioError(504, 'Export exceeded the 10-minute processing limit') from exc
        if result.returncode or not output.is_file() or output.stat().st_size == 0:
            output.unlink(missing_ok=True)
            raise StudioError(500, f'Export failed: {result.stderr[-500:]}')
        return output, f'{metadata["title"]}.{fmt}'
