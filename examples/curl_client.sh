#!/bin/bash

set -ex

curl -X POST "http://127.0.0.1:10000/v1/chat/completions" -H "Content-Type: application/json" -d '{
  "model": "Qwen/Qwen2-7B-Instruct",
  "messages": [{"role": "user", "content": "Who are you?"}]
}'