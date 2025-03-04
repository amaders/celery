import os
from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL"))
logger = get_task_logger(__name__)
app.autodiscover_tasks()

@app.task
def add(x, y, z):
    logger.info(f'Adding {x} + {y}')
    print("FROM TASKS MESSAGE")
    return x + y + z
