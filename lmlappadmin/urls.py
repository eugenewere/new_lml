from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'LMLAdmin'
urlpatterns = [
    path('',views.home,name='home'),
    path('account/',views.useradminaccount,name='useradminaccount'),
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
    path('carouselImagesDelete/<int:carousel_id>/',views.carouselImagesDelete, name='carouselImagesDelete'),


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
    path('deleteallcompanyPricing/',views.deleteallcompanyPricing, name='deleteallcompanyPricing'),
    path('editcompanyPricing/<int:price_id>',views.editcompanyPricing, name='editcompanyPricing'),
    path('allcategories/',views.categories, name='categories'),

    # graph
    path('customer_graph/', views.customer_graph, name='customer_graph'),
    path('registration_graph/', views.registration_graph, name='registration_graph'),
    path('registration_graph_time/', views.registration_graph_time, name='registration_graph_time'),
    path('companystatuspaymentgraph/', views.companystatuspaymentgraph, name='companystatuspaymentgraph'),
    path('companystatuspaymentgraphtime/', views.companystatuspaymentgraphtime, name='companystatuspaymentgraphtime'),
    path('company_graph/', views.company_graph, name='company_graph'),
    path('company_graph_time_filter/', views.company_graph_time_filter, name='company_graph_time_filter'),
    path('candidate_graph_time_filter/', views.candidate_graph_time_filter, name='candidate_graph_time_filter'),
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

    # candidatepricing
    path('allcandidateregpricing/', views.candidateregpricing, name='candidateregpricing'),
    path('allcandidateaddregpricing/', views.candidateaddregpricing, name='candidateaddregpricing'),
    path('allcandidateupdateregpricing/<int:price_id>/', views.candidateupdateregpricing, name='candidateupdateregpricing'),
    path('allcandidatedeleteregpricing/<int:price_id>/', views.candidatedeleteregpricing, name='candidatedeleteregpricing'),
    path('allcandidatestatusregpricing/<int:price_id>/', views.candidatestatusregpricing, name='candidatestatusregpricing'),

    # compdidatepricing
    path('allcompanyregpricing/', views.companyregpricing, name='companyregpricing'),
    path('allcompanyaddregpricing/', views.companyaddregpricing, name='companyaddregpricing'),
    path('allcompanyupdateregpricing/<int:price_id>/', views.companyupdateregpricing, name='companyupdateregpricing'),
    path('allcompanydeleteregpricing/<int:price_id>/', views.companydeleteregpricing, name='companydeleteregpricing'),
    path('allcompanystatusregpricing/<int:price_id>/', views.companystatusregpricing, name='companystatusregpricing'),

    path('analytics/', views.analytics, name='analytics'),
    path('admin/change_password', views.admin_change_password, name='admin_change_password'),
    path('admin/edit_account', views.admin_edit_account, name='admin_edit_account'),

    path('county/', views.county, name='county'),
    path('region/', views.region, name='region'),

    path('compayments/', views.payments, name='companypayments'),
    path('candpayments/', views.candpayments, name='candidatepayments'),
]