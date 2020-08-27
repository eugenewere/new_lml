import urllib.request

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
import os
from datetime import datetime, timedelta
import sweetify
import humanize
# from django.contrib.humanize.templatetags.humanize import naturalday
from django.contrib.humanize.templatetags.humanize import *

# from rest_framework import status
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from lmlapp.decorators import has_user_paid_registration
from lmlapp.forms import *

from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.

# # Base method with no type specified
# sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')
#
# # Additional methods with the type already defined
# sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
# sweetify.success(self.request, 'You successfully changed your password')
# sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
# sweetify.warning(self.request, 'This is a warning... I guess')
import json

from lmlapp.pdf_util import render_to_pdf


def home(request):
    customers = Customer.objects.order_by('-created_at')[:6]
    all_customers = Customer.objects.all()
    loadCurrency()
    context = {
        'customers': customers,
        'all_customers': all_customers,
        'title': 'home',
        'counties': County.objects.all(),
        'categories': Category.objects.all(),
        'regions': Region.objects.all(),
        'bannercustomercount': Customer.objects.filter(status='REGISTERED_CONFIRMED'),
        'images': AdvertCarousel.objects.order_by('-created_at'),
        'offers': WhatWeOffer.objects.all()
    }

    return render(request, 'normal/home/index.html', context)


def loadCurrency():
    # 2020 - 0:  8 - 20:  22: 33:16.362734
    if CurrencyValue.objects.all().count() <= 0:
        contents = urllib.request.urlopen("https://openexchangerates.org/api/latest.json?app_id=71501b20f84c42cfa79667487398fd93").read()
        k = json.loads(contents)
        if k is not None and k['rates']['KES'] is not None:
            CurrencyValue.objects.create(
                currency=k['rates']['KES']
            )
    else:
        time_threshold = datetime.datetime.now() - timedelta(hours=12)
        jk = CurrencyValue.objects.first()
        if CurrencyValue.objects.filter(id=jk.id, created_at__lt=time_threshold).first():
            for r in CurrencyValue.objects.all():
                r.delete()
            loadCurrency()
    pass


def signup(request):
    if request.is_ajax() and request.method == 'POST':
        # print(request.POST)
        qualifications = request.POST.getlist('qualifications')
        schools = request.POST.getlist('school')
        courses = request.POST.getlist('course')
        graduation_dates = request.POST.getlist('graduation_date')
        regnos = request.POST.getlist('reg_number')

        employer_names = request.POST.getlist('employer_name')
        company_names = request.POST.getlist('company_name')
        company_emails = request.POST.getlist('company_email')
        company_phones = request.POST.getlist('company_phone')
        position_helds = request.POST.getlist('position_held')
        date_froms = request.POST.getlist('date_from')
        date_tos = request.POST.getlist('date_to')
        experiences = request.POST.getlist('experience')

        skills = request.POST.getlist('skill')
        referees = request.POST.getlist('referee')
        referee_phonenumbers = request.POST.getlist('referee_phonenumber')

        account_url = request.POST.get('account_url')

        password1 = request.POST.get('password1')
        username = request.POST.get('username')

        county = request.POST.get('county')
        country = request.POST.get('country')
        biography = request.POST.get('biography')
        password2 = request.POST.get('password2')
        print(county, country, password2, biography)

        form = PersonelRegisterForm(request.POST, request.FILES)

        def genRegNo(regnopers):
            if CustomerRegNo.objects.filter(personel_reg_no__exact=regnopers):
                regnoperss = ('PRN' + get_random_string(length=8, allowed_chars='ABCDFGHIJKLMNPQRSTUVWXYZ123456789'))
                genRegNo(regnoperss)
            else:
                return regnopers

        if form.is_valid():
            new_user = form.save()

            CustomerRegNo.objects.create(
                customer=new_user,
                personel_reg_no=genRegNo(
                    ('PRN' + get_random_string(length=8, allowed_chars='ABCDFGHIJKLMNPQRSTUVWXYZ123456789'))),
            )
            Social_account.objects.create(
                customer=new_user,
                account_url=account_url
            )

            for skill, referee, referee_phonenumber in zip(skills, referees, referee_phonenumbers):
                Skills.objects.create(
                    customer=new_user,
                    skill=skill,
                    referee=referee,
                    referee_phonenumber=referee_phonenumber
                )

            for qualification, school, course, graduation_date, regno in zip(qualifications, schools, courses,
                                                                             graduation_dates, regnos):
                Education.objects.create(
                    customer=new_user,
                    qualifications=qualification,
                    school=school,
                    course=course,
                    graduation_date=graduation_date,
                    reg_number=regno,
                )

            for employer_name, company_name, company_email, company_phone, position_held, date_from, date_to, experience in zip(
                    employer_names, company_names, company_emails, company_phones, position_helds, date_froms, date_tos,
                    experiences):
                Experience.objects.create(
                    customer=new_user,
                    employer_name=employer_name,
                    company_name=company_name,
                    comapny_email=company_email,
                    company_phone=company_phone,
                    position_held=position_held,
                    date_from=date_from,
                    date_to=date_to,
                    experience=experience,
                )

            new_userrr = authenticate(username=username, password=password1)
            print(new_user)
            login(request, new_userrr)
            sweetify.success(request, 'You did it',
                             text='Good job! You successfully Registered, Make Payment to Continue',
                             persistent='Continue')
            data = {
                'results': 'success',
                'success': 'Good job! You successfully Registered, just login'
            }
            return JsonResponse(data, safe=False)

        else:
            print(form.errors)

            #
            data = {
                'results': 'error',
                'form': form.errors.as_json(),
            }
            return JsonResponse(data)

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path1 = os.path.join(module_dir, 'Bachelorcourses')
    file_path2 = os.path.join(module_dir, 'course_certificate')
    file_path3 = os.path.join(module_dir, 'DiplomaCourses')
    file_path4 = os.path.join(module_dir, 'phdcourses')
    file_path5 = os.path.join(module_dir, 'Masterscourses')
    file_path6 = os.path.join(module_dir, 'university')
    # file_path6 = os.path.join(module_dir, 'categories')
    qbfile = open(file_path1, "r")
    qbfile2 = open(file_path2, "r")
    qbfile3 = open(file_path3, "r")
    qbfile4 = open(file_path4, "r")
    qbfile5 = open(file_path5, "r")
    qbfile6 = open(file_path6, "r")

    context = {
        'title': 'Create an account',
        'bachelors': qbfile.readlines(),
        'certificates': qbfile2.readlines(),
        'diplomas': qbfile3.readlines(),
        'phds': qbfile4.readlines(),
        'masters': qbfile5.readlines(),
        'unis': qbfile6.readlines(),
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'normal/signup/signup.html', context)


