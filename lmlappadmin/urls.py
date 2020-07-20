from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'LMLAdmin'
urlpatterns = [
    path('',views.home,name='home'),
    path('messages/employee/',views.employee_messages ,name='E_messages'),
    path('messages/random/',views.random_messages ,name='R_messages'),
    path('messages/company/',views.company_messages, name='C_messages'),
    path('allemployees/',views.employees, name='employees'),
    path('premiumemployees/',views.premiumemployees, name='premiumemployees'),
    path('shortlistedemployees/',views.shortlistedemployees, name='shortlistedemployees'),
    path('registeredemployees/',views.registeredemployees, name='registeredemployees'),
    path('deactivatedemployees/',views.deactivatedemployees, name='deactivatedemployees'),


    path('carouselImages/',views.carouselImages, name='carouselImages'),


    path('allcompanies/',views.companies, name='companies'),
    path('allpremiumcompanies/',views.premiumcompanies, name='premiumcompanies'),
    path('allplatinumcompanies/',views.platinumcompanies, name='platinumcompanies'),
    path('allbasiccompanies/',views.basiccompanies, name='basiccompanies'),
    path('allproultimatecompanies/',views.proultimatecompanies, name='proultimatecompanies'),
    path('allprobasiccompanies/',views.probasiccompanies, name='probasiccompanies'),
    path('allultimatecompanies/',views.ultimatecompanies, name='ultimatecompanies'),
    path('allundefinedcompanies/',views.undefinedcompanies, name='undefinedcompanies'),
    path('allcompaniesregpayment/',views.companiesregpayment, name='companiesregpayment'),
    path('alldeactivatedemployers/',views.deactivatedemployers, name='deactivatedemployers'),



    path('companyPricing/',views.companyPricing, name='companyPricing'),
    path('allcategories/',views.categories, name='categories'),

    # graph
    path('customer_graph/', views.customer_graph, name='customer_graph'),
    path('company_graph/', views.company_graph, name='company_graph'),
    path('messages_graph/', views.messages_graph, name='messages_graph'),

    # emails
    path('replytorandommessagesviaemail/<str:source>', views.reply_to_random_messages_via_email, name='reply_to_random_messages_via_email'),
]