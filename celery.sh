#!/usr/bin/env bash
celery -A celeryworker  worker --loglevel=debug --concurrency=2
