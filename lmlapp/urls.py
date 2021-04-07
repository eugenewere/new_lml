from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
import random, string



# def id_generator(size=122, chars=string.ascii_lowercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))


app_name = 'LML'



urlpatterns = [
    path('', views.home, name="home"),
    # path('li/<str:room_name>/', views.room, name='room'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    # re_path(r"^employerdash_message/(?P<username>[\w.@+-]+)/$", views.employer_dash_message),
    path('candidateShortlistGraph/', views.EmployerCustomerShortlist, name='employee_shortlist_graph'),
    path('candidateShortlistGraphTime/', views.candidateShortlistGraphTime, name='candidateShortlistGraphTime'),
    # path('candidateShortlistGraphStatusType/', views.candidateShortlistGraphStatusType, name='candidateShortlistGraphStatusType'),

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
    path('daraja/stk-push/', views.mpesa_stk_push_callback, name='mpesa_stk_push_callback'),
    path('send_stk-push/', views.send_stk_push_callback, name='mpesa_send_stk_push_callback'),
    path('companydash/',views.employer_dash, name='employer_dash'),


    path('candidatedash/',views.employee_dash, name='employee_dash'),
    path('candidateviewpdf/<cv_id>',views.userviewpdf, name='userviewpdf'),

    # employeestatus
    path('allpremiumcandidates/',views.all_premium_employees, name = 'all_premium_employees'),
    path('allcategorycandidates/<int:category_id>',views.all_category_employees, name = 'all_category_employees'),
    path('alloffercandidates/<str:offer>',views.all_offer_employees, name = 'all_offer_employees'),
    path('allcandidates/',views.all_employees, name = 'all_employees'),
    path('potentialcandidatedetails/<int:customer_id>', views.premium_employee_details, name='premium_employee_detail'),

    path('shortlist/', views.shortlistcustomers, name='shortlistemployees'),
    # path('unshortlist/', views.unshortlistcustomers, name='unshortlistemployees'),
    path('categories/', views.categories, name='viewcategories'),

    path('dumb/', views.dumb, name='dumb'),




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



    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('registrationpaydetails/', views.registrationpaydetails, name='registrationpaydetails'),
    path('payment_complete/', views.payment_complete, name='payment_complete'),



    path('companyregistrationpaydetails/', views.companyregistrationpaydetails, name='companyregistrationpaydetails'),
    path('company_payment_complete/', views.comapny_payment_complete, name='comapny_payment_complete'),
    path('company_payment-done/', views.company_payment_done, name='company_payment_done'),
    path('company_payment-cancelled/', views.company_payment_canceled, name='company_payment_cancelled'),

    path('company_price_details/<int:price_id>', views.company_price_details, name='company_price_details'),
    path('company_price_details_record/<int:price_id>', views.company_price_details_record, name='company_price_details_record'),
    path('payment-status-done/', views.payment_company_status_done, name='payment_company-status_done'),
    path('payment-status-cancelled/', views.payment_company_status_canceled, name='payment_company-status_cancelled'),

    path('candidate_files_upload/', views.candidate_files_upload, name='candidate_files_upload'),
    path('candidate_files_delete/', views.candidate_files_delete_single, name='candidate_files_delete_single'),
    path('candidate_files_delete_multiple/', views.candidate_files_delete_multiple_single, name='candidate_files_delete_multiple_single'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]