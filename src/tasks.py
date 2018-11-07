# -*- coding: utf-8 -*-
from hello.celery import app


@app.task
def add(a, b):
    return a + b
