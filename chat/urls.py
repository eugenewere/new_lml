from . import views
from django.urls import path

app_name = 'Chat'
urlpatterns = [
    path('chat', views.employer_dash_message, name='employer_dash_message'),
    path('sendmessages/', views.messages, name='messages'),
    # path('fetchmessages/', views.fetch_data_messages, name='fetch_data_messages'),
    path('trashmessage/', views.trashmessage, name='trashmessage'),
    path('permtrashmessage/', views.permtrashmessage, name='permtrashmessage'),
    path('restoretrashmessage/', views.restoretrashmessage, name='restoretrashmessage'),
    path('starredmessage/', views.starredmessage, name='starredmessage'),
    path('mark_as_read_or_unread/', views.mark_as_read_or_unread, name='mark_as_read_or_unread'),

    path('candidate_dash_message/', views.employee_dash_message, name='employee_dash_message'),
    path('message_reply/', views.message_reply, name='message_reply'),
    path('message_read/', views.message_read, name='message_read'),
    path('message_count/', views.message_count, name='message_count'),

]
