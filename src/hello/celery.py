# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('hello')
app.conf.update(broker_url='redis://:vNmJVW4vp3eiSmPe@54.223.163.72:6379/7')
app.conf.update(result_backend='redis://:vNmJVW4vp3eiSmPe@54.223.163.72:6379/7')
app.conf.update(imports=['tasks'])