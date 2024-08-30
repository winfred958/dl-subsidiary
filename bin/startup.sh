#!/bin/bash

APP_HOME=$(
  cd "$(dirname "$0")"
  cd ..
  pwd
)

export PYTHONPATH=${APP_HOME}:${PYTHONPATH}

export CUDA_VISIBLE_DEVICES=0
export MODELSCOPE_CACHE=/data/modelscope/cache

uvicorn main:app --host 0.0.0.0 --port 18088 --workers 2