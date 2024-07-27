#!/bin/bash

set -ex

uvicorn lime.main:app --reload --port 10000
