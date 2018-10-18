#!/usr/bin/env bash
gunicorn -c query_service/gun_query_app.py query_app:app --daemon