from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'update-news': {
        'task': 'app.taskQueue.updateNews',
        'schedule': timedelta(seconds=10),
    },

}
