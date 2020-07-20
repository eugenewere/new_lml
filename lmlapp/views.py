
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response
import os
from datetime import datetime
import sweetify

from rest_framework import status


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
    context = {
        'customers':customers,
        'all_customers':all_customers,
        'title': 'home',
        'counties': County.objects.all(),
        'categories':Category.objects.all(),
        'regions':Region.objects.all(),
        'images': AdvertCarousel.objects.order_by('-created_at'),
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):

    if  request.is_ajax() and request.method=='POST' :
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
        referee_phonenumbers= request.POST.getlist('referee_phonenumber')

        account_url= request.POST['account_url']

        password1= request.POST['password1']
        username= request.POST['username']



        form = PersonelRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            new_user= form.save()
            CustomerRegNo.objects.create(
                customer=new_user,
                personel_reg_no=('PERS' + get_random_string(length=5, allowed_chars='ABCDFGHIJKLMNPQRSTUVWXYZ123456789')),
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

            for qualification, school, course, graduation_date, regno in zip(qualifications, schools, courses, graduation_dates, regnos):
                Education.objects.create(
                    customer=new_user,
                    qualifications=qualification,
                    school=school,
                    course=course,
                    graduation_date=graduation_date,
                    reg_number=regno,
                )

            for employer_name, company_name, company_email, company_phone, position_held, date_from, date_to, experience in zip(employer_names,company_names,company_emails,company_phones,position_helds,date_froms,date_tos,experiences):
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
            if ('Phd' in qualifications) and ('Masters' in qualifications) and ('Degree' in qualifications) and ('Certificate' in qualifications) and ('Degree' in qualifications) and ('Diploma' in qualifications):
                status='ULTIMATE'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )
            elif ('Diploma' in qualifications):
                status = 'BASIC'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )
            elif ('Degree' in qualifications) and ('Diploma' in qualifications):
                status = 'BASIC'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )

            elif('Masters' in qualifications) and ('Degree' in qualifications) :
                status = 'PREMIUM'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )
            elif('Certificate' in qualifications) and ('Degree' in qualifications) and ('Diploma' in qualifications):
                status = 'BASIC'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )

            else:
                status = 'BASIC'
                Customer.objects.filter(user_ptr_id=new_user.id).update(
                    rank_status=status,
                )
            new_userrr = authenticate(username=username, password=password1)
            print(new_user)
            login(request, new_userrr)
            sweetify.success(request, 'You did it', text='Good job! You successfully Registered, Make Payment to Continue', persistent='Continue')
            data = {
                'results': 'success',
                'success': 'Good job! You successfully Registered, just login'
            }
            return JsonResponse(data, safe=False)

        else:
            form1 = PersonelRegisterForm(request.POST,request.FILES)
            #
            data = {
                'results':'error',
                'form':form1,
            }
            return render_to_response('normal/signup/errors.html', data)




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
        'bachelors':qbfile.readlines(),
        'certificates':qbfile2.readlines(),
        'diplomas':qbfile3.readlines(),
        'phds':qbfile4.readlines(),
        'masters':qbfile5.readlines(),
        'unis':qbfile6.readlines(),
        'counties':County.objects.all(),
        'regions':Region.objects.all(),
        'categories':Category.objects.all(),
    }
    return render(request,'normal/signup/signup.html',context)

# def company_signupform_handling(request):
#
#
#     return redirect('LML:companysignup' )
        # return redirect('LML:companysignup')

def update_employers_profile(request):
    user= request.user.id

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
            updated=form.save()
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
            sweetify.success(request, 'Success', text='Good job! You successfully Updated Your Account', persistent='Ok')
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

                user=authenticate(request, username=username, password=password)
                if user is not None:
                    if  user.is_active and user.is_superuser:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue')
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link', text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link', text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employeedetails')
                else:
                    sweetify.error(request, 'Error', text='Invalid Username and Password', persistent='Retry')
                    source = source.replace('____', '/')
                    return redirect(source)
                    # return render(request, 'normal/login/login.html', {'username': username, })

            if User.objects.filter(email__exact=username).first():

                user = authenticate(request, username=usernamel(username), password=password)
                if user is not None:
                    if  user.is_active and user.is_superuser:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue')
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue')
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

