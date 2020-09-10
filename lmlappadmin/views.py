from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
import sweetify
# Create your views here.
# from lmlappadmin.models import *
from datetime import timedelta, date
from lmlapp.forms import *
from .models import *
@login_required()
def home(request):
    customer_count = Customer.objects.all().count()
    company_count = Company.objects.all().count()
    from datetime import datetime, timedelta

    one_week_ago = datetime.today() - timedelta(days=7)
    two_week_ago = datetime.today() - timedelta(days=14)

    customer_reg_count = Customer.objects.filter(regpayment__isnull=False, regpayment__payment_status='COMPLETED', regpayment__transaction_status='COMPLETED').count()
    customer_unreg_count = Customer.objects.filter(regpayment__isnull=True).count()

    company_reg_count = Company.objects.filter(regpayment__isnull=False, regpayment__payment_status='COMPLETED', regpayment__transaction_status='COMPLETED').count()
    company_unreg_count = Company.objects.filter(regpayment__isnull=True,).count()


    recent_companies = Company.objects.order_by('-created_at')
    recent_employees = Customer.objects.order_by('-created_at')

    commpany_messages_count =  ContactUsCompany.objects.all().count()
    customer_messages_count =  ContactUsEmployee.objects.all().count()
    random_messages = ContactUsHome.objects.all().count()

    context={
        'title': 'Dash',
        'customer_count':customer_count,
        'company_count':company_count,
        'customer_reg_count':customer_reg_count,
        'customer_unreg_count':customer_unreg_count,
        'company_reg_count':company_reg_count,
        'company_unreg_count':company_unreg_count,
        'recent_companies':recent_companies,
        'recent_employees': recent_employees,
        'commpany_messages_count':commpany_messages_count,
        'customer_messages_count':customer_messages_count,
        'random_messages':random_messages,
    }
    return render(request, 'aanewadminportal/home/index2.html', context)

def useradminaccount(request):
    context={
        'title': request.user.username+ ' Account',
        'user': User.objects.filter(id=request.user.id).first()
    }
    return render(request, 'aanewadminportal/account/account.html', context)
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
    return render(request,'aanewadminportal/candidates/allcandidates.html', context)

@login_required()
def premiumemployees(request):
    employees = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    context = {
        'title': 'Premium Employees',
        'customers': employees,
    }
    return render(request,'aanewadminportal/candidates/premiumCandidates.html', context)
@login_required()
def basicemployees(request):
    employees = Customer.objects.filter(rank_status='BASIC').order_by('-created_at')
    context = {
        'title': 'Basic Employees',
        'customers': employees,
    }
    return render(request,'aanewadminportal/candidates/basicCandidates.html', context)
@login_required()
def ultimateemployees(request):
    employees = Customer.objects.filter(rank_status='ULTIMATE').order_by('-created_at')
    context = {
        'title': 'Ultimate Employees',
        'customers': employees,
    }
    return render(request,'aanewadminportal/candidates/ultimateCandidates.html', context)

@login_required()
def shortlistedemployees(request):

     # = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    # customers =[]
    employ = CompanyShortlistCustomers.objects.filter(payment_status='SHORTLISTED').order_by('-created_at')
    context = {
        'title': 'ShortlistedEmployees',
        'customers': employ,
    }
    return render(request,'aanewadminportal/candidates/shortlistedCandidates.html', context)

@login_required()
def allshortlistedemployeeshistory(request):
    employ = CompanyShortlistCustomers.objects.all().order_by('-created_at')
    context = {
        'title': 'Shortlisted History',
        'customers': employ,
    }
    return render(request,'employee/allshortlistinghistory.html', context)

@login_required()
def registeredemployees(request):

    employ = Customer.objects.filter(regpayment_id__isnull=False)
    # employ = Customer.objects.filter(regpayment__payment_status="PAYED")
    context = {
        'title': 'RegisteredEmployees',
        'customers': employ,
    }
    return render(request,'aanewadminportal/candidates/registeredCandidates.html', context)

