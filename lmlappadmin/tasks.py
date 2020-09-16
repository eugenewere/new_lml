from __future__ import  absolute_import, unicode_literals
from celery import  shared_task

import time

from lmlappadmin.models import *


@shared_task
def sum(a, b):
    time.sleep(5)
    return a+b


@shared_task
def checkforstatuspayexpiry():
    for company in Company.objects.exclude(rank_status='UNDEFINED').all():
        c = CompanyStatusPayment.objects.filter(company=company).order_by('-created_at').first()
        if c.getexpiryremainingdays == 'EXPIRED':
           Company.objects.filter(id=company.id).update(
               rank_status='UNDEFINED',
           )
    print('Status was checked')
    return 'Companies Were Checked'
