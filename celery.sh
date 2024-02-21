#!/usr/bin/env bash
#testing
#final test i swear
celery -A celeryworker  worker --loglevel=debug --concurrency=2
