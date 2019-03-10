#!/usr/bin/env bash
gunicorn -c query_service/gun_config.py app:app --daemon