import json
from html import escape

import sweetify
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils.safestring import mark_safe
from humanize import naturaltime

from lmlappadmin.models import *


@login_required()
def employer_dash_message(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company, payment_status='SHORTLISTED')
    u = User.objects.filter(id=user).first()
    messages_count = Message.objects.filter(readstatus='UNREAD',reciever=u, delstar='NORMAL').exclude(sender=u).count()
    username_of_user = request.user.first_name + "" + request.user.last_name + "("+ str(messages_count) +")"

    product_label = Message.objects.filter(sender=u, labels='PRODUCT')
    misc_label = Message.objects.filter(sender=u, labels='MISC')
    work_label = Message.objects.filter(sender=u, labels='WORk')
    undefined_label = Message.objects.filter(sender=u, labels='UNDEFINED')

    context={
        # 'allmessages': Message.objects.filter(sender=u,  delstar='NORMAL').order_by('-created_at'),
        'allmessages': Message.objects.filter(Q(sender=u) | Q(reciever=u), delstar='NORMAL').order_by('-created_at'),
        'inboxmessages': Message.objects.filter(reciever=u, delstar='NORMAL').order_by('-created_at'),
        'sentmessages': Message.objects.filter(sender=u),
        'starredmessages': Message.objects.filter(sender=u, delstar='STARRED'),
        'trashmessages': Message.objects.filter(sender=u, delstar='DELETE'),
        'title': username_of_user,
        'company': company,
        'social': social,
        'customers':customers,
        'product_label':product_label,
        'misc_label':misc_label,
        'work_label':work_label,
        'undefined_label':undefined_label,
        'messages_count':messages_count,



        # 'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'employer/app-email.html', context)

@login_required()
def messages(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        sender = request.user.id
        recievers = request.POST.getlist('recievers')
        room = request.user.id
        subject = request.POST.get('subject')
        label = request.POST.get('label')
        file = request.FILES.get('filee')


        user = User.objects.filter(id=sender).first()
        if user is not None:
            for reciever in recievers:
                reciever_user = User.objects.filter(id=reciever).first()
                Message.objects.create(
                    msg_content=message,
                    sender=user,
                    reciever=reciever_user,
                    subject=subject,
                    labels=label.upper(),
                    file=file,
                    room=int(str(user.id) + str(reciever_user.id))
                )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        return redirect('Chat:employer_dash_message')

    return redirect('Chat:employer_dash_message')

@login_required()
def fetch_data_messages(request):
    # company = Company.objects.filter(user_ptr_id = request.user.id).first()
    # messages = Message.objects.filter(sender=company).order_by('-created_at')[:11]
    # print(messages)
    # context = {
    #
    # }
    # # return JsonResponse(context)
    # return render(request, 'normal/dashboard/../chat/templates/employer/message.html', {'messages': messages, })
    pass