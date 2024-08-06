#!/bin/bash

set -ex

uvicorn lime.main:app --reload --port 10000

# nohup uvicorn lime.main:app --host 0.0.0.0 --port 10000 &
