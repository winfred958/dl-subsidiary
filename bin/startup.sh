#!/bin/bash

APP_HOME=$(
  cd "$(dirname "$0")"
  cd ..
  pwd
)

export PYTHONPATH=${APP_HOME}:${PYTHONPATH}

FAST_MAIN_PY=${APP_HOME}/main.py

python ${FAST_MAIN_PY}