#!/bin/bash

set -ex

basket maas use Lime

basket model use Qwen/Qwen2-7B-Instruct

basket chat "what is the meaning of life?"
