#!/bin/bash

set -ex

uvicorn lime.main:app --reload --port 10000
# uvicorn lime.main:app --port 10000
