from . import views
from django.urls import path

app_name = 'Chat'
urlpatterns = [
    path('chat', views.employer_dash_message, name='employer_dash_message'),
    path('sendmessages/', views.messages, name='messages'),
    path('fetchmessages/', views.fetch_data_messages, name='fetch_data_messages'),
]
