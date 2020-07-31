from django.conf.urls import url
from django.urls import path, re_path

from . import views
import random, string


def id_generator(size=122, chars=string.ascii_lowercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),

    # path('li/<str:room_name>/', views.room, name='room'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    # re_path(r"^employerdash_message/(?P<username>[\w.@+-]+)/$", views.employer_dash_message),
    path('candidateShortlistGraph/', views.EmployerCustomerShortlist, name='employee_shortlist_graph'),
    path('candidateShortlistGraphtemplate/', views.EmployerCustomerShortlistTemplate, name='employee_shortlist_graph_template'),

    path('signup', views.signup_initial, name="signup_initial"),
    path('signupcompany/', views.signup_company_initial, name="signup_company_initial"),
    path('signupcandidate/', views.signup_employee_initial, name="signup_employee_initial"),

    path('loginauser/<str:source>/', views.login_user, name="login_user"),
    path('logoutuser/', views.log_out_user, name="log_out_user"),

    path('personelsignup/', views.signup, name="signup"),
    path('companysignup/', views.companysignup, name="companysignup"),
    # path('companysignup/formhandling/', views.company_signupform_handling, name="company_signup_formhandling"),

    path('signin/', views.signin, name="signin"),

    path('candidateprofile/', views.employeeprofile, name="employeeprofile"),
    path('updatecandidatepersonaldetails', views.employee_personal_details_update, name='employee_personal_details_update'),
    path('updatecandidateskills', views.employee_skills_update, name='employee_skills_update'),
    path('updatecandidateskillsupdate', views.employee_skills_detail_update, name='employee_skills_detail_update'),
    path('updatecandidatexperiencesupdate', views.employee_experience_detail_update, name='employee_experience_detail_update'),
    path('updatecandidateducationsupdate', views.employee_education_detail_update, name='employee_education_detail_update'),
    path('updatcandidateexperiencesdelete', views.employee_experience_detail_delete, name='employee_experience_detail_delete'),
    path('updatcandidateeducationsdelete', views.employee_education_detail_delete, name='employee_education_detail_delete'),
    path('candidatedetails/', views.employeedetails, name="employeedetails"),
    path('advancesearch/', views.advancesearch, name="advancesearch"),

    path('compantsprofile/', views.employersprofile, name="employersprofile"),
    path('updatecompantsprofile/', views.update_employers_profile, name="update_employers_profile"),
    path('compantdetails/', views.employerdetails, name="employerdetails"),

    path('company/user_account/change_password', views.employer_change_password, name='employer_change_password'),
    path('company/user_account/change_password', views.employee_change_password, name='employee_change_password'),

    path('companypricing/', views.companypricing, name="companypricing"),
    path('contactus/', views.contactus, name="contactus"),

    path('termsandconditons/', views.termsandconditons, name="termsandconditons"),
    path('FAQ/', views.frequentaskedquestions, name="frequentaskedquestions"),

    path('companycontactus/',views.company_contact_us, name='company_contact_us'),
    path('homecontactus/<str:source>',views.home_contact_us, name='home_contact_us'),
    path('customercontactus/', views.customer_contact_us, name='customer_contact_us'),

    path('payment/',views.payment, name='payment'),
    path('companypayment/',views.companypayment, name='companypayment'),
    path('companypaymentpackage/<int:pricing_id>',views.companypaymentpackage, name='companypaymentpackage'),

    path('companydash/',views.employer_dash, name='employer_dash'),
    path('companydash_message/<str:room_name>/',views.employer_dash_message, name='employer_dash_message'),

    path('candidatedash/',views.employee_dash, name='employee_dash'),
    path('candidate_dash_message/<str:room_name>/',views.employee_dash_message, name='employee_dash_message'),

    # employeestatus
    path('allpremiumcandidates/',views.all_premium_employees, name = 'all_premium_employees'),
    path('allcategorycandidates/<int:category_id>',views.all_category_employees, name = 'all_category_employees'),
    path('allcandidates/',views.all_employees, name = 'all_employees'),
    path('premiumcandidatedetails/<int:customer_id>', views.premium_employee_details, name='premium_employee_detail'),

    path('shortlist/', views.shortlistcustomers, name='shortlistemployees'),
    path('unshortlist/', views.unshortlistcustomers, name='unshortlistemployees'),
    path('categories/', views.categories, name='viewcategories'),

    path('dumb/', views.dumb, name='dumb'),

    path('sendmessages/', views.messages, name='messages'),
    path('fetchmessages/<int:customer_id>', views.fetch_data_messages, name='fetch_data_messages'),


    path('reviewshortlistedcustomer', views.review_shortlisted_customer, name='review_shortlisted_customer'),


    # pdf
    path('customer/resume/<int:customer_id>', views.generate_PDF, name='customer_resume_pdf'),

    path('update/add/skill/dvdsjkxzmvnesdk/', views.update_add_skill, name='update_skill_add'),
    path('update/add/s_experience/dvdsjksakjfvsdzxk/', views.update_add_experience, name='update_add_experience'),
    path('update/add/s_education/dvdsjksakjfvsdzxk/', views.update_add_education, name='update_add_education'),
    path('update/add/s_social/dvdsjksakjfvsdzxk/', views.update_add_social, name='update_add_social'),
    path('deletesocial/', views.deletesocial, name='deletesocial'),
    path('checkifemailexists/', views.checkifemailexists, name='checkifemailexists'),
    path('checkifusernameexists/', views.checkifusernameexists, name='checkifusernameexists'),


]