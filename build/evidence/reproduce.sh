#!/bin/sh
# Every number the write-up puts in front of you, re-derived here.
#
# Two blind readings of this challenge said the same thing about this entry:
# the argument is thorough and there is nothing a reader can run. This is the
# answer to that. Nothing below calls a model or needs a key — the agent runs
# are already recorded in bench/ and are replayed, not repeated.
set -e
cd "$(dirname "$0")/.."

echo "=== 80 assertions over the policy, drift and host-contract layers ==="
npm test 2>&1 | grep -E 'Test Files|Tests '

echo
echo "=== 0 identifiers returned, against 1552 with the policy layer deleted ==="
sed -n '/ABLATION/,/Without it/p' bench/ablation.txt

echo
echo "=== 21 of 24: an agent never told the tool exists reaches for it ==="
python3 bench/tool-choice.py | sed -n '1,7p'

echo
echo "=== what a DOM-reading agent can see on the screen itself ==="
python3 bench/dom-check.py 2>/dev/null | tail -6 || sed -n '1,8p' bench/dom-check.txt

echo
echo "=== the deployed site, checked against the walkthrough ==="
python3 bench/live-check.py | tail -3

echo
echo "=== how many people this is for, asked of the BLS live ==="
python3 bench/population.py | sed -n '1,11p'

echo
echo "=== where this sits in the field, over all 868 other entries ==="
cd webmcp-evaluator && python3 field_position.py | sed -n '/Counting the same claim/,$p'
