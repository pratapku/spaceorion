import os

from celery import Celery
import webbrowser
from time import sleep


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print("HELLO Pankaj!!!!!!")

@app.task(bind=True)
def mytk(self):
    url = 'http://127.0.0.1:8000/schedulepinstimes/'

    while True:
        print("refreshing...")
        webbrowser.open(url, new=0)
        sleep(25)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')