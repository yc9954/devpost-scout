"""How many people the write-up is talking about, from the primary source.

The Impact claim named five roles and could only put a number on one of them.
This asks the US Bureau of Labor Statistics for all five, live, over its public
API — no key, no account, no scraped page. Run it yourself:

    python3 bench/population.py

Two different federal counts of the same occupation exist and they disagree,
so this script reports which one it is using. The Occupational Outlook
Handbook's "number of jobs" comes from Employment Projections and *includes*
the self-employed; OEWS below is an establishment survey and counts wage and
salary jobs only. For bookkeepers that is 1,532,400 against 1,373,680. Neither
is wrong. The OEWS one is the one a stranger can re-derive in one command,
so it is the one this file asserts.
"""
import json
import sys
import urllib.error
import urllib.request

API = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# OEWS national, all industries, by occupation. Data type 01 is employment.
#   OEUN + area(7) + industry(6) + SOC(6) + datatype(2)
ROLES = [
    ('43-3031', 'Bookkeeping, accounting and auditing clerks', 'bookkeepers'),
    ('43-3051', 'Payroll and timekeeping clerks',              'payroll administrators'),
    ('13-1071', 'Human resources specialists',                 'HR administrators'),
    ('43-4051', 'Customer service representatives',            'support leads'),
    ('43-6013', 'Medical secretaries and administrative assistants', 'schedulers in clinics'),
]

# What the API returned on 2026-09-04, so this file still says something when
# the network is not there. It is a record of a reading, not a substitute for one.
RECORDED = {
    '43-3031': 1373680, '43-3051': 153140, '13-1071': 912430,
    '43-4051': 2595750, '43-6013': 961610,
}
RECORDED_ON = '2026-09-04'


def series(soc):
    return 'OEUN' + '0' * 7 + '0' * 6 + soc.replace('-', '') + '01'


def ask():
    body = json.dumps({'seriesid': [series(soc) for soc, _, _ in ROLES]}).encode()
    req = urllib.request.Request(API, body, {'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if payload.get('status') != 'REQUEST_SUCCEEDED':
        raise RuntimeError(payload.get('status'))
    out = {}
    for s in payload['Results']['series']:
        rows = s['data']
        if not rows:
            raise RuntimeError('no data for ' + s['seriesID'])
        out[s['seriesID']] = (int(rows[0]['value']), rows[0]['year'])
    return out


def main():
    live = True
    try:
        got = ask()
    except (urllib.error.URLError, RuntimeError, TimeoutError) as e:
        print(f'the BLS API did not answer ({e}); reporting the reading recorded on {RECORDED_ON}\n')
        got = {series(soc): (RECORDED[soc], '2025') for soc, _, _ in ROLES}
        live = False

    print('US employment in the five roles the write-up names')
    print('source: BLS Occupational Employment and Wage Statistics, national, via api.bls.gov')
    print('        wage and salary jobs only — the self-employed are not counted here\n')

    total = 0
    drift = []
    for soc, title, plain in ROLES:
        value, year = got[series(soc)]
        total += value
        flag = '' if value == RECORDED[soc] else f'  (was {RECORDED[soc]:,} on {RECORDED_ON})'
        if flag:
            drift.append(soc)
        print(f'  {soc}  {value:>10,}  {year}  {title} — {plain}{flag}')

    print(f'  {"":>7}  {total:>10,}        all five')
    print(f'\nread it as the population these roles are drawn from, not as five million'
          f'\npeople who each need this. Customer service representatives is a wider'
          f'\noccupation than "support lead"; not everyone in it runs a recurring report'
          f'\nover records that carry an identifier. It is the upper bound that is citable.')
    if live:
        print('\nfetched live just now.')
    if drift:
        print(f'\nBLS has revised {", ".join(drift)} since {RECORDED_ON}. The number above is theirs, not mine.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
