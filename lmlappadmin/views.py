from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
import sweetify
# Create your views here.
# from lmlappadmin.models import *
from .models import *
@login_required()
def home(request):
    customer_count = Customer.objects.all().count()
    company_count = Company.objects.all().count()
    from datetime import datetime, timedelta

    one_week_ago = datetime.today() - timedelta(days=7)
    two_week_ago = datetime.today() - timedelta(days=14)

    customer_count_this_week = Customer.objects.filter(created_at__gte=one_week_ago).count()
    company_count_this_week = Company.objects.filter(created_at__gte=one_week_ago).count()
    company_count_two_week_ago= Company.objects.filter(created_at__gte=two_week_ago).count()
    customer_count_two_week_ago = Customer.objects.filter(created_at__gte=two_week_ago).count()
    recent_companies = Company.objects.order_by('-created_at')
    recent_employees = Customer.objects.order_by('-created_at')

    commpany_messages_count =  ContactUsCompany.objects.all().count()
    customer_messages_count =  ContactUsEmployee.objects.all().count()
    random_messages = ContactUsHome.objects.all().count()

    context={
        'title': 'Dash',
        'customer_count':customer_count,
        'company_count':company_count,
        'customer_count_this_week':customer_count_this_week,
        'company_count_this_week':company_count_this_week,
        'customer_count_two_week_ago':customer_count_two_week_ago,
        'company_count_two_week_ago':company_count_two_week_ago,
        'recent_companies':recent_companies,
        'recent_employees': recent_employees,
        'commpany_messages_count':commpany_messages_count,
        'customer_messages_count':customer_messages_count,
        'random_messages':random_messages,
    }
    return render(request,'admin/index.html', context)

@login_required()
def employee_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/employee.html', context)

@login_required()
def random_messages(request):
    contactushome = ContactUsHome.objects.order_by("-created_at")
    context = {
        'title': 'Random Messages',
        'messages':contactushome,
        'messagecount':contactushome.count(),
        'inboxcount': ContactUsHome.objects.filter(status="UNREAD").count()
    }
    return render(request, 'messages/RandomMessages.html', context)

@login_required()
def company_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/company.html', context)

@login_required()
def employees(request):
    employees = Customer.objects.order_by('-created_at')
    context = {
        'title': 'Employees',
        'customers': employees,
    }
    return render(request,'employee/allemployees.html', context)

@login_required()
def premiumemployees(request):
    employees = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    context = {
        'title': 'PremiumEmployees',
        'customers': employees,
    }
    return render(request,'employee/premiumemployees.html', context)

@login_required()
def shortlistedemployees(request):

     # = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    # customers =[]
    employ = CompanyShortlistCustomers.objects.filter()
    context = {
        'title': 'ShortlistedEmployees',
        'customers': employ,
    }
    return render(request,'employee/shortlistedemployies.html', context)

@login_required()
def registeredemployees(request):

    employ = Customer.objects.filter(regpayment_id__isnull=False)
    context = {
        'title': 'RegisteredEmployees',
        'customers': employ,
    }
    return render(request,'employee/registeredemployees.html', context)

@login_required()
def deactivatedemployees(request):

    employ = Customer.objects.filter(status='DEACTIVATED')
    context = {
        'title': 'DeactivatedEmployees',
        'customers': employ,
    }
    return render(request,'employee/deactivatedemployees.html', context)



@login_required()
def companies(request):
    company = Company.objects.all()

    context = {
        'title': 'Companies',
        'companies': company,
    }
    return render(request, 'company/company.html', context)

@login_required()
def premiumcompanies(request):
    company = Company.objects.filter(rank_status='PREMIUM')

    context = {
        'title': 'Premium Companies',
        'companies': company,
    }
    return render(request, 'company/premiumcompanies.html', context)

@login_required()
def platinumcompanies(request):
    company = Company.objects.filter(rank_status='PLATINUM')

    context = {
        'title': 'Platinum Companies',
        'companies': company,
    }
    return render(request, 'company/platinumcompanies.html', context)

@login_required()
def basiccompanies(request):
    company = Company.objects.filter(rank_status='BASIC')

    context = {
        'title': 'Basic Companies',
        'companies': company,
    }
    return render(request, 'company/basiccompanies.html', context)

