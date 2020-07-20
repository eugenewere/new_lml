from django.conf.urls import url
from django.urls import path, re_path

from . import views
# from .views import EmployerCustomerShortlist

app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),

    # path('li/<str:room_name>/', views.room, name='room'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    # re_path(r"^employerdash_message/(?P<username>[\w.@+-]+)/$", views.employer_dash_message),
    path('employeeShortlistGraph/', views.EmployerCustomerShortlist, name='employee_shortlist_graph'),
    path('employeeShortlistGraphtemplate/', views.EmployerCustomerShortlistTemplate, name='employee_shortlist_graph_template'),

    path('signup/', views.signup_initial, name="signup_initial"),
    path('signupcompany/', views.signup_company_initial, name="signup_company_initial"),
    path('signupemployee/', views.signup_employee_initial, name="signup_employee_initial"),

    path('loginauser/<str:source>/', views.login_user, name="login_user"),
    path('logoutuser/', views.log_out_user, name="log_out_user"),

    path('personelsignup/', views.signup, name="signup"),
    path('companysignup/', views.companysignup, name="companysignup"),
    # path('companysignup/formhandling/', views.company_signupform_handling, name="company_signup_formhandling"),

    path('signin/', views.signin, name="signin"),

    path('employeeprofile/', views.employeeprofile, name="employeeprofile"),
    path('updateemployeepersonaldetails', views.employee_personal_details_update, name='employee_personal_details_update'),
    path('updateemployeeskills', views.employee_skills_update, name='employee_skills_update'),
    path('updateemployeeskillsupdate', views.employee_skills_detail_update, name='employee_skills_detail_update'),
    path('updateemployeexperiencesupdate', views.employee_experience_detail_update, name='employee_experience_detail_update'),
    path('updateemployeeducationsupdate', views.employee_education_detail_update, name='employee_education_detail_update'),
    path('updateemployeexperiencesdelete', views.employee_experience_detail_delete, name='employee_experience_detail_delete'),
    path('updateemployeeducationsdelete', views.employee_education_detail_delete, name='employee_education_detail_delete'),
    path('employeedetails/', views.employeedetails, name="employeedetails"),
    path('advancesearch/', views.advancesearch, name="advancesearch"),

    path('employersprofile/', views.employersprofile, name="employersprofile"),
    path('updateemployersprofile/', views.update_employers_profile, name="update_employers_profile"),
    path('employerdetails/', views.employerdetails, name="employerdetails"),

    path('employer/user_account/change_password', views.employer_change_password, name='employer_change_password'),

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

    path('employerdash/',views.employer_dash, name='employer_dash'),
    path('employerdash_message/<str:room_name>/',views.employer_dash_message, name='employer_dash_message'),

    path('employeedash/',views.employee_dash, name='employee_dash'),
    path('employee_dash_message/<str:room_name>/',views.employee_dash_message, name='employee_dash_message'),

    # employeestatus
    path('allpremiumemployees/',views.all_premium_employees, name = 'all_premium_employees'),
    path('allemployees/',views.all_employees, name = 'all_employees'),
    path('premiumemployeedetails/<int:customer_id>', views.premium_employee_details, name='premium_employee_detail'),

    path('shortlist/', views.shortlistcustomers, name='shortlistemployees'),
    path('unshortlist/', views.unshortlistcustomers, name='unshortlistemployees'),
    path('categories/', views.categories, name='viewcategories'),

    path('dumb/', views.dumb, name='dumb'),

    path('sendmessages/', views.messages, name='messages'),
    path('fetchmessages/<int:customer_id>', views.fetch_data_messages, name='fetch_data_messages'),


    path('reviewshortlistedcustomer', views.review_shortlisted_customer, name='review_shortlisted_customer'),


    # pdf
    path('customer/resume/<int:customer_id>', views.generate_PDF, name='customer_resume_pdf'),




]