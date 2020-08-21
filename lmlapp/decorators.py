from django.core.exceptions import PermissionDenied
# from simple_decorators.apps.models import Entry
from django.shortcuts import redirect

from lmlappadmin.models import *

def has_user_paid_registration(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            user=request.user.id
            customer = Customer.objects.filter(user_ptr_id = user).first()
            company = Company.objects.filter(user_ptr_id = user).first()
            if customer:
                if Customer.objects.filter(user_ptr_id=user, regpayment__isnull=False, regpayment__payment_status='COMPLETED', regpayment__transaction_status='COMPLETED').first():
                    return function(request, *args, **kwargs)
                else:
                    return redirect('LML:payment')
            elif company:
                if Company.objects.filter(user_ptr_id=user, regpayment__isnull=False, regpayment__payment_status='COMPLETED', regpayment__transaction_status='COMPLETED').first():
                    return function(request, *args, **kwargs)
                else:
                    return redirect('LML:companypayment')
            else:
                raise PermissionDenied
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


 # entry = Entry.objects.get(pk=kwargs['entry_id'])
        # if entry.created_by == request.user:
        #     return function(request, *args, **kwargs)
        # else:
        #     raise PermissionDenied