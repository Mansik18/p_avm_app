import os
import time
import inspect
import pickle
import importlib
import typing
from celery import Celery
from fastapi import Request


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
WORKER_NAME = os.getenv("WORKER_NAME")

worker = Celery(
    "worker",
    backend=CELERY_BROKER_URL,
    broker=CELERY_RESULT_BACKEND,
)
inspector = worker.control.inspect()


def get_str_tasks(tasks):
    return '\n'.join([f'Task: {task["name"]}, id: {task["id"]}' for task in tasks])

def get_active_tasks():
    global inspector
    tasks = inspector.active()[f'celery@{WORKER_NAME}']
    tasks = [{'name': task['name'], 'id': task['id'], 'time_start': task['time_start']} for task in  tasks]
    return tasks

@worker.task(name='check_libs')
def check_libs(data): 
    libs_status = {}
    try:
        for lib in data.split(';'):
            libs_status[lib] = importlib.util.find_spec(lib) is not None
    except Exception as e:
        return f'Exception: {e}'
    return libs_status
