#!/usr/bin/env bash
gunicorn -c query_service/gun_config.py app:app --daemon \
&& python schedule_service/scheduler.py