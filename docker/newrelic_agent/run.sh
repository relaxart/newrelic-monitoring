#!/usr/bin/env bash
set -e
python config.py > config.yaml
newrelic-plugin-agent -f -c /usr/local/bin/agent/config.yaml