# def company_signupform_handling(request):
#
#
#     return redirect('LML:companysignup' )
# return redirect('LML:companysignup')
# if ('Phd' in qualifications) and ('Masters' in qualifications) and ('Degree' in qualifications) and (
#         'Certificate' in qualifications) and ('Degree' in qualifications) and ('Diploma' in qualifications):
#     status = 'ULTIMATE'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )
# elif ('Diploma' in qualifications):
#     status = 'BASIC'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )
# elif ('Degree' in qualifications) and ('Diploma' in qualifications):
#     status = 'BASIC'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )
#
# elif ('Masters' in qualifications) and ('Degree' in qualifications):
#     status = 'PREMIUM'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )
# elif ('Certificate' in qualifications) and ('Degree' in qualifications) and ('Diploma' in qualifications):
#     status = 'BASIC'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )
#
# else:
#     status = 'BASIC'
#     Customer.objects.filter(user_ptr_id=new_user.id).update(
#         rank_status=status,
#     )

@login_required()
def update_employers_profile(request):
    user = request.user.id

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        facebook = request.POST.get('facebook')
        googlr_plus = request.POST.get('googlr_plus')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        linkedin = request.POST.get('linkedin')
        company = Company.objects.filter(id=request.user.id).first()
        form = CompanyUserupdateForm(request.POST, request.FILES, instance=company)
        print(form)
        if form.is_valid():
            updated = form.save()
            CompanySocialAccount.objects.filter(company=company.id).update(
                company=updated,
                facebook=facebook,
                googlr_plus=googlr_plus,
                twitter=twitter,
                instagram=instagram,
                linkedin=linkedin,
            )
            User.objects.filter(pk=request.user.id).update(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )
            sweetify.success(request, 'Success', text='Good job! You successfully Updated Your Account',
                             persistent='Ok')
            return redirect('LML:employersprofile')
        else:

            sweetify.error(request, 'Error', text='Error updating your account', persistent='Retry')
            return redirect('LML:employersprofile')
            # return redirect('LML:companysignup',{'form':formr})
    else:
        return redirect('LML:employersprofile')


def login_user(request, source):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        def usernamel(email):
            uz = User.objects.filter(email__exact=email).first()
            # us = User.objects.filter(email=uz.email).values('username').first()
            print(uz.email)
            print(uz.username)

            if uz.email:
                return uz.username
            return None

        if User.objects.filter(username__exact=username).first() or User.objects.filter(email__exact=username).first():
            if User.objects.filter(username__exact=username).first():

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active and user.is_superuser:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue',
                                         timer=1500)
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue', timer=1500)

                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            rankCandidateStatus(request)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue', timer=1500)
                            return redirect('LML:employeedetails')
                else:
                    sweetify.error(request, 'Error', text='Invalid Username and Password', persistent='Retry')
                    source = source.replace('____', '/')
                    return redirect(source)
                    # return render(request, 'normal/login/login.html', {'username': username, })

            if User.objects.filter(email__exact=username).first():

                user = authenticate(request, username=usernamel(username), password=password)
                if user is not None:
                    if user.is_active and user.is_superuser:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue',
                                         timer=1500)
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue', timer=1500)
                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            rankCandidateStatus(request)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue', timer=1500)
                            return redirect('LML:employeedetails')
                else:
                    sweetify.error(request, 'Error', text='Invalid Email and Password', persistent='Retry')
                    source = source.replace('____', '/')
                    return redirect(source)
                    # return render(request, 'normal/login/login.html', {'username': username, })
        else:
            sweetify.error(request, 'Error', text='Invalid Credentials dont exist', persistent='Retry')
            source = source.replace('____', '/')
            return redirect(source)
    source = source.replace('____', '/')
    return render(request, source)


def signin(request):
    return render(request, 'normal/login/loginstyled.html')


def log_out_user(request):
    logout(request)
    return redirect('LML:home')

@login_required()
def employer_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            sweetify.success(request, title='Success', text='Successfully Password Changed.', persistent='Continue')
            return redirect("LML:employersprofile")
        else:
            form = PasswordChangeForm(request.user)
            sweetify.error(request, 'Error',
                           text='Password not Changed \n 1).Password did not match \n 2) Wrong Current Password' + str(
                               form.errors), persistent='Retry')
            return redirect("LML:employersprofile")
    else:
        form = PasswordChangeForm(request.user)
        return redirect("LML:employersprofile")