@login_required()
def probasiccompanies(request):
    company = Company.objects.filter(rank_status='PRO_BASIC')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'company/probasiccompanies.html', context)


@login_required()
def proultimatecompanies(request):
    company = Company.objects.filter(rank_status='PRO_ULTIMATE')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'company/proultimatecompanies.html', context)

@login_required()
def ultimatecompanies(request):
    company = Company.objects.filter(rank_status='ULTIMATE')

    context = {
        'title': 'Ultimate Companies',
        'companies': company,
    }
    return render(request, 'company/ultimatecompany.html', context)

@login_required()
def undefinedcompanies(request):
    company = Company.objects.filter(rank_status='UNDEFINED')

    context = {
        'title': 'Undefined Companies',
        'companies': company,
    }
    return render(request, 'company/undefinedcompanies.html', context)

@login_required()
def companiesregpayment(request):
    company = Company.objects.filter(regpayment_id__isnull=False)

    context = {
        'title': 'Company Registration Payment',
        'companies': company,
    }
    return render(request, 'company/registrationpayment.html', context)

def deactivatedemployers(request):
    company = Company.objects.filter(status='DEACTIVATED')

    context = {
        'title': 'Deactivated Company',
        'companies': company,
    }
    return render(request, 'company/deactivatedcompanies.html', context)





def companyPricing(request):
    pricing = CompanyPricingPlan.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        description = request.POST['description']
        CompanyPricingPlan.objects.create(
            title=title,
            price=price,
            description=description
        )
        sweetify.success(request, 'Success', text='Price Added', persistent='Ok')
    else:
        pricing = CompanyPricingPlan.objects.all()


    context = {
        'title': 'Companies Pricing',
        'pricings': pricing

    }
    return render(request, 'company/companypricing.html', context)


@login_required()
def categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'Categories',
        'categories': categories,
    }
    return render(request, 'categories/categories.html',context)


def carouselImages(request):
    if request.method == 'POST':
        image = request.FILES['carousel_image']
        img = AdvertCarousel.objects.create(
            carousel_image=image
        )
        if img:
            sweetify.success(request, 'Success', text='Advert Added Successfully', persistent='Ok')
            return redirect('LMLAdmin:carouselImages')
        else:
            sweetify.error(request, 'Error', text='Error adding', persistent='Retry')
            return redirect('LMLAdmin:carouselImages')

    context = {
        'title': 'Categories',
        'images': AdvertCarousel.objects.order_by('-created_at'),
    }
    return render(request, 'advertimages/carouselimages.html', context)


def customer_graph(request):
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))
    labels2 = months_choices
    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))
    for months_choice in months_choices_int:
        month_data.append(
            Customer.objects.filter(created_at__month=months_choice).count())
    defaultData2 = month_data
    context2 = {
        'labels2': labels2,
        'defaultData2': defaultData2,

    }

    return JsonResponse(context2)


def company_graph(request):
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))
    labels3 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))
    for months_choice in months_choices_int:
        month_data.append(Company.objects.filter(created_at__month=months_choice).count())
    defaultData3 = month_data
    context2 = {
        'labels3': labels3,
        'defaultData3': defaultData3,

    }
    return JsonResponse(context2)

def messages_graph(request):
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))
    labels4 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))
    for months_choice in months_choices_int:
        month_data.append(ContactUsHome.objects.filter(created_at__month=months_choice).count())
    defaultData4 = month_data

    context2 = {
        'labels4': labels4,
        'defaultData4': defaultData4,

    }
    return JsonResponse(context2)


def reply_to_random_messages_via_email(request, source):
    sourcez = source.replace('____', '/')
    if request.method == "POST":
        body = request.POST['message']
        subject = request.POST['subject']
        emails = Newsletter.objects.all()

        # NewsletterMessage.objects.create(
        #     subject=subject,
        #     message=body,
        #     email_count=emails.count()
        # )
        #
        # messages.success(request, 'Messages Saved')
        # for email in emails:
        #     email_from = settings.EMAIL_HOST_USER
        #     recipient_list = [email.email, ]
        #     send_mail(
        #         subject=subject,
        #         message=body,
        #         from_email=email_from,
        #         recipient_list=recipient_list
        #     )
        # messages.success(request, 'Emails sent')
        # return redirect('CCSBADMIN:newsLetter')
    return redirect(sourcez)
