from __future__ import  absolute_import, unicode_literals
from celery import  shared_task

import time

from lmlappadmin.models import Company


@shared_task
def sum(a, b):
    time.sleep(5)
    return a+b

@shared_task
def checkforstatuspayexpiry():
    for candidate in Company.objects.all():
        if candidate.getexpiryremainingdays == 'EXPIRED':
           Company.objects.filter(id=candidate.id).update(
               rank_status='UNDEFINED',
           )
    print('Status was checked')
    return 'Companies Were Checked'
