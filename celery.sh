#!/usr/bin/env bash
#testing
celery -A celeryworker  worker --loglevel=debug --concurrency=2
