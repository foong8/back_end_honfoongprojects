from background_task import background
from datetime import datetime
from background_task.models import Task
import time

from .custom_script import process_qc


@background()
def testing():
    print(datetime.now())
    process_qc()


Task.objects.all().delete()
testing(repeat=2)

