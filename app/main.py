from fastapi import FastAPI, Body, Request
from fastapi.responses import Response
import worker

import time

app = FastAPI()

@app.get("/touch")
async def touch():
    return {"response": "OK"}

@app.post("/check_libs")
async def check_libs(data: str = Body(..., embed=True)):
    try:
        active_tasks = worker.get_active_tasks()
        if active_tasks:
            return 'Please wait current tasks:\n' + worker.get_str_tasks(active_tasks)
        task = worker.check_libs.delay(data)
        result = task.get(timeout=1, interval=0.2)
    except Exception as e:
        return f'Exception: {e}'
    return result
