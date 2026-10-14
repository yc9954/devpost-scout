"""Exercise recording upload, ranged playback, and actual FFmpeg exports."""

import json
import shutil
import subprocess
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

from scout import server
from scout.studio import StudioLibrary
from scout.workspace import WorkspaceStore


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg is required')
class TestStudioHTTP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix='studio-test-')
        cls.root = Path(cls.tmp.name)
        cls.sample = cls.root / 'sample.webm'
        subprocess.run([
            'ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'testsrc2=size=320x180:rate=12',
            '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=48000', '-t', '1.5',
            '-c:v', 'libvpx-vp9', '-b:v', '300k', '-c:a', 'libopus', str(cls.sample),
        ], check=True, timeout=30)
        server.set_studio(StudioLibrary(cls.root / 'library'))
        server.set_workspace(WorkspaceStore(cls.root / 'workspace.db'))
        cls.project = server.workspace().create('projects', {'title': 'Filming project'})
        cls.http = server.make_server('127.0.0.1', 0)
        cls.base = f'http://127.0.0.1:{cls.http.server_port}'
        cls.thread = threading.Thread(target=cls.http.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.http.shutdown()
        cls.http.server_close()
        server.set_studio(None)
        server.set_workspace(None)
        cls.tmp.cleanup()

    def request(self, method, path, body=None, headers=None):
        req = urllib.request.Request(self.base + path, data=body, method=method, headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=40) as response:
                return response.status, response.headers, response.read()
        except urllib.error.HTTPError as error:
            with error:
                return error.code, error.headers, error.read()

    def test_upload_range_trim_export_and_delete(self):
        status, _, body = self.request('GET', '/api/studio/status')
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body)['ready'])
        status, _, body = self.request('POST', '/api/studio/recordings', self.sample.read_bytes(), {
            'Content-Type': 'video/webm', 'X-Recording-Title': 'Demo', 'X-Recording-Duration': '1.5',
            'X-Project-Id': self.project['id'],
        })
        self.assertEqual(status, 201)
        item = json.loads(body)
        self.assertEqual((item['width'], item['height'], item['has_audio']), (320, 180, True))
        self.assertGreater(item['duration'], 1)
        self.assertEqual(item['project_id'], self.project['id'])
        route = f'/api/studio/recordings/{item["id"]}'

        status, _, body = self.request('PATCH', route, b'{"project_id":null}',
                                       {'Content-Type': 'application/json'})
        self.assertEqual((status, json.loads(body)['project_id']), (200, None))
        status, _, body = self.request('PATCH', route, b'{"project_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}',
                                       {'Content-Type': 'application/json'})
        self.assertEqual((status, json.loads(body)['error']), (400, 'project not found'))

        status, headers, chunk = self.request('GET', route + '/file', headers={'Range': 'bytes=0-31'})
        self.assertEqual((status, len(chunk)), (206, 32))
        self.assertEqual(headers['Content-Range'], f'bytes 0-31/{item["size"]}')
        self.assertEqual(chunk, self.sample.read_bytes()[:32])

        status, _, body = self.request('PATCH', route, b'{"title":"Renamed"}', {'Content-Type': 'application/json'})
        self.assertEqual((status, json.loads(body)['title']), (200, 'Renamed'))
        status, _, body = self.request('POST', route + '/export', json.dumps({
            'format': 'mp4', 'start': 0.2, 'end': 1.2, 'aspect': 'square',
            'padding': 20, 'background': '#224466', 'zoom': 1.5,
            'focus_x': 0.7, 'focus_y': 0.4, 'speed': 1.25,
        }).encode(), {'Content-Type': 'application/json'})
        self.assertEqual(status, 200, body[:500])
        exported = self.root / 'exported.mp4'
        exported.write_bytes(body)
        info = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                               '-show_entries', 'stream=width,height', '-of', 'json', str(exported)],
                              check=True, capture_output=True, text=True, timeout=20)
        video = json.loads(info.stdout)['streams'][0]
        self.assertEqual((video['width'], video['height']), (1080, 1080))

        status, _, gif = self.request('POST', route + '/export', json.dumps({
            'format': 'gif', 'start': 0, 'end': 0.5, 'aspect': 'source', 'padding': 0,
        }).encode(), {'Content-Type': 'application/json'})
        self.assertEqual(status, 200, gif[:500])
        self.assertEqual(gif[:6], b'GIF89a')

        status, _, body = self.request('POST', route + '/export', json.dumps({
            'start': 0.5, 'end': 0.4,
        }).encode(), {'Content-Type': 'application/json'})
        self.assertEqual((status, json.loads(body)['error']), (400, 'Select at least 0.1 seconds to export'))
        self.assertEqual(self.request('DELETE', route)[0], 200)
        self.assertEqual(self.request('GET', route)[0], 404)


if __name__ == '__main__':
    unittest.main()
