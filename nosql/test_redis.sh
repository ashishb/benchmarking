#!/bin/bash
set -v
time python exec_redis.py set
time python exec_redis.py get
time python exec_redis.py dict_set
time python exec_redis.py dict_get
time python exec_redis.py set_add
time python exec_redis.py set_rem
time python exec_redis.py list_push
time python exec_redis.py list_pop
