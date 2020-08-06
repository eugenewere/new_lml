from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'LMLAdmin'
urlpatterns = [
    path('',views.home,name='home'),
    path('messages/employee/',views.employee_messages ,name='E_messages'),
    path('messages/random/',views.random_messages ,name='R_messages'),
    path('messages/company/',views.company_messages, name='C_messages'),
    path('allcandidates/',views.employees, name='employees'),
    path('candidateeedetails/<int:customer_id>',views.employeesdetails, name='employeesdetails'),
    path('premiumemployees/',views.premiumemployees, name='premiumemployees'),
    path('basicemployees/',views.basicemployees, name='basicemployees'),
    path('ultimateemployees/',views.ultimateemployees, name='ultimateemployees'),
    path('shortlistedemployees/',views.shortlistedemployees, name='shortlistedemployees'),
    path('allshortlistedemployeeshistory/',views.allshortlistedemployeeshistory, name='allshortlistedemployeeshistory'),
    path('registeredemployees/',views.registeredemployees, name='registeredemployees'),
    path('unregipayedemployees/',views.unregipayedemployees, name='unregipayedemployees'),
    path('deactivatedemployees/',views.deactivatedemployees, name='deactivatedemployees'),


    path('carouselImages/',views.carouselImages, name='carouselImages'),


    path('allcompanies/',views.companies, name='companies'),
    path('companydetails/<int:company_id>/',views.companydetails, name='companydetails'),
    path('allpremiumcompanies/',views.premiumcompanies, name='premiumcompanies'),
    path('allplatinumcompanies/',views.platinumcompanies, name='platinumcompanies'),
    path('allbasiccompanies/',views.basiccompanies, name='basiccompanies'),
    path('allproultimatecompanies/',views.proultimatecompanies, name='proultimatecompanies'),
    path('allprobasiccompanies/',views.probasiccompanies, name='probasiccompanies'),
    path('allultimatecompanies/',views.ultimatecompanies, name='ultimatecompanies'),
    path('allundefinedcompanies/',views.undefinedcompanies, name='undefinedcompanies'),
    path('allcompaniesregpayment/',views.companiesregpayment, name='companiesregpayment'),
    path('allcompaniesregunpayment/',views.companiesregunpayment, name='companiesregunpayment'),
    path('alldeactivatedemployers/',views.deactivatedemployers, name='deactivatedemployers'),



    path('companyPricing/',views.companyPricing, name='companyPricing'),
    path('addcompanyPricing/',views.addcompanyPricing, name='addcompanyPricing'),
    path('deletecompanyPricing/<int:price_id>',views.deletecompanyPricing, name='deletecompanyPricing'),
    path('editcompanyPricing/<int:price_id>',views.editcompanyPricing, name='editcompanyPricing'),
    path('allcategories/',views.categories, name='categories'),

    # graph
    path('customer_graph/', views.customer_graph, name='customer_graph'),
    path('company_graph/', views.company_graph, name='company_graph'),
    path('messages_graph/', views.messages_graph, name='messages_graph'),

    # emails
    path('replytorandommessagesviaemail/<str:source>', views.reply_to_random_messages_via_email, name='reply_to_random_messages_via_email'),


    # whatweoffer
    path('allwhatweoffer/',views.whatweoffer, name='whatweoffer'),
    path('addwhatweoffer/',views.addwhatweoffer, name='addwhatweoffer'),
    path('editwhatweoffer/<int:offer_id>',views.editwhatweoffer, name='editwhatweoffer'),
    path('deletewhatweoffer/<int:offer_id>',views.deletewhatweoffer, name='deletewhatweoffer'),


   # changestatus
    path('changecandidatestatustonewbee/<int:custom_id>/', views.changecandidatestatustonewbee, name='changecandidatestatustonewbee'),
    path('changecandidatestatustoregi/<int:custom_id>/', views.changecandidatestatustoregi, name='changecandidatestatustoregi'),
    path('changecandidatestatustodeac/<int:custom_id>/', views.changecandidatestatustodeac, name='changecandidatestatustodeac'),

     # changestatus
    path('changecompanystatustonewbee/<int:custom_id>/', views.changecompanystatustonewbee, name='changecompanytatustonewbee'),
    path('changecompanystatustoregi/<int:custom_id>/', views.changecompanystatustoregi, name='changecompanystatustoregi'),
    path('changecompanystatustodeac/<int:custom_id>/', views.changecompanystatustodeac, name='changecompanystatustodeac'),




]