def employer_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            sweetify.success(request, title='Success', text='Password Changed.', persistent='Continue')
            return redirect("LML:employersprofile")
        else:
            form = PasswordChangeForm(request.user)
            sweetify.error(request, 'Error', text='Password not Changed', persistent='Retry')
            return render(request, 'normal/account/employer-profile.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return redirect("LML:employersprofile")


@login_required()
def employerdetails(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    similar_company = Company.objects.filter(category=company.category)
    context = {
       'company':company,
       'social': social,
       'scompany': similar_company,
    }
    return render(request ,'normal/jobdetails/employerdetails.html', context)

@login_required()
def employersprofile(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    # similar_company = Company.objects.filter(category=company.category).exclude(id=user.id)
    categories = Category.objects.all()

    context = {
        'title': 'Company profile',
        'user': request.user,
        'company':company,
        'social':social,
        # 'scompany':similar_company,
        'categories':categories,
        'counties': County.objects.all(),
        'regions': Region.objects.all(),
    }
    return render(request, 'normal/account/employer-profile.html',context)


def employeeprofile(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    social = Social_account.objects.filter(customer=customer).first()

    emShortlist = CompanyShortlistCustomers.objects.filter(customer=customer).count()
    unreadMessages = Message.objects.filter(reciever_id=user, status='UNREAD').count()
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
        'shortlist_count':emShortlist,
        'title': 'Your Profile',
        'customer': customer,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'social': social,
        'bachelors': qbfile.readlines(),
        'certificates': qbfile2.readlines(),
        'diplomas': qbfile3.readlines(),
        'phds': qbfile4.readlines(),
        'masters': qbfile5.readlines(),
        'unis': qbfile6.readlines(),
        'unreadMessages':unreadMessages,
        'counties':County.objects.all(),
        'regions':Region.objects.all(),
        'categories':Category.objects.all(),
    }

    return render(request, 'normal/account/candidate-profile.html', context)

def employee_personal_details_update(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    account_url = request.POST['account_url']
    emailix = request.POST['emailix']
    usernme = request.POST['usernme']
    if request.method == 'POST':
        form = PersonelUpdateForm(request.POST, request.FILES, instance=customer)
        print(form.errors)
        if form.is_valid():
            form.save()
            Social_account.objects.filter(customer=customer).update_or_create(
                account_url=account_url,
            )
            sweetify.success(request, title='Success', text='Personal Account Updated Successfully.', persistent='Continue')
            return redirect('LML:employeeprofile')
        else:
            sweetify.error(request, 'Error', text='Details Not Updated', persistent='Retry')
            return redirect('LML:employeeprofile')
    return redirect('LML:employeeprofile')

def employee_skills_update(request):
    if request.method == 'POST' and request.is_ajax():
        skill_id =  request.POST['skill_id']
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
                'success': 'Error deleting skill'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

def employee_skills_detail_update(request):
    customer =  Customer.objects.filter(user_ptr_id = request.user.id).first()
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
        for employer_name, company_name, company_email, company_phone, position_held, date_from, date_to, experience, exp_id in\
            zip(employer_names, company_names, company_emails, company_phones, position_helds, date_froms, date_tos, experiences, exp_ids):
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
        return redirect('LML:employeeprofile')
    else:
        sweetify.error(request, 'Error', text='Experiences Not Updated', persistent='Retry')
        return redirect('LML:employeeprofile')

def employee_experience_detail_delete(request):
    if request.method == 'POST' and request.is_ajax():
        experience_id =  request.POST['experience_id']
        experience = Experience.objects.filter(id=int(experience_id)).first()
        print(experience)
        if experience:
            experience.delete()
            data = {
                'results': 'success',
                'success': 'Experience deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'success': 'Error deleting Experience'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)

def employee_education_detail_delete(request):
    if request.method == 'POST' and request.is_ajax():
        education_id =  request.POST['education_id']
        education = Education.objects.filter(id=int(education_id)).first()
        print(education)
        if education:
            # education.delete()
            data = {
                'results': 'success',
                'success': 'Education deleted'
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'results': 'error',
                'success': 'Error deleting Education'
            }
            return JsonResponse(data, safe=False)
    data = {

    }
    return JsonResponse(data, safe=False)
def employeedetails(request):
    user=request.user.id
    customer = Customer.objects.filter(user_ptr_id= user).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    social = Social_account.objects.filter(customer=customer)
    context = {
        'customer':customer,
        'skills':skills,
        'educations':educations,
        'experiences':experiences,
        'social':social,
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

        # print(form)
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
                company_reg_no=('CMP'+get_random_string(length=8, allowed_chars='ABDEFGHIJKLNPQRSTUVWXYZ123456789')),
            )
            # sweetify.success(request, 'You did it', text='Good job! You successfully registered', persistent='Ok')
            new_userrr = authenticate(username=username, password=password1)
            print(new_user)
            login(request, new_userrr)
            data = {
                'results': 'success',
                'success': 'Good job! You successfully Registered, just login'
            }
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        else:
            formr = CompanyRegisterForm(request.POST, request.FILES)

            # print(formr.errors)
            # sweetify.error(request, 'Error', text='Ensure you fill all fields correctly', persistent='Retry')
            context3 = {
                'results': 'error',
                'title': 'Create an account',
                'form': formr

            }
            # return JsonResponse(context3, safe=False)
            # return render_to_response('normal/signup/errors.html', context)
            return render_to_response('normal/signup/errors.html', context3)

            # return redirect('LML:companysignup',{'form':form, 'social':form2})

    else:

        form = CompanyRegisterForm()
        form2 = CompanySocialsForm()





    context = {
        'title': 'Create an account',
        'counties':County.objects.all(),
        'regions':Region.objects.all(),
        'categories': Category.objects.all(),
        'form': form,
        'social': form2,


    }

    return render(request, 'normal/signup/create-company.html', context)


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
    context={
        'title':"Advance search",
        'categories': Category.objects.all(),
        "customers": customers,
        'counties': County.objects.all(),
        "regions":Region.objects.all(),
    }
    return render(request, 'normal/advancedsearch/advancedsearch.html', context)




def companypricing(request):
    context={
        'title':'Company Pricing',
        'pricing':CompanyPricingPlan.objects.order_by('price')
    }
    return render(request,'normal/companypricing/companypricing.html', context)


def contactus(request):
    context={
        'title':'Contact Us',
    }
    return render(request,'normal/contact/contact.html', context)


def signup_initial(request):
    context={
        'title': "Signup",
    }
    return render(request, 'normal/signup/signupdecision.html', context)


def termsandconditons(request):
    context={
        'title':'Terms and Conditions',
    }
    return render(request, 'normal/termsandconditions/terms.html', context)


def frequentaskedquestions(request):
    context={
        'title':'FAQ',
    }
    return render(request, 'normal/faq/faq.html', context)


def signup_employee_initial(request):
    context={
        'title':'Employee Signup',
    }
    return render(request, 'normal/signup/employeesignupdecision.html', context )


def signup_company_initial(request):
    context={
        'title':'Company Signup',
    }
    return render(request, 'normal/signup/companysignupdecision.html', context)


def company_contact_us(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id = user).first()
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method =='POST':
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
    customer = Customer.objects.filter(user_ptr_id = user).first()
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method =='POST':
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
    if request.method =='POST':
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


def payment(request):
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    customer_reg = CustomerRegNo.objects.filter(customer=customer).first()
    context = {
        'regno':customer_reg,
        'customer':customer,
    }
    return render(request,'normal/payment/payment-method.html', context)

def companypayment(request):
    company = Company.objects.filter(user_ptr_id=request.user.id).first()
    customer_reg = CompanyRegNo.objects.filter(company=company).first()
    # CompanyRegNo
    context = {
        'regno':customer_reg,
        'customer':company,
    }
    return render(request,'normal/payment/companympesapayment.html', context)

def companypaymentpackage(request, pricing_id):
    pricing = CompanyPricingPlan.objects.filter(id=pricing_id).first()
    # CompanyRegNo
    context = {
        'pricing':pricing,
    }
    return render(request,'normal/companypricing/subscribetoplan.html', context)


def employer_dash(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company)
    context={
        'company': company,
        'social': social,
        'customers':customers,
    }
    return render(request, 'normal/dashboard/employer-dash.html', context)

def employer_dash_message(request, room_name):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company)
    username_of_user = request.user.first_name + "" + request.user.last_name + " messsages"
    context={
        'title': username_of_user,
        'company': company,
        'social': social,
        'customers':customers,
        'room_name_json': mark_safe(json.dumps(room_name))

    }
    return render(request, 'normal/dashboard/employerchatpage.html', context)

def employee_dash_message(request, room_name):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    username_of_user = request.user.first_name + "" + request.user.last_name + " messsages"

    companies_list = []
    userr = User.objects.filter(id=user).first()
    companies = Message.objects.filter(reciever=userr)
    for company in companies:
        cmpn = Company.objects.filter(user_ptr_id=company.sender.id).first()
        companies_list.append(cmpn)
    msg_companies = list(set(companies_list))
    context = {
        'title': username_of_user,
        # 'company': company,
        # 'social': social,
        'customer': customer,
        'msg_comapanies': msg_companies,
        'room_name_json': mark_safe(json.dumps(room_name))

    }
    return render(request, 'normal/dashboard/employee-message-chat.html', context)

def employee_dash(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    social = Social_account.objects.filter(customer=customer).first()
    # customers = CompanyShortlistCustomers.objects.filter(company=company)
    companies_list = []
    userr = User.objects.filter(id=user).first()
    companies = Message.objects.filter(reciever=userr)
    for company in companies:
        cmpn =  Company.objects.filter(user_ptr_id = company.sender.id).first()
        companies_list.append(cmpn)
    msg_companies= list(set(companies_list))

    context={
        'customer': customer,
        'social': social,
        # 'customers':customers,
        'msg_comapanies':msg_companies
    }
    return render(request, 'normal/dashboard/employee-dash.html', context)


def premium_employee_details(request, customer_id):

    customer = Customer.objects.filter(user_ptr_id=customer_id).first()
    educations = Education.objects.filter(customer=customer)
    experiences = Experience.objects.filter(customer=customer)
    skills = Skills.objects.filter(customer=customer)
    social = Social_account.objects.filter(customer=customer)
    reviews = CustomerReviews.objects.filter(customer=customer).order_by('-created_at')
    all_customers = Customer.objects.filter(category_id=customer.category.id)
    print(reviews)
    context = {
        'customer': customer,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'social': social,
        'reviews':reviews,
        'all_customers':all_customers,

    }

    return render(request, 'normal/allcandidates/premium-candidate-detail.html', context)


def all_premium_employees(request):

    if request.method == 'POST':
        county = request.POST['county']
        region = request.POST['region']
        category = request.POST['category']
        cat = Category.objects.filter(id=int(category)).first()
        reg =Region.objects.filter(id=int(region)).first()
        count = County.objects.filter(id=int(county)).first()
        customers = Customer.objects.filter(category=cat, region=reg, county=count)
    else:
        customers = Customer.objects.order_by('?')

    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions':Region.objects.all(),
        'categories': Category.objects.all(),

    }
    return render(request, 'normal/allcandidates/premium-candidate.html', context)


def shortlistcustomers(request):

    if request.method == 'POST':
        customer= request.POST['customer_id']
        company= request.POST['company_id']

        customer_user = Customer.objects.filter(user_ptr_id=customer).first()
        company_user = Company.objects.filter(user_ptr_id=company).first()
        if not CompanyShortlistCustomers.objects.filter(customer=customer, company=company).exists():
            CompanyShortlistCustomers.objects.create(
                customer=customer_user,
                company=company_user,
            )
            data = {
                'shortlisted': 'Successfully shortlisted',
            }
            if data['shortlisted']:
                data['success_message'] ='Successfully Shortlisted'

        else:
            data = {
                'is_shortlisted': 'You have already shortlisted this user',
            }
            if data['is_shortlisted']:
                data['error_message'] = 'You have already shortlisted this user'



        return JsonResponse(data)
def unshortlistcustomers(request):

    if request.method == 'POST':
        customer_id= request.POST.get('customer_id')
        company_id= request.POST.get('company_id')
        print(company_id, customer_id)
        if CompanyShortlistCustomers.objects.filter(customer_id=customer_id, company_id=company_id).exists():
            relation = CompanyShortlistCustomers.objects.filter(customer_id=customer_id, company_id=company_id).first()
            customer =  relation.customer.first_name + relation.customer.last_name
            relation.delete()
            data = {
                'shortlisted':  customer + 'Unshortlisted Successfully',
            }
            if data['shortlisted']:
                data['success_message'] =customer + 'Unshortlisted Successfully'

        else:

            data = {
                'is_shortlisted': 'Error Deleting',
            }
            if data['is_shortlisted']:
                data['error_message'] = 'Error Deleting'



        return JsonResponse(data)



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






    context = {
        'customers': customers,
        'counties': County.objects.all(),
        'regions':Region.objects.all(),
        'categories': Category.objects.all(),

    }
    return render(request, 'normal/allcandidates/all-candidates.html', context)


def categories(request):
    if request.method == 'POST':
        category = request.POST['category']
        categories =Category.objects.filter(id=category)
    else:
        categories= Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,'normal/categories/category.html', context)


def dumb(request):
    if request.method == 'POST':
        file = request.FILES.get('fileupload')
        print(file)
        context = {

        }
        return JsonResponse(context, status=status.HTTP_200_OK)
    context={

    }
    return render(request, 'normal/signup/dumb.html', context)


def messages(request):
    if request.is_ajax() and request.method == 'POST':
        message= request.POST['message']
        sender= request.POST['sender']
        reciever = request.POST['reciever']
        # customer = Customer.objects.filter(user_ptr_id=reciever).first()
        user_sender = User.objects.filter(id=int(sender)).first()
        user_reciever = User.objects.filter(id=int(reciever)).first()
        print(message,sender,reciever,user_reciever,user_sender)
        Message.objects.create(
            msg_content=message,
            sender=user_sender,
            reciever=user_reciever,
        )
        context = {
            'results':'success',
            'msg': message,
            'cmpny' : Company.objects.filter(user_ptr_id = int(sender))
        }
        return JsonResponse(context)
    context = {
        'results': 'error'
    }
    return JsonResponse(context)


def fetch_data_messages(request, customer_id):
    # customer = Customer.objects.filter(id=int(customer_id)).first()
    userr =User.objects.filter(id=customer_id).first()
    messg = Message.objects.filter(reciever=userr, sender_id=request.user.id).order_by('created_at')

    context = {
        'messages': messg,
        'sender': request.user.id
    }
    # content = loader.render_to_string('normal/dashboard/chatb.html', context )

    # html_data = render_to_string('normal/dashboard/employer-dash.html',context, request=request,)
    return render_to_response('normal/dashboard/chatb.html', context)
    # return JsonResponse(content)
    # return render(request, 'normal/dashboard/employer-dash.html', context)




login_required()
def EmployerCustomerShortlist(request):
    user=request.user.id
    company =  Company.objects.filter(user_ptr_id=user).first()
    print(company)
    month_data = []
    months_choices=[]
    months_choices_int=[]
    for i in range(1,13):
        months_choices.append(( datetime.date(2008, i, 1).strftime('%B')[0:3]))
    labels2 = months_choices
    for z in range(1,13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))
    for months_choice in months_choices_int:
        month_data.append(CompanyShortlistCustomers.objects.filter(company_id=company.id, created_at__month=months_choice).count())
    defaultData2 = month_data
    context2={
        'labels2':labels2,
        'defaultData2':defaultData2,

    }

    return JsonResponse(context2)

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


def review_shortlisted_customer(request):
    if request.method == 'POST':
        # message =  request.POST.get('message')
        # ratings =  request.POST.get('ratings')
        # customer =  request.POST.get('customer')
        # company =  request.POST.get('company')
        form = CustomerReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Success', text='Customer Rated Successfully', persistent='Ok')
            return redirect('LML:employer_dash')
        else:
            sweetify.success(request, 'Error', text='Customer Not Rated', persistent='Ok')
        return redirect('LML:employer_dash')

    return


def generate_PDF(request, customer_id):

   employee = Customer.objects.filter(id=int(customer_id)).first()
   experiences = Experience.objects.filter(customer=employee)
   educations = Education.objects.filter(customer=employee)
   skills = Skills.objects.filter(customer=employee)
   social = Social_account.objects.filter(customer=employee).first()
   download = request.GET.get("download")

   filename = "Invoice_%s.pdf" % ("12341231")
   if download:
       content = "attachment; filename='%s'" % (filename)

   context = {
     'employee':employee,
     'experiences':experiences,
     'educations':educations,
     'skills':skills,
     'social':social,
   }
   return render(request, 'normal/Pdf_resume/employee_resume.html', context)


def employee_education_detail_update(request):
    education_ids = request.POST.getlist('education_id')

    schools = request.POST.getlist('school')
    courses = request.POST.getlist('course')
    graduation_dates = request.POST.getlist('graduation_date')
    regnos = request.POST.getlist('reg_number')

    if request.method == 'POST':
        customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
        for education_id, school, course, graduation_date, regno in zip(education_ids, schools, courses, graduation_dates, regnos):
            Education.objects.filter(id=int(education_id)).update(
                customer=customer,
                school=school,
                course=course,
                graduation_date=graduation_date,
                reg_number=regno,
            )
        sweetify.success(request, title='Success', text='Education Updated Successfully.', persistent='Continue')
        return redirect('LML:employeeprofile')
    else:
        sweetify.error(request, 'Error', text='Eeducation Not Updated', persistent='Retry')
        return redirect('LML:employeeprofile')