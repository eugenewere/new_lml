import os
import re
import statistics
from datetime import date

from django import template
# from django.shortcuts import render_to_response
from django.views import View
from lmlappadmin.models import *


register = template.Library()

@register.filter(name='logged_in_company')
def logged_in_company(user):
    user_id = user.id
    company = Company.objects.filter(user_ptr_id=user_id).first()
    if company is not None:
        return company
    else:
        return False

@register.filter(name='logged_in_customer')
def logged_in_customer(user):
    user_id = user.id
    customer = Customer.objects.filter(user_ptr_id=user_id).first()
    if customer is not None:
        return customer
    else:
        return False

@register.filter(name='make_safe')
def make_safe(source):
    source = source.replace('/', '____')
    return "%s" %source

@register.filter(name='today')
def today(request):
    user = request.user.id
    today = date.today()
    # company = Company.objects.filter(user_ptr_id = user).first()
    # experience = ( (today.strftime("%Y")) - company.date_created)
    return today

@register.filter(name='experience_years')
def experience_years(experience_id):
    experience = Experience.objects.filter(id=experience_id).first()
    date_from = experience.date_from
    date_to = experience.date_to
    diff = date_to-date_from
    if diff.days > 365:
        day = str(int(diff.days/365))
        if int(day) > 1:
            return day + str(' Years')
        else:
            return day + str(' Year')
    elif diff.days < 365:
        day = str(int(diff.days/30))
        if int(day) > 1:
            return day + str(" Month's")
        else:
            return day + str(' Month')
    else:
        return 0


@register.filter(name='company_experience_years')
def company_experience_years(company_id):
    company = Company.objects.filter(id=int(company_id)).first()
    datex = company.date_created
    todayz = date.today()
    diff = todayz - datex
    if diff.days > 365:
        day = str(int(diff.days/365)) + str(' Years')
        return day
    elif diff.days < 365:
        day = str(int(diff.days/30)) + str(' Monthes')
        return day
    else:
        return 0




@register.filter(name='confirm_reg_payment')
def confirm_reg_payment(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user, regpayment__isnull=False).first()
    if customer:
        return False
    return True

@register.filter(name='confirm_company_reg_payment')
def confirm_company_reg_payment(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user, regpayment__isnull=False).first()
    if company:
        return False
    return True

@register.filter(name='shortlisted')
def shortlisted(request, customer_id):
    customer = Customer.objects.filter(user_ptr_id=customer_id).first()
    is_shortlisted = CompanyShortlistCustomers.objects.filter(customer_id=customer.id, company_id=request.user.id, payment_status='SHORTLISTED').exists()
    if is_shortlisted:
        return False
    return True

@register.filter(name='top_customer_categories')
def top_customer_categories(request):
    list_category =[]
    customer = Customer.objects.annotate(itemcount=Count('id')).order_by('-itemcount')
    for c in customer:
        list_category.append(c.category.category)


    return list(set(list_category))

@register.filter(name='contactushome')
def comments(request):
    contactushome = ContactUsHome.objects.filter(status="UNREAD").order_by("-created_at")
    if contactushome is not None:
        return contactushome
    return False

@register.filter(name='contactushomecount')
def commentscount(request):
    contactushomecount = ContactUsHome.objects.count()
    if contactushomecount > 0:
        return contactushomecount
    return False


@register.filter(name='if_company_has_shortlisted_the_customer')
def if_company_has_shortlisted_the_customer(customer_id, company_id):
     custShortlist =  CompanyShortlistCustomers.objects.filter(company_id=company_id,customer_id=customer_id, payment_status='SHORTLISTED').exists()
     if custShortlist:
         return False
     return True

@register.filter(name='replacestring')
def replacestring(request, s):
    # return re.sub('[^0-9a-zA-Z]+', '_', s)
    return re.sub('[^a-zA-Z0-9\n\.]', ' ', s)




@register.filter(name='average_ratings')
def average_ratings(customer_id):
    customer= Customer.objects.filter(user_ptr_id=customer_id).first()
    if customer is None:
        return False
    else:
        data = []
        ratings=CustomerReviews.objects.filter(customer=customer)
        for rating in ratings:
            data.append(rating.ratings)
        print(data)
        if data:
            average_ratings = statistics.mean(data)
            return average_ratings
        else:
            return 0

@register.filter(name='get_messege_reciever_image')
def get_messege_reciever_image(request, user_id):
    user = User.objects.filter(id=int(user_id)).first()
    candidate = Customer.objects.filter(user_ptr_id=user.id).first()
    if candidate:
        return candidate.profile_image.url
    else:
        return 'Noimage.jpg'

@register.filter(name='get_filename')
def get_filename(name):
    return os.path.basename(name)

@register.filter(name='sizify')
def sizify(value):
    # value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = 'kb'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'mb'
    else:
        value = value / 1073741824.0
        ext = 'gb'
    return '%s %s' % (str(round(value, 2)), ext.capitalize())


register.filter('sizify', sizify)