@login_required()
@has_user_paid_registration
def employerdetails(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    similar_company = Company.objects.filter(category=company.category)
    context = {
        'company': company,
        'social': social,
        'scompany': similar_company,
        'title': company.company_name + ' details'
    }
    return render(request, 'normal/jobdetails/employerdetails.html', context)


@login_required()
@has_user_paid_registration
def employersprofile(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    # similar_company = Company.objects.filter(category=company.category).exclude(id=user.id)
    categories = Category.objects.all()

    context = {
        'title': company.company_name + ' profile',
        'user': request.user,
        'company': company,
        'social': social,
        # 'scompany':similar_company,
        'categories': categories,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
    }
    return render(request, 'normal/account/employer-profile.html', context)


@login_required()
@has_user_paid_registration
def employeeprofile(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    socials = Social_account.objects.filter(customer=customer)
    userr = User.objects.filter(id=user).first()

    emShortlist = CompanyShortlistCustomers.objects.filter(customer=customer).count()
    unreadMessages = Message.objects.filter(reciever=userr, readstatus='UNREAD').count()
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path1 = os.path.join(module_dir, 'Bachelorcourses')
    file_path2 = os.path.join(module_dir, 'course_certificate')
    file_path3 = os.path.join(module_dir, 'DiplomaCourses')
    file_path4 = os.path.join(module_dir, 'phdcourses')
    file_path5 = os.path.join(module_dir, 'Masterscourses')
    file_path6 = os.path.join(module_dir, 'university')
    # file_path6 = os.path.join(module_dir, 'categories')
    qbfile = open(file_path1, "r")
    qbfile2 = open(file_path2, "r")
    qbfile3 = open(file_path3, "r")
    qbfile4 = open(file_path4, "r")
    qbfile5 = open(file_path5, "r")
    qbfile6 = open(file_path6, "r")
    context = {
        'shortlist_count': emShortlist,
        'title': 'Your Profile',
        'customer': customer,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'socials': socials,
        'bachelors': qbfile.readlines(),
        'certificates': qbfile2.readlines(),
        'diplomas': qbfile3.readlines(),
        'phds': qbfile4.readlines(),
        'masters': qbfile5.readlines(),
        'unis': qbfile6.readlines(),
        'unreadMessages': unreadMessages,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
    }

    return render(request, 'normal/account/candidate-profile.html', context)

@login_required()
@has_user_paid_registration
def employee_personal_details_update(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    account_urls = request.POST.getlist('account_url')
    account_ids = request.POST.getlist('account_id')

    if request.method == 'POST':
        form = PersonelUpdateForm(request.POST, request.FILES, instance=customer)
        print(form.errors)
        if form.is_valid():
            form.save()
            for account_url, account_id in zip(account_urls, account_ids):
                Social_account.objects.filter(customer=customer, id=int(account_id)).update(
                    account_url=account_url,
                )
            sweetify.success(request, title='Success', text='Personal Account Updated Successfully.',
                             persistent='Continue')
            return redirect('LML:employeeprofile')
        else:
            sweetify.error(request, 'Error', text='Details Not Updated', persistent='Retry')
            return redirect('LML:employeeprofile')
    return redirect('LML:employeeprofile')

@login_required()
@has_user_paid_registration
def employee_skills_update(request):
    if request.method == 'POST' and request.is_ajax():
        skill_id = request.POST['skill_id']
        skill = Skills.objects.filter(id=int(skill_id)).first()
        print(skill)
        if skill:
            skill.delete()
            data = {
                'results': 'success',
                'success': 'Skill deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'errortxt': 'Error Deleting Your Skill'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

@login_required()
@has_user_paid_registration
def employee_skills_detail_update(request):
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    if request.method == 'POST':
        skills = request.POST.getlist('skill')
        skill_ids = request.POST.getlist('skill_id')
        referees = request.POST.getlist('referee')
        referee_phonenumbers = request.POST.getlist('referee_phonenumber')

        # form =  SkillsForm(request.POST, instance=customer)

        for skill, referee, referee_phonenumber, skill_id in zip(skills, referees, referee_phonenumbers, skill_ids):
            Skills.objects.filter(id=int(skill_id)).update(
                customer_id=customer.id,
                skill=skill,
                referee=referee,
                referee_phonenumber=referee_phonenumber
            )
        sweetify.success(request, title='Success', text='Skills Updated Successfully.', persistent='Continue')
        return redirect('LML:employeeprofile')
    else:
        sweetify.error(request, 'Error', text='Skills Not Updated', persistent='Retry')
        return redirect('LML:employeeprofile')

@login_required()
@has_user_paid_registration
def employee_experience_detail_update(request):
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    exp_ids = request.POST.getlist('experience_id')
    employer_names = request.POST.getlist('employer_name')
    company_names = request.POST.getlist('company_name')
    company_emails = request.POST.getlist('comapny_email')
    company_phones = request.POST.getlist('company_phone')
    position_helds = request.POST.getlist('position_held')
    date_froms = request.POST.getlist('date_from')
    date_tos = request.POST.getlist('date_to')
    experiences = request.POST.getlist('experience')
    if request.method == 'POST':
        # print(employer_names,company_names,company_emails,company_phones,position_helds,date_froms,date_tos,experiences, exp_ids)
        for employer_name, company_name, company_email, company_phone, position_held, date_from, date_to, experience, exp_id in \
                zip(employer_names, company_names, company_emails, company_phones, position_helds, date_froms, date_tos,
                    experiences, exp_ids):
            # print(exp_ids, employer_name)
            if Experience.objects.filter(id=int(exp_id)).exists() or exp_id is not None:
                Experience.objects.filter(id=int(exp_id)).update(
                    customer_id=customer.id,
                    employer_name=employer_name,
                    company_name=company_name,
                    comapny_email=company_email,
                    company_phone=company_phone,
                    position_held=position_held,
                    date_from=date_from,
                    date_to=date_to,
                    experience=experience,
                )
            else:
                Experience.objects.create(
                    customer_id=customer.id,
                    employer_name=employer_name,
                    company_name=company_name,
                    comapny_email=company_email,
                    company_phone=company_phone,
                    position_held=position_held,
                    date_from=date_from,
                    date_to=date_to,
                    experience=experience,
                )

        sweetify.success(request, title='Success', text='Experiences Updated Successfully.', persistent='Continue')
        rankCandidateStatus(request)
        return redirect('LML:employeeprofile')
    else:
        sweetify.error(request, 'Error', text='Experiences Not Updated', persistent='Retry')
        return redirect('LML:employeeprofile')

@login_required()
@has_user_paid_registration
def employee_experience_detail_delete(request):
    if request.method == 'POST' and request.is_ajax():
        experience_id = request.POST['experience_id']
        experience = Experience.objects.filter(id=int(experience_id)).first()
        print(experience)
        if experience:
            experience.delete()
            rankCandidateStatus(request)
            data = {
                'results': 'success',
                'success': 'Experience deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'errortxt': 'Error Deleting Your Experience'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

@login_required()
@has_user_paid_registration
def employee_education_detail_delete(request):
    if request.method == 'POST' and request.is_ajax():
        education_id = request.POST['education_id']
        education = Education.objects.filter(id=int(education_id)).first()
        print(education)
        if education:
            education.delete()
            data = {
                'results': 'success',
                'success': 'Education deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'errortxt': 'Error Deleting Your Education'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

@login_required()
@has_user_paid_registration
def employeedetails(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    socials = Social_account.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'socials': socials,
        'title': "Account Details"
    }
    return render(request, 'normal/account/candidate-detail.html', context)


def companysignup(request):
    facebook = request.POST.get('facebook')
    googlr_plus = request.POST.get('googlr_plus')
    twitter = request.POST.get('twitter')
    instagram = request.POST.get('instagram')
    linkedin = request.POST.get('linkedin')
    password1 = request.POST.get('password1')
    username = request.POST.get('username')

    if request.method == 'POST' and request.is_ajax():
        # form = CompanyUserSignUpForm(request.POST)
        form = CompanyRegisterForm(request.POST, request.FILES)
        form2 = CompanySocialsForm(request.POST)

        def genCoRegNo(regnopers):
            if CompanyRegNo.objects.filter(company_reg_no__exact=regnopers):
                regnoperss = ('CMP' + get_random_string(length=8, allowed_chars='ABDEFGHIJKLNPQRSTUVWXYZ123456789'))
                genCoRegNo(regnoperss)
            else:
                return regnopers

        if form.is_valid():
            new_user = form.save()
            CompanySocialAccount.objects.create(
                company=new_user,
                facebook=facebook,
                googlr_plus=googlr_plus,
                twitter=twitter,
                instagram=instagram,
                linkedin=linkedin,
            )
            CompanyRegNo.objects.create(
                company=new_user,
                company_reg_no=genCoRegNo(
                    'CMP' + get_random_string(length=8, allowed_chars='ABDEFGHIJKLNPQRSTUVWXYZ123456789')),
            )
            # sweetify.success(request, 'You did it', text='Good job! You successfully registered', persistent='Ok')
            new_userrr = authenticate(username=username, password=password1)
            print(new_user)
            login(request, new_userrr)
            data = {
                'results': 'success',
                'success': 'Good job! You successfully Registered, just login'
            }
            return JsonResponse(data, safe=False)

        else:

            # print(formr.errors)
            # sweetify.error(request, 'Error', text='Ensure you fill all fields correctly', persistent='Retry')
            context3 = {
                'results': 'error',
                'form': form.errors.as_json()

            }
            # return JsonResponse(context3, safe=False)
            # return render_to_response('normal/signup/errors.html', context)
            return JsonResponse(context3)



    else:

        form = CompanyRegisterForm()
        form2 = CompanySocialsForm()

    context = {
        'title': 'Create an account',
        'counties': County.objects.all().order_by('county'),
        'regions': Region.objects.all().order_by('county_number'),
        'categories': Category.objects.all().order_by('category'),
        'form': form,
        'social': form2,

    }

    return render(request, 'normal/signup/create-company.html', context)

@login_required()
@has_user_paid_registration
def advancesearch(request):
    # customers = Customer.objects.order_by('?')
    from datetime import datetime
    todayy = datetime.today()
    yr = todayy.year
    if request.method == 'POST':
        cat = request.POST.get('category')
        cou = request.POST.get('county')
        reg = request.POST.get('region')
        # exp = request.POST.get('experience')
        # qual = request.POST.get('qualification')
        # jt = request.POST.get('job_type')

        category = Category.objects.filter(id=cat).first()
        county = County.objects.filter(id=cou).first()
        region = Region.objects.filter(id=reg).first()

        customers = Customer.objects.filter(category=category, county=county, region=region)
        print(customers)
    else:
        customers = Customer.objects.order_by('?')
    context = {
        'title': "Advance search",
        'categories': Category.objects.all(),
        "customers": customers,
        'counties': County.objects.all(),
        "regions": Region.objects.all(),
    }
    return render(request, 'normal/advancedsearch/advancedsearch.html', context)


def companypricing(request):
    comp = Company.objects.filter(user_ptr_id=request.user.id).first()
    cpp = CompanyStatusPayment.objects.filter(company=comp).order_by('-created_at').first()

    context = {
        'title': 'Company Pricing',
        'monthpricing': CompanyPricingPlan.objects.filter(status='MONTHLY').order_by('price'),
        'yearpricing': CompanyPricingPlan.objects.filter(status='YEARLY').order_by('price'),
        'paid_pac':cpp,
    }
    return render(request, 'normal/companypricing/companypricing.html', context)


def contactus(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'normal/contact/contact.html', context)


def signup_initial(request):
    context = {
        'title': "Signup",
    }
    return render(request, 'normal/signup/signupdecision.html', context)


def termsandconditons(request):
    context = {
        'title': 'Terms and Conditions',
    }
    return render(request, 'normal/termsandconditions/terms.html', context)


def frequentaskedquestions(request):
    context = {
        'title': 'FAQ',
    }
    return render(request, 'normal/faq/faq.html', context)


def signup_employee_initial(request):
    context = {
        'title': 'Employee Signup',
    }
    return render(request, 'normal/signup/employeesignupdecision.html', context)


def signup_company_initial(request):
    context = {
        'title': 'Company Signup',
    }
    return render(request, 'normal/signup/companysignupdecision.html', context)


def company_contact_us(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method == 'POST':
        ContactUsCompany.objects.create(
            name=name,
            company=company,
            email=email,
            message=message,
        )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        return redirect('LML:employerdetails')
    else:
        sweetify.success(request, 'Error', text='Message not sent', persistent='Ok')
    return redirect('LML:employerdetails')


def customer_contact_us(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method == 'POST':
        ContactUsEmployee.objects.create(
            name=name,
            customer=customer,
            email=email,
            message=message,
        )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        return redirect('LML:employeedetails')
    else:
        sweetify.success(request, 'Error', text='Message not sent', persistent='Ok')
    return redirect('LML:employeedetails')


def home_contact_us(request, source):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method == 'POST':
        ContactUsHome.objects.create(
            name=name,
            email=email,
            message=message,
        )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        source = source.replace('____', '/')
        return redirect(source)
    else:
        sweetify.success(request, 'Error', text='Message not sent', persistent='Ok')
        source = source.replace('____', '/')
    return redirect(source)


@csrf_exempt
def payment_done(request):
    # print(request.POST)
    context = {
        'post': request.POST
    }
    return render(request, 'normal/payment/employee/paymentdone.html', context)


@csrf_exempt
def payment_canceled(request):
    # print(request)
    return render(request, 'normal/payment/employee/paymentcanceled.html')

@csrf_exempt
def payment_company_status_done(request):
    # print(request.POST)
    context = {
        'post': request.POST
    }
    return render(request, 'normal/payment/company/status/paymentdone.html', context)


@csrf_exempt
def payment_company_status_canceled(request):
    # print(request)
    return render(request, 'normal/payment/company/status/paymentcanceled.html')


@login_required()
def payment(request):
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    if not CustomerPayments.objects.filter(payer_reg_no=customer.customer_reg_no).first():
        customer_reg = CustomerRegNo.objects.filter(customer=customer).first()
        pricing = CandidateRegPrice.objects.filter(status='ACTIVE').first()
        loadCurrency()
        context = {
            'regno': customer_reg,
            'customer': customer,
            'price': pricing,
            # 'form': form
        }
        return render(request, 'normal/payment/payment-method.html', context)
    else:
        context = {
            'was': 'was',

        }
        return render(request, 'normal/payment/employee/paymentdone.html', context)



def companypayment(request):
    company = Company.objects.filter(user_ptr_id=request.user.id).first()
    if not CompanyRegistrationPayment.objects.filter(payer_reg_no=company.companyregno).first():
        customer_reg = CompanyRegNo.objects.filter(company=company).first()
        pricing = CompanyRegPrice.objects.filter(status='ACTIVE').first()
        loadCurrency()
        context = {
            'regno': customer_reg,
            'company': company,
            'price': pricing,
        }
        return render(request, 'normal/payment/companympesapayment.html', context)
    else:
        context = {
            'was': 'was',
        }
        return render(request, 'normal/payment/company/paymentdone.html', context)



def companypaymentpackage(request, pricing_id):
    pricing = CompanyPricingPlan.objects.filter(id=pricing_id).first()

    context = {
        'pricing': pricing,
    }
    return render(request, 'normal/companypricing/subscribetoplan.html', context)


@login_required()
@has_user_paid_registration
def employer_dash(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company, payment_status='SHORTLISTED')
    company_reg_pay = CompanyRegistrationPayment.objects.filter(payer_reg_no=company.companyregno).order_by('-created_at').all()

    basic_customers = []
    for customer in Customer.objects.filter(rank_status='BASIC'):
        c_c1 = CompanyShortlistCustomers.objects.filter(company=company, customer=customer,
                                                        payment_status='SHORTLISTED')
        for ccc1 in c_c1:
            basic_customers.append(ccc1.customer)
    premium_customers = []
    for customer in Customer.objects.filter(rank_status='PREMIUM'):
        c_c2 = CompanyShortlistCustomers.objects.filter(company=company, customer=customer,
                                                        payment_status='SHORTLISTED')
        for ccc2 in c_c2:
            premium_customers.append(ccc2.customer)
    ultimate_customers = []
    for customer in Customer.objects.filter(rank_status='ULTIMATE'):
        c_c3 = CompanyShortlistCustomers.objects.filter(company=company, customer=customer,
                                                        payment_status='SHORTLISTED')
        for ccc3 in c_c3:
            ultimate_customers.append(ccc3.customer)

    print(len(basic_customers))

    context = {
        'company': company,
        'social': social,
        'customers': customers,
        'title': company.company_name + ' Dash',
        'premium_customers': premium_customers,
        # 'premium_customers': Customer.objects.all(),
        'basic_customers': basic_customers,
        'ultimate_customers': ultimate_customers,
        'company_reg_pay':company_reg_pay
        # 'ultimate_customers': Customer.objects.all(),
    }
    return render(request, 'normal/dashboard/employer-dash.html', context)


@login_required()
@has_user_paid_registration
def employee_dash(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    social = Social_account.objects.filter(customer=customer).first()
    # customers = CompanyShortlistCustomers.objects.filter(company=company)
    cust_reg_pay = CustomerPayments.objects.filter(payer_reg_no=customer.customer_reg_no).order_by('-created_at').all()
    custome_documents = CustomerCvFiles.objects.all()
    companies_list = []
    userr = User.objects.filter(id=user).first()
    companies = Message.objects.filter(reciever=userr)
    for company in companies:
        cmpn = Company.objects.filter(user_ptr_id=company.sender.id).first()
        companies_list.append(cmpn)
    msg_companies = list(set(companies_list))

    context = {
        'customer': customer,
        'social': social,
        'msg_comapanies': msg_companies,
        'cust_reg_pay': cust_reg_pay,
        'custome_documents':custome_documents,

    }
    return render(request, 'normal/dashboard/employee-dash.html', context)

@login_required()
@has_user_paid_registration
def premium_employee_details(request, customer_id):
    customer = Customer.objects.filter(user_ptr_id=customer_id).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    socials = Social_account.objects.filter(customer=customer)
    reviews = CustomerReviews.objects.filter(customer=customer).order_by('-created_at')
    all_customers = Customer.objects.filter(category_id=customer.category.id).exclude(id=customer.id)[:7]
    other_customers = Customer.objects.filter(category__category__contains=customer.category.category).exclude(
        id=customer.id)

    print(other_customers)
    context = {
        'title': customer.first_name.capitalize() + ' ' + customer.last_name.capitalize(),
        'customer': customer,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'socials': socials,
        'reviews': reviews,
        'all_customers': all_customers,
        'other_customers': other_customers,

    }

    return render(request, 'normal/allcandidates/premium-candidate-detail.html', context)

@login_required()
@has_user_paid_registration
def all_premium_employees(request):
    if request.method == 'POST':
        county = request.POST['county']
        region = request.POST['region']
        category = request.POST['category']
        cat = Category.objects.filter(id=int(category)).first()
        reg = Region.objects.filter(id=int(region)).first()
        count = County.objects.filter(id=int(county)).first()
        customers = Customer.objects.filter(category=cat, region=reg, county=count)
    else:
        customers = Customer.objects.order_by('?')

    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Premium Candidates'

    }
    return render(request, 'normal/allcandidates/premium-candidate.html', context)


def all_category_employees(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if category is not None:
        customers = Customer.objects.filter(category=category)
    else:
        customers = Customer.objects.order_by('?')

    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Premium Candidates'

    }
    return render(request, 'normal/allcandidates/premium-candidate.html', context)


def all_offer_employees(request, offer):
    category = Category.objects.filter(category__contains=offer).first()
    print(category)
    if category is not None:
        customers = Customer.objects.filter(category=category)
    else:
        customers = Customer.objects.order_by('?')

    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Premium Candidates'

    }
    return render(request, 'normal/allcandidates/premium-candidate.html', context)

@login_required()
@has_user_paid_registration
def shortlistcustomers(request):
    if request.method == 'POST':
        customer = request.POST.get('customer_id')
        company = request.POST.get('company_id')
        print(customer, company)
        customer_user = Customer.objects.filter(user_ptr_id=int(customer)).first()
        company_user = Company.objects.filter(user_ptr_id=int(company)).first()
        if not CompanyShortlistCustomers.objects.filter(customer=customer, company=company,
                                                        payment_status='SHORTLISTED').exists():
            CompanyShortlistCustomers.objects.create(
                customer=customer_user,
                company=company_user,
                payment_status="SHORTLISTED"
            )
            data = {
                'shortlisted': 'Successfully shortlisted',
            }
            if data['shortlisted']:
                data[
                    'success_message'] = 'Successfully Shortlisted ' + customer_user.first_name.upper() + ' ' + customer_user.last_name.upper() + '.'

        else:
            data = {
                'is_shortlisted': 'You have already shortlisted this user',
            }
            if data['is_shortlisted']:
                data['error_message'] = 'You have already shortlisted this user'

        return JsonResponse(data)


def unshortlistcustomers(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        company_id = request.POST.get('company_id')
        print(company_id, customer_id)
        if CompanyShortlistCustomers.objects.filter(customer_id=customer_id, company_id=company_id).exists():
            relation = CompanyShortlistCustomers.objects.filter(customer_id=customer_id, company_id=company_id).first()
            customer = relation.customer.first_name + ' ' + relation.customer.last_name
            CompanyShortlistCustomers.objects.filter(customer_id=customer_id, company_id=company_id).update(
                payment_status='UNSHORTLISTED'
            )
            # relation.delete()
            data = {
                'shortlisted': customer.upper() + 'Unshortlisted Successfully',
            }
            if data['shortlisted']:
                data['success_message'] = customer.upper() + ' Unshortlisted Successfully'

        else:

            data = {
                'is_shortlisted': 'Error Deleting',
            }
            if data['is_shortlisted']:
                data['error_message'] = 'Error Deleting'

        return JsonResponse(data)

@login_required()
@has_user_paid_registration
def all_employees(request):
    if request.method == 'POST':
        county = request.POST.get('county')
        region = request.POST.get('region')
        category = request.POST.get('category')

        if (category is not None) and (region is not None) and (county is not None):
            cat = Category.objects.filter(id=int(category)).first()
            reg = Region.objects.filter(id=int(region)).first()
            count = County.objects.filter(id=int(county)).first()
            customers = Customer.objects.filter(Q(category_id=cat.id), Q(region_id=reg.id), Q(county_id=count.id))
        elif (category is not None):
            cat = Category.objects.filter(id=int(category)).first()

            customers = Customer.objects.filter(Q(category_id=cat.id))
        elif (region is not None):
            reg = Region.objects.filter(id=int(region)).first()
            customers = Customer.objects.filter(Q(region_id=reg.id))
        elif (county is not None):
            count = County.objects.filter(id=int(county)).first()
            customers = Customer.objects.filter(Q(county_id=count.id))
        else:
            customers = Customer.objects.order_by('?')
    else:
        customers = Customer.objects.order_by('?')

    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'title': 'All Candidates',

    }
    return render(request, 'normal/allcandidates/all-candidates.html', context)


def categories(request):
    if request.method == 'POST':
        category = request.POST['category']
        categories = Category.objects.filter(id=category)
    else:
        categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'normal/categories/category.html', context)


def dumb(request):
    if request.method == 'POST':
        file = request.FILES.get('fileupload')
        print(file)
        context = {

        }
        return JsonResponse(context)
    context = {

    }
    return render(request, 'normal/signup/dumb.html', context)


@login_required()
def EmployerCustomerShortlist(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    print(company)
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
            CompanyShortlistCustomers.objects.filter(company_id=company.id, created_at__month=months_choice).count())
    defaultData2 = month_data
    context2 = {
        'labels2': labels2,
        'defaultData2': defaultData2,

    }

    return JsonResponse(context2)

@login_required()
@has_user_paid_registration
def EmployerCustomerShortlistTemplate(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company)
    context = {
        'title': 'Employee Shortlist Graph',
        'company': company,
        'social': social,
        'customers': customers,
    }

    return render(request, 'normal/dashboard/shortlistgraph.html', context)

@login_required()
@has_user_paid_registration
def review_shortlisted_customer(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        ratings = request.POST.get('ratings')
        customer = request.POST.get('customer')
        comp = Company.objects.filter(user_ptr_id=request.user.id).first()
        cusr = Customer.objects.filter(id=customer).first()
        # form = CustomerReviewsForm(request.POST)
        if comp is not None:
            CustomerReviews.objects.create(
                message=message,
                ratings=ratings,
                customer=cusr,
                company=comp,

            )
            sweetify.success(request, 'Success', text='Candidate Rated Successfully', persistent='Ok')
            return redirect('LML:employer_dash')
        else:
            sweetify.error(request, 'Error', text='Candidate Not Rated', persistent='Ok')
        return redirect('LML:employer_dash')

    return redirect('LML:employer_dash')


@login_required()
def generate_PDF(request, customer_id):
    employee = Customer.objects.filter(user_ptr_id=int(customer_id)).first()
    experiences = Experience.objects.filter(customer=employee)
    educations = Education.objects.filter(customer=employee)
    skills = Skills.objects.filter(customer=employee)
    social = Social_account.objects.filter(customer=employee).first()
    download = request.GET.get("download")

    filename = "Invoice_%s.pdf" % ("12341231")
    if download:
        content = "attachment; filename='%s'" % (filename)

    context = {
        'employee': employee,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'social': social,
    }
    return render(request, 'normal/Pdf_resume/employee_resume.html', context)


@login_required()
def employee_education_detail_update(request):
    education_ids = request.POST.getlist('education_id')
    schools = request.POST.getlist('school')
    courses = request.POST.getlist('course')
    graduation_dates = request.POST.getlist('graduation_date')
    regnos = request.POST.getlist('reg_number')
    print(education_ids, schools, courses, graduation_dates, regnos)

    if request.method == 'POST':
        customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
        if customer:

            for education_id, school, course, graduation_date, regno in zip(education_ids, schools, courses,
                                                                            graduation_dates, regnos):
                print(education_id, school, course, graduation_date, regno)
                edu = Education.objects.filter(id=int(education_id)).first()
                Education.objects.filter(id=edu.id).update(
                    school=school,
                    course=course,
                    graduation_date=graduation_date,
                    reg_number=regno,
                    customer=customer,
                )
            sweetify.success(request, title='Success', text='Education Updated Successfully.', persistent='Continue')
            rankCandidateStatus(request)
            return redirect('LML:employeeprofile')
        else:
            sweetify.error(request, 'Error', text='User Does Not Exist', persistent='Retry')
    else:
        sweetify.error(request, 'Error', text='Education Not Updated', persistent='Retry')
        return redirect('LML:employeeprofile')


@login_required()
def update_add_skill(request):
    if request.method == 'POST':
        skill = request.POST.get('skill')
        customer = request.POST.get('customer')
        referee = request.POST.get('referee')
        referee_phonenumber = request.POST.get('referee_phonenumber')
        new_user = Customer.objects.filter(user_ptr_id=customer).first()
        if new_user:
            if not Skills.objects.filter(customer=customer, skill__exact=skill):
                Skills.objects.create(
                    customer=new_user,
                    skill=skill,
                    referee=referee,
                    referee_phonenumber=referee_phonenumber
                )
                sweetify.success(request, 'Success', text='Successfully Added New Skill', persistent='Ok')
            else:
                sweetify.error(request, 'Error', text=str(skill) + ' Skill Exists', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Adding New Skill', persistent='Ok')
    return redirect('LML:employeeprofile')

@login_required()
def update_add_experience(request):
    if request.method == 'POST':
        employer_name = request.POST.get('employer_name')
        customer = request.POST.get('customer')
        company_namee = request.POST.get('company_name')
        company_email = request.POST.get('company_email')
        company_phone = request.POST.get('company_phone')
        position_held = request.POST.get('position_held')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        experience = request.POST.get('experience')
        new_user = Customer.objects.filter(user_ptr_id=customer).first()
        if new_user:
            Experience.objects.create(
                customer=new_user,
                employer_name=employer_name,
                company_name=company_namee,
                comapny_email=company_email,
                company_phone=company_phone,
                position_held=position_held,
                date_from=date_from,
                date_to=date_to,
                experience=experience,
            )
            sweetify.success(request, 'Success', text='Successfully Added New Experience', persistent='Ok')
            rankCandidateStatus(request)
        else:
            sweetify.error(request, 'Error', text='Error Adding New Experience', persistent='Ok')
    return redirect('LML:employeeprofile')

@login_required()
def update_add_education(request):
    if request.method == 'POST':
        qualification = request.POST.get('qualifications')
        school = request.POST.get('school')
        course = request.POST.get('course')
        graduation_date = request.POST.get('graduation_date')
        regno = request.POST.get('reg_number')
        customer = request.POST.get('customer')
        new_user = Customer.objects.filter(user_ptr_id=customer).first()
        if new_user:
            Education.objects.create(
                customer=new_user,
                qualifications=qualification,
                school=school,
                course=course,
                graduation_date=graduation_date,
                reg_number=regno,
            )
            sweetify.success(request, 'Success', text='Successfully Added New Education', persistent='Ok')
            rankCandidateStatus(request)
        else:
            sweetify.error(request, 'Error', text='Error Adding New Education', persistent='Ok')
    return redirect('LML:employeeprofile')

@login_required()
def update_add_social(request):
    if request.method == 'POST':
        account_url = request.POST['account_url']
        customer = request.POST.get('customer')
        new_user = Customer.objects.filter(user_ptr_id=customer).first()
        if new_user:
            Social_account.objects.create(
                customer=new_user,
                account_url=account_url
            )
            sweetify.success(request, 'Success', text='Successfully Added New Social', persistent='Ok')
        else:
            sweetify.error(request, 'Error', text='Error Adding New Social', persistent='Ok')
    return redirect('LML:employeeprofile')

@login_required()
def deletesocial(request):
    if request.method == 'POST' and request.is_ajax():
        social_id = request.POST['social_id']
        social = Social_account.objects.filter(id=int(social_id)).first()
        print(social)
        if social:
            # social.delete()
            data = {
                'results': 'success',
                'success': 'Social deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'errortxt': 'Error Deleting Your Social'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

@login_required()
def employee_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            sweetify.success(request, title='Success', text='Successfuly Password Changed.', persistent='Continue')
            return redirect("LML:employeeprofile")
        else:
            form = PasswordChangeForm(request.user)
            print(form.error_messages)
            sweetify.error(request, 'Error',
                           text='Password not Changed \n 1).Password did not match \n 2) Wrong Current Password' + str(
                               form.errors), persistent='Retry')
            return redirect("LML:employeeprofile")
    else:
        form = PasswordChangeForm(request.user)
        return redirect("LML:employeeprofile")


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


@csrf_exempt
def checkifemailexists(request):
    if request.method == 'POST' and request.is_ajax():
        test = request.POST.get('testvalue')

        if User.objects.filter(email__iexact=test) and test is not None:
            if validateEmail(test):
                context = {
                    'results': 'error',
                    'answer': "Email Already Exists !!!",
                }
            else:
                context = {
                    'results': 'error',
                    'answer': "Wrong email syntax",
                }
        else:
            if validateEmail(test):
                context = {
                    'results': 'success',
                    'answer': "Email Is Clean For Use!",
                }
            else:
                context = {
                    'results': 'error',
                    'answer': "Wrong email syntax",
                }
        return JsonResponse(context, safe=True)


@csrf_exempt
def checkifusernameexists(request):
    if request.method == 'POST' and request.is_ajax():
        test = request.POST.get('testvalue2')
        if User.objects.filter(username__exact=test) and test is not None:
            context = {
                'results': 'error',
                'answer': "Username Already Exists !!!",
            }
        else:
            context = {
                'results': 'success',
                'answer': "Username Is Clean For Use!",
            }
        return JsonResponse(context, safe=True)


def rankCandidateStatus(request):
    # ('BASIC', 'Basic'),
    # ('PREMIUM', 'Premium'),
    # ('ULTIMATE', 'Ultimate'),
    from datetime import datetime
    logedinuser = request.user
    candidate = Customer.objects.filter(user_ptr_id=logedinuser.id).first()
    exp_dates = []
    educations = []

    for experience in Experience.objects.filter(customer=candidate):
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(experience.date_from), date_format)
        b = datetime.strptime(str(experience.date_to), date_format)
        delta = b - a
        exp_dates.append(delta.days)

    for education in Education.objects.filter(customer=candidate):
        educations.append(education.qualifications)
    # print(exp_dates, educations)
    status = " "
    if ((('Certificate' in educations)) and ('Phd' not in educations) and ('Bachelor' not in educations) and (
            'Masters' not in educations) and ('Diploma' not in educations)):
        if (max(exp_dates) > 730):
            status = "ULTIMATE"
        elif (max(exp_dates) > 365):
            status = "PREMIUM"
        elif (max(exp_dates) < 365):
            status = "BASIC"
        else:
            status = "BASIC"

    elif ((('Certificate' in educations) or ('Diploma' in educations)) and ('Phd' not in educations) and (
            'Bachelor' not in educations) and ('Masters' not in educations)):
        if (max(exp_dates) > 730):
            status = "ULTIMATE"
        elif (max(exp_dates) > 365):
            status = "PREMIUM"
        elif (max(exp_dates) < 365):
            status = "BASIC"
        else:
            status = "BASIC"
    elif ((('Certificate' in educations) or ('Diploma' in educations) or ('Bachelor' in educations)) and (
            'Phd' not in educations) and ('Masters' not in educations)):
        if (max(exp_dates) > 730):
            status = "ULTIMATE"
        elif (max(exp_dates) > 365):
            status = "PREMIUM"
        elif (max(exp_dates) < 365):
            status = "BASIC"
        else:
            status = "BASIC"

    elif ((('Certificate' in educations) or ('Diploma' in educations) or ('Bachelor' in educations) or (
            'Masters' in educations)) and ('Phd' not in educations)):
        if (max(exp_dates) > 730):
            status = "ULTIMATE"
        elif (max(exp_dates) > 365):
            status = "PREMIUM"
        elif (max(exp_dates) < 365):
            status = "BASIC"
        else:
            status = "BASIC"

    elif ((('Certificate' in educations) or ('Diploma' in educations) or ('Bachelor' in educations) or (
            'Masters' in educations) or ('Phd' in educations))):
        if (max(exp_dates) > 730):
            status = "ULTIMATE"
        elif (max(exp_dates) > 365):
            status = "PREMIUM"
        elif (max(exp_dates) < 365):
            status = "BASIC"
        else:
            status = "BASIC"
    print(status, candidate.id)
    Customer.objects.filter(id=candidate.id).update(
        rank_status=status.upper()
    )


def registrationpaydetails(request):
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    customer_reg = CustomerRegNo.objects.filter(customer=customer).first()
    crp = CandidateRegPrice.objects.filter(status='ACTIVE').first()
    curre = CurrencyValue.objects.first()

    paypal_dict = {
        # 'business': settings.PAYPAL_RECEIVER_EMAIL,
        'reg_amount': crp.price,
        'user_name': customer.username,
        'user_id': customer.id,
        # 'invoice': str(customer.customer_reg_no),
        'reg_no': customer_reg.personel_reg_no,
        'currency': curre.currency,

    }
    return JsonResponse(paypal_dict)


def payment_complete(request):
    body = json.loads(request.body)
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    cust_reg_ammount = CandidateRegPrice.objects.filter(status='ACTIVE').first()
    curr = CurrencyValue.objects.first()

    pay_method = "PAYPAL"
    payer_reg_no = customer.customer_reg_no
    payer_paying_email = body['payer']['email_address']
    business_email_paid = body['purchase_units'][0]['payee']['email_address']
    country_code = body['payer']['address']['country_code']
    payer_name = body['payer']['name']['given_name'] + ' ' + body['payer']['name']['surname']
    amount = cust_reg_ammount.price
    currency_amount = body['purchase_units'][0]['amount']['value']
    currency_code = body['purchase_units'][0]['amount']['currency_code']
    currency_value = curr.currency
    pay_recipt_no = body['purchase_units'][0]['payments']['captures'][0]['id']
    transaction_recipt_no = body['id']
    transaction_status = body['status']

    if transaction_status == 'COMPLETED':
        payment_status = 'COMPLETED'
    elif transaction_status == 'REVERSED':
        payment_status = 'CANCELED'

    # print(payer_reg_no, payer_paying_email, business_email_paid, country_code, payer_name, amount, currency_amount, currency_code,
    #       currency_value,pay_recipt_no, transaction_recipt_no,transaction_status)
    if transaction_status == 'COMPLETED':
        cp = CustomerPayments.objects.create(
            pay_method=pay_method,
            payer_reg_no=payer_reg_no,
            payer_full_name=payer_name,
            payer_paying_email=payer_paying_email,
            business_email_paid=business_email_paid,
            country_code=country_code,
            amount=amount,
            currency_amount=currency_amount,
            currency_code=currency_code,
            currency_value=currency_value,
            pay_recipt_no=pay_recipt_no,
            transaction_recipt_no=transaction_recipt_no,
            transaction_status=transaction_status,
            payment_status=payment_status,

        )
        if cp:
            Customer.objects.filter(user_ptr_id=request.user.id).update(
                regpayment=cp,
            )
            context={
                'status':'success',
                'payment':'done',
            }
            return JsonResponse(context)
    elif transaction_status == 'REVERSED':
        context = {
            'status': 'error',
            'payment': 'reversed',
        }
        return JsonResponse(context)


def companyregistrationpaydetails(request):
    company = Company.objects.filter(user_ptr_id=request.user.id).first()
    # company_reg = CompanyRegNo.objects.filter(company=company).first()
    crp = CompanyRegPrice.objects.filter(status='ACTIVE').first()
    curre = CurrencyValue.objects.first()

    paypal_dict = {
        'reg_amount': crp.price,
        'currency': curre.currency,

    }
    return JsonResponse(paypal_dict)


def comapny_payment_complete(request):
    body = json.loads(request.body)
    company= Company.objects.filter(user_ptr_id=request.user.id).first()
    company_reg_ammount = CompanyRegPrice.objects.filter(status='ACTIVE').first()
    curr = CurrencyValue.objects.first()

    pay_method = "PAYPAL"
    payer_reg_no = company.companyregno
    payer_paying_email = body['payer']['email_address']
    business_email_paid = body['purchase_units'][0]['payee']['email_address']
    country_code = body['payer']['address']['country_code']
    payer_name = body['payer']['name']['given_name'] + ' ' + body['payer']['name']['surname']
    amount = company_reg_ammount.price
    currency_amount = body['purchase_units'][0]['amount']['value']
    currency_code = body['purchase_units'][0]['amount']['currency_code']
    currency_value = curr.currency
    pay_recipt_no = body['purchase_units'][0]['payments']['captures'][0]['id']
    transaction_recipt_no = body['id']
    transaction_status = body['status']

    if transaction_status == 'COMPLETED':
        payment_status = 'COMPLETED'
    elif transaction_status == 'REVERSED':
        payment_status = 'CANCELED'

    # print(payer_reg_no, payer_paying_email, business_email_paid, country_code, payer_name, amount, currency_amount, currency_code,
    #       currency_value,pay_recipt_no, transaction_recipt_no,transaction_status)
    if transaction_status == 'COMPLETED':
        cp = CompanyRegistrationPayment.objects.create(
            pay_method=pay_method,
            payer_reg_no=payer_reg_no,
            payer_full_name=payer_name,
            payer_paying_email=payer_paying_email,
            business_email_paid=business_email_paid,
            country_code=country_code,
            amount=amount,
            currency_amount=currency_amount,
            currency_code=currency_code,
            currency_value=currency_value,
            pay_recipt_no=pay_recipt_no,
            transaction_recipt_no=transaction_recipt_no,
            transaction_status=transaction_status,
            payment_status=payment_status,
        )
        if cp:
            Company.objects.filter(user_ptr_id=request.user.id).update(
                regpayment=cp,
            )
            context = {
                'status': 'success',
                'payment': 'done',
            }
            return JsonResponse(context)
    elif transaction_status == 'REVERSED':
        context = {
            'status': 'error',
            'payment': 'reversed',
        }
        return JsonResponse(context)


def company_payment_done(request):
    print(request.POST)
    context = {
        'post': request.POST
    }
    return render(request, 'normal/payment/company/paymentdone.html', context)


def company_payment_canceled(request):
    print(request)
    return render(request, 'normal/payment/company/paymentcanceled.html')


def company_price_details(request, price_id):
    pricing = CompanyPricingPlan.objects.filter(id=price_id).first()
    cur = CurrencyValue.objects.all().first()
    context = {
        'currency': cur.currency,
        'reg_amount': pricing.price,
    }
    return JsonResponse(context)


def company_price_details_record(request, price_id):
    body = json.loads(request.body)
    company = Company.objects.filter(user_ptr_id=request.user.id).first()
    # company_reg_ammount = CompanyRegPrice.objects.filter(status='ACTIVE').first()
    pricing = CompanyPricingPlan.objects.filter(id=int(price_id)).first()
    curr = CurrencyValue.objects.first()
    title = pricing.title
    print(title)
    pay_method = "PAYPAL"
    payer_reg_no = company.companyregno
    payer_paying_email = body['payer']['email_address']
    business_email_paid = body['purchase_units'][0]['payee']['email_address']
    country_code = body['payer']['address']['country_code']
    payer_name = body['payer']['name']['given_name'] + ' ' + body['payer']['name']['surname']
    amount = pricing.price
    currency_amount = body['purchase_units'][0]['amount']['value']
    currency_code = body['purchase_units'][0]['amount']['currency_code']
    currency_value = curr.currency
    pay_recipt_no = body['purchase_units'][0]['payments']['captures'][0]['id']
    transaction_recipt_no = body['id']
    transaction_status = body['status']

    if transaction_status == 'COMPLETED':
        payment_status = 'COMPLETED'
    elif transaction_status == 'REVERSED':
        payment_status = 'CANCELED'

    if transaction_status == 'COMPLETED':
        cp = CompanyStatusPayment.objects.create(
            pay_method=pay_method,
            payer_reg_no=payer_reg_no,
            payer_full_name=payer_name,
            payer_paying_email=payer_paying_email,
            business_email_paid=business_email_paid,
            country_code=country_code,
            amount=amount,
            currency_amount=currency_amount,
            currency_code=currency_code,
            currency_value=currency_value,
            pay_recipt_no=pay_recipt_no,
            transaction_recipt_no=transaction_recipt_no,
            transaction_status=transaction_status,
            payment_status=payment_status,
            company=company,
            cpp=pricing,
        )
        if cp:
            Company.objects.filter(id=company.id).update(
                rank_status=title.upper()
            )
            context = {
                'status': 'success',
                'payment': 'done',
            }
            return JsonResponse(context)
    elif transaction_status == 'REVERSED':
        context = {
            'status': 'error',
            'payment': 'reversed',
        }
        return JsonResponse(context)


def candidate_files_upload(request):
    print(request.POST)
    candidate = Customer.objects.filter(user_ptr_id=request.user.id).first()
    con = request.POST.get('content-type')
    title = request.POST.get('title')
    details = request.POST.get('details')
    filee = request.FILES.get('filee')
    fileext = ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/pdf"]

    if con in fileext:
        if candidate is not None and con is not None and title is not None and details is not None and filee is not None:
            CustomerCvFiles.objects.create(
                customer=candidate,
                title=title,
                description=details,
                file=filee,
            )
            context={
                'success': 'success',
                'msg': 'File Uploaded'
            }
            return JsonResponse(context)
        else:
            context = {
                'error': 'error',
                'msg': 'Error uploading , missing inputs.'
            }
            return JsonResponse(context)
    else:
        context={
            'error':'error',
            'msg':'Wrong File Format'
        }
    return JsonResponse(context)