@login_required()
def unregipayedemployees(request):

    employ = Customer.objects.filter(regpayment__payment_status="UNPAYED", regpayment_id__isnull=True)
    # employ = Customer.objects.all()
    context = {
        'title': 'RegisteredEmployees',
        'customers': employ,
    }
    return render(request,'aanewadminportal/candidates/unregisteredCandidates.html', context)

@login_required()
def deactivatedemployees(request):

    employ = Customer.objects.filter(status='DEACTIVATED')
    context = {
        'title': 'DeactivatedEmployees',
        'customers': employ,
    }
    return render(request,'aanewadminportal/candidates/deactivatedCandidates.html', context)






@login_required()
def companies(request):
    company = Company.objects.order_by('-created_at')

    context = {
        'title': 'Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/allcompanies.html', context)


@login_required()
def companydetails(request, company_id):
    company = Company.objects.filter(id=company_id).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    print(social)
    context = {
        'title': 'Companies',
        'company': company,
        'social': social,
    }
    return render(request, 'company/companydetails.html', context)



@login_required()
def premiumcompanies(request):
    company = Company.objects.filter(rank_status='PREMIUM')

    context = {
        'title': 'Premium Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/premium.html', context)

@login_required()
def platinumcompanies(request):
    company = Company.objects.filter(rank_status='PLATINUM')

    context = {
        'title': 'Platinum Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/platinumcompany.html', context)

@login_required()
def basiccompanies(request):
    company = Company.objects.filter(rank_status='BASIC')

    context = {
        'title': 'Basic Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/basic.html', context)

@login_required()
def probasiccompanies(request):
    company = Company.objects.filter(rank_status='PRO_BASIC')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/probasic.html', context)


@login_required()
def proultimatecompanies(request):
    company = Company.objects.filter(rank_status='PRO_ULTIMATE')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/proultimate.html', context)

@login_required()
def ultimatecompanies(request):
    company = Company.objects.filter(rank_status='ULTIMATE')

    context = {
        'title': 'Ultimate Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/ultimate.html', context)

