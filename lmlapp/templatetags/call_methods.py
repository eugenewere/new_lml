import statistics
from datetime import date

from django import template
from django.shortcuts import render_to_response
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
        day = str(int(diff.days/365)) + str(' Years')
        return day
    elif diff.days < 365:
        day = str(int(diff.days/30)) + str(' Monthes')
        return day
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
    is_shortlisted = CompanyShortlistCustomers.objects.filter(customer_id=customer.id, company_id=request.user.id).exists()
    if is_shortlisted:
        return False
    return True

@register.filter(name='top_customer_categories')
def top_customer_categories(request):
    category = Customer.objects.annotate(itemcount=Count('id')).order_by('-itemcount')[:7]
    return category

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
     custShortlist =  CompanyShortlistCustomers.objects.filter(company_id=company_id,customer_id=customer_id).exists()
     if custShortlist:
         return False
     return True

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