@login_required()
def undefinedcompanies(request):
    company = Company.objects.filter(rank_status='UNDEFINED')

    context = {
        'title': 'Undefined Companies',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/undefined.html', context)

@login_required()
def companiesregpayment(request):
    company = Company.objects.filter(regpayment_id__isnull=False, regpayment__payment_status="PAYED", )

    context = {
        'title': 'Company Registration Payment',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/regpay.html', context)

@login_required()
def companiesregunpayment(request):
    company = Company.objects.filter(regpayment_id__isnull=True, regpayment__payment_status="UNPAYED", )

    context = {
        'title': 'Company Registration UnPayed',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/unregpay.html', context)




def deactivatedemployers(request):
    company = Company.objects.filter(status='DEACTIVATED')

    context = {
        'title': 'Deactivated Company',
        'companies': company,
    }
    return render(request, 'aanewadminportal/companies/deactivatedcompanies.html', context)





def companyPricing(request):
    pricing = CompanyPricingPlan.objects.all()


    context = {
        'title': 'Companies Pricing',
        'pricings': pricing

    }
    return render(request, 'aanewadminportal/companies/compnypricing.html', context)

def addcompanyPricing(request):
    # pricing = CompanyPricingPlan.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')

        shortlist_access = request.POST.get('shortlist_access')
        review_access = request.POST.get('review_access')
        no_of_candidates = request.POST.get('no_of_candidates')
        chat_with_candidates = request.POST.get('chat_with_candidates')
        view_lml_cv = request.POST.get('view_lml_cv')
        view_user_own_cv = request.POST.get('view_user_own_cv')
        print(shortlist_access, review_access, no_of_candidates, chat_with_candidates, view_lml_cv, view_user_own_cv)
        cpp = CompanyPricingPlan.objects.create(
            title=title.capitalize(),
            price=price,
            status=status.upper(),
            description=description
        )
        CompanyPricingDetails.objects.create(
            pricing=cpp,
            shortlist_access=shortlist_access,
            review_access=review_access,
            no_of_candidates=no_of_candidates,
            chat_with_candidates=chat_with_candidates,
            view_lml_cv=view_lml_cv,
            view_user_own_cv=view_user_own_cv,

        )
        sweetify.success(request, 'Success', text='Price Added', persistent='Ok')


    return redirect(request.META['HTTP_REFERER'])

def editcompanyPricing(request, price_id):

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        status = request.POST.get('status')
        description = request.POST.get('description')

        shortlist_access = request.POST.get('shortlist_access')
        review_access = request.POST.get('review_access')
        no_of_candidates = request.POST.get('no_of_candidates')
        chat_with_candidates = request.POST.get('chat_with_candidates')
        view_lml_cv = request.POST.get('view_lml_cv')
        view_user_own_cv = request.POST.get('view_user_own_cv')
        pricing = CompanyPricingPlan.objects.filter(id=price_id).first()
        if pricing is not None:
            CompanyPricingPlan.objects.filter(id=pricing.id).update(
                title=title.capitalize(),
                price=price,
                status=status.upper(),
                description=description
            )
            CompanyPricingDetails.objects.filter(pricing=pricing).update(
                shortlist_access=shortlist_access,
                review_access=review_access,
                no_of_candidates=no_of_candidates,
                chat_with_candidates=chat_with_candidates,
                view_lml_cv=view_lml_cv,
                view_user_own_cv=view_user_own_cv,

            )
            sweetify.success(request, 'Success', text='Price Updated', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Price Does Not Exist', persistent='Ok')


    return redirect(request.META['HTTP_REFERER'])

def deletecompanyPricing(request, price_id):
    pricing = CompanyPricingPlan.objects.filter(id=price_id).first()
    if pricing is not None:
        pricing.delete()
        sweetify.success(request, 'Success', text='Price Deleted', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='Price Not Deleted', persistent='Ok')

    return redirect(request.META['HTTP_REFERER'])

def deleteallcompanyPricing(request):
    pricings = CompanyPricingPlan.objects.all()
    if pricings is not None:
        for pricing in pricings:
            pricing.delete()
        sweetify.success(request, 'Success', text='All Prices Deleted', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='All Prices Not Deleted', persistent='Ok')

    return redirect(request.META['HTTP_REFERER'])



@login_required()
def categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'Categories',
        'categories': categories,
    }
    return render(request, 'aanewadminportal/categories/categories.html',context)


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
    return render(request, 'aanewadminportal/carousel/carousel.html', context)


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

def registration_graph(request):
    company_month_data = []
    candidate_month_data = []
    months_choices = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    months_choices_int = []
    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        company_month_data.append(CompanyRegistrationPayment.objects.filter(created_at__month=months_choice).count())

    for months_choice in months_choices_int:
        candidate_month_data.append(CandidateRegPrice.objects.filter(created_at__month=months_choice).count())
    context = {
        'labels': months_choices,
        'companydata': company_month_data,
        'candidatedata': candidate_month_data,

    }

    return JsonResponse(context)

def companystatuspaymentgraph(request):
    company_month_data = []
    months_choices = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    months_choices_int = []
    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        val=[]
        for c in CompanyStatusPayment.objects.filter(created_at__month=months_choice).all():
            val.append(int(c.amount))
        company_month_data.append(sum(val))
    context = {
        'labels': months_choices,
        'companydata': company_month_data,

    }

    return JsonResponse(context)

def companystatuspaymentgraphtime(request):
    company_days_data = []
    days_choices = []
    if request.method == 'POST':
        startdate = request.POST.get('statuspaychartselectstartdate')
        enddate = request.POST.get('statuspaychartselectenddate')
        # CompanyRegistrationPayment.objects.filter(created_at__day=)
        if startdate and enddate:
            if enddate > startdate:
                start_date = datetime.datetime.strptime(startdate, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(enddate, '%Y-%m-%d')
                for single_date in daterange(start_date, end_date):
                    days_choices.append(single_date.strftime("%B")[:3] + ' ' + str(single_date.strftime("%d")))
                for single_date in daterange(start_date, end_date):
                    val = []
                    for c in CompanyStatusPayment.objects.filter(created_at__day=single_date.strftime("%d"),created_at__year=single_date.strftime("%Y"),created_at__month=single_date.strftime("%m")):
                        val.append(int(c.amount))
                    company_days_data.append(sum(val))
                print(company_days_data)
                context = {
                    'labels': days_choices,
                    'companydata': company_days_data,

                }
                return JsonResponse(context)
            else:
                print('less')
        else:
            print('required')









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

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def registration_graph_time(request):
    company_days_data = []
    candidate_days_data = []
    days_choices = []
    if request.method == 'POST':
        startdate = request.POST.get('registrationstartdate')
        enddate = request.POST.get('registrationenddate')
        # CompanyRegistrationPayment.objects.filter(created_at__day=)
        if startdate and enddate:
            if enddate > startdate:
                start_date = datetime.datetime.strptime(startdate, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(enddate, '%Y-%m-%d')
                for single_date in daterange(start_date, end_date):
                    days_choices.append(single_date.strftime("%B")[:3] + ' ' + str(single_date.strftime("%d")))
                for single_date in daterange(start_date, end_date):
                    company_days_data.append(CompanyRegistrationPayment.objects.filter(created_at__day=single_date.strftime("%d"), created_at__year=single_date.strftime("%Y"), created_at__month=single_date.strftime("%m")).count())
                    candidate_days_data.append(CandidateRegPrice.objects.filter(created_at__day=single_date.strftime("%d"), created_at__year=single_date.strftime("%Y"), created_at__month=single_date.strftime("%m")).count())
                context = {
                    'labels': days_choices,
                    'companydata': company_days_data,
                    'candidatedata': candidate_days_data,

                }
                return JsonResponse(context)
            else:
                print('less')
        else:
            print('required')

def company_graph_time_filter(request):
    months_choice = []
    days_data = []
    days_choices = []
    days_choices_int = []
    if request.method == 'POST':
        startdate = request.POST.get('companystartdate')
        enddate = request.POST.get('companyenddate')
        # CompanyRegistrationPayment.objects.filter(created_at__day=)
        if startdate  and enddate:
            if enddate > startdate:
                # print(startdate, enddate)
                #     s = datetime.datetime.strptime(startdate,'%Y-%m-%d').month
                #     sd = datetime.datetime.strptime(startdate,'%Y-%m-%d').day
                #     sy = datetime.datetime.strptime(startdate,'%Y-%m-%d').year
                #
                #     e = datetime.datetime.strptime(enddate,'%Y-%m-%d').month
                #     ed = datetime.datetime.strptime(enddate,'%Y-%m-%d').day
                #     # print(s)
                #
                #     for m in range(s, e):
                #         print(m, s, e)
                #         for i in range(sd, (ed+1)):
                #             days_choices.append((datetime.date(sy, m, i).strftime('%B')[0:3]) + ' ' + str((datetime.date(sy, m, i).strftime('%d'))))
                #     print(days_choices)
                #
                #     for z in range(sd, (ed+1)):
                #         days_choices_int.append((datetime.date(sy, s, z).strftime('%d')))
                #     print(days_choices_int)
                start_date = datetime.datetime.strptime(startdate,'%Y-%m-%d')
                end_date = datetime.datetime.strptime(enddate,'%Y-%m-%d')
                for single_date in daterange(start_date, end_date):
                    days_choices.append(single_date.strftime("%B")[:3] +' '+ str(single_date.strftime("%d")))

                # print(days_choices)

                for single_date in daterange(start_date, end_date):
                    # print(single_date)
                    # print(single_date.strftime("%Y-%m-%d"))
                    days_data.append(Company.objects.filter(created_at__day=single_date.strftime("%d"), created_at__year=single_date.strftime("%Y"), created_at__month=single_date.strftime("%m")).count())

                # print(days_data)
                context2 = {
                    'labels3': days_choices,
                    'defaultData3': days_data,

                }
                # pass
                return JsonResponse(context2)
            else:
                print('less')
        else:
            print('required')

def candidate_graph_time_filter(request):
    days_data = []
    days_choices = []
    if request.method == 'POST':
        startdate = request.POST.get('candidatestartdate')
        enddate = request.POST.get('candidateenddate')
        if startdate  and enddate:
            if enddate > startdate:
                start_date = datetime.datetime.strptime(startdate,'%Y-%m-%d')
                end_date = datetime.datetime.strptime(enddate,'%Y-%m-%d')
                for single_date in daterange(start_date, end_date):
                    days_choices.append(single_date.strftime("%B")[:3] +' '+ str(single_date.strftime("%d")))
                for single_date in daterange(start_date, end_date):
                    days_data.append(Customer.objects.filter(created_at__day=single_date.strftime("%d"), created_at__year=single_date.strftime("%Y"), created_at__month=single_date.strftime("%m")).count())

                # print(days_data)
                context2 = {
                    'labels3': days_choices,
                    'defaultData3': days_data,

                }
                # pass
                return JsonResponse(context2)
            else:
                print('less')
        else:
            print('required')



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


def whatweoffer(request):
    context={
        'whatweoffer':WhatWeOffer.objects.all()
    }
    return render(request, 'aanewadminportal/settings/whatweoffer.html' , context)


def addwhatweoffer(request):
    if request.method == "POST":
        icon = request.POST.get('icon')
        title = request.POST.get('title')
        description = request.POST.get('description')
        WhatWeOffer.objects.create(
            icon=icon,
            title=title,
            description=description,
        )
        sweetify.success(request, 'Success', text='Offer Added Successfully', persistent='Ok')

    else:
        sweetify.error(request, 'Error', text='Error adding the offer', persistent='Retry')

    return redirect('LMLAdmin:whatweoffer')


def editwhatweoffer(request, offer_id):
    w = WhatWeOffer.objects.filter(id= offer_id).first()
    if request.method == "POST":
        icon = request.POST.get('icon')
        title = request.POST.get('title')
        description = request.POST.get('description')
        WhatWeOffer.objects.filter(id=w.id).update(
            icon=icon,
            title=title,
            description=description,
        )
        sweetify.success(request, 'Success', text='Offer Updated Successfully', persistent='Ok')

    else:
        sweetify.error(request, 'Error', text='Error updating the offer', persistent='Retry')

    return redirect('LMLAdmin:whatweoffer')


def deletewhatweoffer(request, offer_id):
    w = WhatWeOffer.objects.filter(id=offer_id).first()
    if w is not None:
        # w.delete()
        sweetify.success(request, 'Success', text='Offer deleted', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='Error deleting the offer', persistent='Retry')

    return redirect('LMLAdmin:whatweoffer')


def employeesdetails(request, customer_id):
    customer = Customer.objects.filter(id=customer_id).first()
    reg = CustomerRegNo.objects.filter(customer=customer).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    socials = Social_account.objects.filter(customer=customer)
    context={
        'title':customer.first_name+' Details',
        'employee':customer,
        'reg':reg,
        'skills':skills,
        'educations':educations,
        'experiences':experiences,
        'socials':socials,
    }
    return render(request, 'employee/employeedetails.html', context)

def changecandidatestatustonewbee(request, custom_id):
    custom = Customer.objects.filter(id=custom_id).first()
    if custom is not None:
        Customer.objects.filter(id=custom.id).update(
            status="NEWBIE"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.success(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])


def changecandidatestatustoregi(request,custom_id):
    custom = Customer.objects.filter(id=custom_id).first()
    if custom is not None:
        Customer.objects.filter(id=custom.id).update(
            status="REGISTERED_CONFIRMED"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])


def changecandidatestatustodeac(request,custom_id):
    custom = Customer.objects.filter(id=custom_id).first()
    if custom is not None:
        Customer.objects.filter(id=custom.id).update(
            status="DEACTIVATED"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.success(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])


def changecompanystatustonewbee(request, custom_id):
    custom = Company.objects.filter(id=custom_id).first()
    if custom is not None:
        Company.objects.filter(id=custom.id).update(
            status="NEWBIE"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.success(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])
    # return redirect('LMLAdmin:companies')


def changecompanystatustoregi(request,custom_id):
    custom = Company.objects.filter(id=custom_id).first()
    if custom is not None:
        Company.objects.filter(id=custom.id).update(
            status="REGISTERED_CONFIRMED"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.success(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])
    # return redirect('LMLAdmin:companies')


def changecompanystatustodeac(request,custom_id):
    custom = Company.objects.filter(id=custom_id).first()
    if custom is not None:
        Company.objects.filter(id=custom.id).update(
            status="DEACTIVATED"
        )
        sweetify.success(request, 'Success', text='Status changed', persistent='Ok')
    else:
        sweetify.success(request, 'Error', text='Status not changed', persistent='Ok')
    return redirect(request.META['HTTP_REFERER'])
    # return redirect('LMLAdmin:companies')




@login_required()
def candidateregpricing(request):
    p = CandidateRegPrice.objects.all()
    context = {
        'pricings': p
    }
    return render(request, 'aanewadminportal/settings/canregprice.html', context)
def candidateaddregpricing(request):
    if request.method == "POST":
        price= request.POST.get('price')
        if not price == 0:
            CandidateRegPrice.objects.create(
                price=price,
            )
            sweetify.success(request, 'Success', text='Price Added', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Adding Price, Try Again', persistent='Ok')

    return redirect('LMLAdmin:candidateregpricing')
def candidateupdateregpricing(request, price_id):
    pricer=CandidateRegPrice.objects.filter(id=price_id).first()
    if request.method == "POST":
        price = request.POST.get('price')
        if not price == 0:
            CandidateRegPrice.objects.filter(id=pricer.id).update(
                price=price,
            )
            sweetify.success(request, 'Success', text='Price Updated', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Updating Price, Try Again', persistent='Ok')

    return redirect('LMLAdmin:candidateregpricing')
def candidatedeleteregpricing(request, price_id):
    price = CandidateRegPrice.objects.filter(id=price_id).first()
    if price is not None:
        price.delete()
        sweetify.success(request, 'Success', text='Price Deleted', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='Error Deleting Price', persistent='Ok')
    return redirect('LMLAdmin:candidateregpricing')
def candidatestatusregpricing(request, price_id):
    price = CandidateRegPrice.objects.filter(id=price_id).first()
    if price.status == "ACTIVE":
        CandidateRegPrice.objects.filter(id=price.id).update(
            status="INACTIVE",
        )
        pp = CandidateRegPrice.objects.filter(status="ACTIVE").count()
        if pp <= 0:
            CandidateRegPrice.objects.first().update(
                status="ACTIVE",
            )

        sweetify.success(request, 'Price Status Updated Successfully')

    elif price.status == "INACTIVE":
        CandidateRegPrice.objects.exclude(id=price.id).update(
            status="INACTIVE",
        )
        CandidateRegPrice.objects.filter(id=price.id).update(
            status="ACTIVE",
        )
        sweetify.success(request, 'Price Status Updated Successfully')
    return redirect('LMLAdmin:candidateregpricing')


@login_required()
def companyregpricing(request):
    p = CompanyRegPrice.objects.all()
    context = {
        'pricings': p
    }
    return render(request, 'aanewadminportal/settings/compregprice.html', context)
def companyaddregpricing(request):
    if request.method == "POST":
        price= request.POST.get('price')
        if not price == 0:
            CompanyRegPrice.objects.create(
                price=price,
            )
            sweetify.success(request, 'Success', text='Price Added', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Adding Price, Try Again', persistent='Ok')

    return redirect('LMLAdmin:companyregpricing')
def companyupdateregpricing(request, price_id):
    pricer=CompanyRegPrice.objects.filter(id=price_id).first()
    if request.method == "POST":
        price = request.POST.get('price')
        if not price == 0:
            CompanyRegPrice.objects.filter(id=pricer.id).update(
                price=price,
            )
            sweetify.success(request, 'Success', text='Price Updated', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Updating Price, Try Again', persistent='Ok')

    return redirect('LMLAdmin:companyregpricing')
def companydeleteregpricing(request, price_id):
    price = CompanyRegPrice.objects.filter(id=price_id).first()
    if price is not None:
        price.delete()
        sweetify.success(request, 'Success', text='Price Deleted', persistent='Ok')
    else:
        sweetify.error(request, 'Error', text='Error Deleting Price', persistent='Ok')
    return redirect('LMLAdmin:companyregpricing')
def companystatusregpricing(request, price_id):
    price = CompanyRegPrice.objects.filter(id=price_id).first()
    if price.status == "ACTIVE":
        CompanyRegPrice.objects.filter(id=price.id).update(
            status="INACTIVE",
        )
        pp = CompanyRegPrice.objects.filter(status="ACTIVE").count()
        if pp <= 0:
            CompanyRegPrice.objects.first().update(
                status="ACTIVE",
            )

        sweetify.success(request, 'Price Status Updated Successfully')

    elif price.status == "INACTIVE":
        CompanyRegPrice.objects.exclude(id=price.id).update(
            status="INACTIVE",
        )
        CompanyRegPrice.objects.filter(id=price.id).update(
            status="ACTIVE",
        )
        sweetify.success(request, 'Price Status Updated Successfully')
    return redirect('LMLAdmin:companyregpricing')

@login_required()
def analytics(request):
    context = {
        'title':'Analytics'
    }
    return render(request, 'aanewadminportal/graphs/analytics.html', context)


@login_required()
def admin_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            sweetify.success(request, title='Success', text='Successfully Password Changed.', persistent='Continue')
            return redirect("LMLAdmin:useradminaccount")
        else:
            form = PasswordChangeForm(request.user)
            print(form.error_messages)
            sweetify.error(request, 'Error', text='Password not Changed \n 1).Password did not match \n 2) Wrong Current Password' + str(form.errors), persistent='Retry')
            return redirect("LMLAdmin:useradminaccount")
    else:
        return redirect("LMLAdmin:useradminaccount")

@login_required()
def admin_edit_account(request):
    if request.method == 'POST':
        user = User.objects.filter(id=request.user.id).first()
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        lastl_name = request.POST.get('last_name')
        if user and user.is_superuser:
            User.objects.filter(id=user.id).update(
                email=email,
                username=username,
                first_name=first_name,
                last_name=lastl_name,
            )
            sweetify.success(request, title='Success', text='Successfully Updated Your Account.', persistent='Continue')
            return redirect("LMLAdmin:useradminaccount")
        else:

            sweetify.error(request, 'Error', text='User is none', persistent='Retry')
            return redirect("LMLAdmin:useradminaccount")
    else:
        return redirect("LMLAdmin:useradminaccount")


def county(request):
    context={
        'counties':County.objects.all()
    }
    return render(request, 'aanewadminportal/county/county.html', context)


def region(request):
    context = {
        'regions': Region.objects.all()
    }
    return render(request, 'aanewadminportal/Region/region.html', context)