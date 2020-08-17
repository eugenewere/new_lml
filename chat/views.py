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
def employee_dash_message(request):
    user = request.user.id
    customer = Customer.objects.filter(user_ptr_id=user).first()
    username_of_user = request.user.first_name + "" + request.user.last_name + " messsages"
    u = User.objects.filter(id=user).first()




    companies_list = []
    userr = User.objects.filter(id=user).first()
    companies = Message.objects.filter(reciever=userr)
    for company in companies:
        cmpn = Company.objects.filter(user_ptr_id=company.sender.id).first()
        companies_list.append(cmpn)
    msg_companies = list(set(companies_list))

    blocked = MsgStatus.objects.filter(Q(m_user=u) and (Q(delstar='DELETE') | Q(delstar='NORMAL'))).values_list(
        'message_id', flat=True)
    product_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='PRODUCT').exclude(
        id__in=blocked).order_by('-created_at').all()
    misc_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='MISC').exclude(id__in=blocked).order_by(
        '-created_at').all()
    work_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='WORK').exclude(id__in=blocked).order_by(
        '-created_at').all()
    undefined_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='UNDEFINED').exclude(
        id__in=blocked).order_by('-created_at').all()

    messages_count = Message.objects.filter(readstatus='UNREAD', reciever=u).exclude(sender=u).count()
    if messages_count > 0:
        username_of_user = request.user.first_name + "" + request.user.last_name + "(" + str(messages_count) + ")"
    else:
        username_of_user = request.user.first_name + "" + request.user.last_name
    # print(product_label)
    starreds = []
    starredmsgs = MsgStatus.objects.filter(m_user=u, delstar='STARRED').order_by('-created_at').all()
    for stm in starredmsgs:
        starreds.append(stm.message)
    trashes = []
    trashedmsgs = MsgStatus.objects.filter(m_user=u, delstar='DELETE').order_by('-created_at').all()
    for trm in trashedmsgs:
        trashes.append(trm.message)

    # print(blocked)
    procuct_l = Message.objects.filter(sender=u).exclude(id__in=blocked).order_by('-created_at').all()
    # print(procuct_l)
    context = {
        'allmessages': Message.objects.filter(Q(sender=u) | Q(reciever=u)).exclude(id__in=blocked).order_by('-created_at').all(),
        'sentmessages': Message.objects.filter(sender=u).exclude(id__in=blocked).order_by('-created_at').all(),        #
        'inboxmessages': Message.objects.filter(reciever=u).exclude(id__in=blocked).order_by('-created_at'),
        'starredmessages': starreds,
        'trashmessages':trashes,
        'title': username_of_user,
        'company': company,
        # 'social': social,
        # 'customers':customers,
        'product_label':product_label,
        'misc_label':misc_label,
        'work_label':work_label,
        'undefined_label':undefined_label,
        'messages_count':messages_count,

    }
    return render(request, 'employee/employee-email.html', context)
@login_required()
def employer_dash_message(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id=user).first()
    social = CompanySocialAccount.objects.filter(company=company).first()
    customers = CompanyShortlistCustomers.objects.filter(company=company, payment_status='SHORTLISTED')
    u = User.objects.filter(id=user).first()
    # Message.objects.update(
    #     readstatus='UNREAD'
    # )
    messages_count = Message.objects.filter(readstatus='UNREAD',reciever=u).exclude(sender=u).count()
    if messages_count > 0:
        username_of_user = request.user.first_name + "" + request.user.last_name + "("+ str(messages_count) +")"
    else:
        username_of_user = request.user.first_name + "" + request.user.last_name

    blocked = MsgStatus.objects.filter(Q(m_user=u) and (Q(delstar='DELETE') | Q(delstar='NORMAL'))).values_list('message_id', flat=True)
    product_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='PRODUCT').exclude(id__in=blocked).order_by('-created_at').all()
    misc_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='MISC').exclude(id__in=blocked).order_by('-created_at').all()
    work_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='WORK').exclude(id__in=blocked).order_by('-created_at').all()
    undefined_label = Message.objects.filter(Q(sender=u) | Q(reciever=u), label='UNDEFINED').exclude(id__in=blocked).order_by('-created_at').all()
    # print(product_label)
    starreds=[]
    starredmsgs = MsgStatus.objects.filter(m_user=u, delstar='STARRED').order_by('-created_at').all()
    for stm in starredmsgs:
        starreds.append(stm.message)
    trashes=[]
    trashedmsgs = MsgStatus.objects.filter(m_user=u, delstar='DELETE').order_by('-created_at').all()
    for trm in trashedmsgs:
        trashes.append(trm.message)



    # print(blocked)
    procuct_l = Message.objects.filter(sender=u).exclude(id__in=blocked).order_by('-created_at').all()
    # print(procuct_l)
    context={
        # 'allmessages':procuct_l,
        'allmessages': Message.objects.filter(Q(sender=u) | Q(reciever=u)).exclude(id__in=blocked).order_by('-created_at').all(),
        'sentmessages': Message.objects.filter(sender=u).exclude(id__in=blocked).order_by('-created_at').all(),        #
        'inboxmessages': Message.objects.filter(reciever=u).exclude(id__in=blocked).order_by('-created_at'),
        'starredmessages': starreds,
        'trashmessages':trashes,
        'title': username_of_user,
        'company': company,
        'social': social,
        'customers':customers,
        'product_label':product_label,
        'misc_label':misc_label,
        'work_label':work_label,
        'undefined_label':undefined_label,
        'messages_count':messages_count,
    }
    return render(request, 'employer/app-email.html', context)

@login_required()
def messages(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        sender = request.user.id
        recievers = request.POST.getlist('recievers')
        subject = request.POST.get('subject')
        label = request.POST.get('label')
        file = request.FILES.get('filee')
        mess = message


        user = User.objects.filter(id=sender).first()
        if user is not None:
            for reciever in recievers:
                reciever_user = User.objects.filter(id=reciever).first()
                message = Message.objects.create(
                    msg_content=mess,
                    sender=user,
                    reciever=reciever_user,
                    subject=subject,
                    label=label.upper(),
                    file=file,
                    room=int(str(user.id) + str(reciever_user.id))
                )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        return redirect('Chat:employer_dash_message')

    return redirect('Chat:employer_dash_message')

@login_required()
@csrf_exempt
def trashmessage(request):
    if request.method == 'POST':
        usr = request.user.id
        list1 = request.POST.getlist('v[]')
        user = User.objects.filter(id= usr).first()
        for i in list1:
            message = Message.objects.filter(id=int(i)).first()
            if not MsgStatus.objects.filter(m_user=user, message=message).exists():
                MsgStatus.objects.create(
                    m_user= user,
                    message=message,
                    delstar='DELETE',
                )
            else:
                MsgStatus.objects.filter(m_user=user, message=message).update(
                    delstar='DELETE',
                )

        context={
            'test': 'success',
            'trash_count': MsgStatus.objects.filter(m_user=user,delstar='DELETE' ).count(),
        }
        return JsonResponse(context)
    pass

@login_required()
@csrf_exempt
def permtrashmessage(request):
    if request.method == 'POST':
        usr = request.user.id
        list1 = request.POST.getlist('v[]')
        user = User.objects.filter(id=usr).first()
        for i in list1:
            message = Message.objects.filter(id=int(i)).first()
            if MsgStatus.objects.filter(m_user=user, message=message).exists():
                MsgStatus.objects.filter(m_user=user, message=message).update(
                    delstar='NORMAL',
                )
        context = {
            'test': 'success',
            'trash_count': MsgStatus.objects.filter(m_user=user, delstar='DELETE').exclude(delstar='NORMAL').count(),
        }
        return JsonResponse(context)
    pass
@login_required()
@csrf_exempt
def restoretrashmessage(request):
    if request.method == 'POST':
        usr = request.user.id
        list1 = request.POST.getlist('v[]')
        user = User.objects.filter(id=usr).first()
        for i in list1:
            message = Message.objects.filter(id=int(i)).first()
            if MsgStatus.objects.filter(m_user=user, message=message).exists():
                msg=MsgStatus.objects.filter(m_user=user, message=message)
                if msg:
                    msg.delete()

        context = {
            'test': 'success',
            'trash_count': MsgStatus.objects.filter(m_user=user, delstar='DELETE').exclude(delstar='NORMAL').count(),
        }
        return JsonResponse(context)
    pass

@login_required()
@csrf_exempt
def starredmessage(request):
    if request.method == 'POST':
        usr = request.user.id
        message_raw_id = request.POST.get('v')
        user = User.objects.filter(id=usr).first()
        message = Message.objects.filter(id=message_raw_id).first()
        if not MsgStatus.objects.filter(message=message, m_user=user, delstar='STARRED').first():
            if MsgStatus.objects.filter(message=message, m_user=user, delstar='DELETE').first():
                MsgStatus.objects.filter(message=message, m_user=user).update(
                    delstar='STARRED',
                )
            else:
               MsgStatus.objects.create(
                    m_user=user,
                    message=message,
                    delstar='STARRED',
               )
        else:
            m = MsgStatus.objects.filter(m_user=user, message=message, delstar='STARRED').first()
            if m:
                m.delete()

        context = {
            'test': 'success',
            'starred_count': MsgStatus.objects.filter(m_user=user, delstar='STARRED').exclude(delstar='NORMAL').count(),
        }
        return JsonResponse(context)
    pass

@login_required()
@csrf_exempt
def mark_as_read_or_unread(request):
    if request.method == 'POST':
        usr = request.user.id
        list1 = request.POST.getlist('v[]')
        user = User.objects.filter(id=usr).first()
        for i in list1:
            message = Message.objects.filter(id=int(i)).first()
            if Message.objects.filter(reciever=user, id=message.id, readstatus='UNREAD'):
                Message.objects.filter(reciever=user, id=message.id).update(
                    readstatus='READ'
                )
            elif Message.objects.filter(reciever=user, id=message.id, readstatus='READ'):
                Message.objects.filter(reciever=user, id=message.id).update(
                    readstatus='UNREAD'
                )
        messages_count = Message.objects.filter(readstatus='UNREAD', reciever=user).exclude(sender=usr).count()
        if messages_count > 0:
            username_of_user = request.user.first_name + "" + request.user.last_name + "(" + str(messages_count) + ")"
        else:
            username_of_user = request.user.first_name + "" + request.user.last_name

        context = {
            'test': 'success',
            'inbox_unread_count':  Message.objects.filter(reciever=user, readstatus="UNREAD").count(),
            'msg_count': messages_count,
            'title': username_of_user,
        }
        return JsonResponse(context)





def message_reply(request):
    if request.method =='POST':
       file = request.FILES.get('filee')
       messageee = request.POST.get('message')
       message_id = request.POST.get('message_id')
       sender = request.user.id
       reciever = request.POST.get('reciever')
       subject = request.POST.get('subject')
       label = request.POST.get('label')
       # print(messageee, subject, label, file)

       user = User.objects.filter(id=sender).first()
       msg = Message.objects.filter(id=message_id).first()
       if user is not None:
           reciever_user = User.objects.filter(id=reciever).first()
           Message.objects.create(
               msg_content=messageee,
               sender=user,
               reply_id=msg.id,
               reciever=reciever_user,
               subject=subject,
               label=label.upper(),
               file=file,
               room=int(str(user.id) + str(reciever_user.id))
           )
           Message.objects.filter(id=msg.id).update(
               readstatus='READ'
           )

    context = {
        'test': 'success',
    }
    return JsonResponse(context)


def message_read(request):
    if request.method =='POST':
       message_id = request.POST.get('message_id')
       msg = Message.objects.filter(id=message_id).first()
       user = User.objects.filter(id=request.user.id).first()
       # print(message_id, user,msg )
       if user is not None and msg is not None:
          Message.objects.filter(id=msg.id).update(
              readstatus='READ',
          )
          messages_count = Message.objects.filter(readstatus='UNREAD', reciever=user).exclude(sender=user).count()
          if messages_count > 0:
              username_of_user = request.user.first_name + "" + request.user.last_name + "(" + str(messages_count) + ")"
          else:
              username_of_user = request.user.first_name + "" + request.user.last_name
          context = {
                'test': 'success',
                'msg_count':messages_count,
                'title': username_of_user,
          }
       else:
           context = {
               'test': 'error',
           }

    return JsonResponse(context)


def message_count(request):
    u = request.user.id
    user = User.objects.filter(id=u).first()
    if user:
        messages_count = Message.objects.filter(readstatus='UNREAD', reciever=user).exclude(sender=user).count()
        context={
            'test': 'success',
            'msg_count': messages_count,

        }
        return JsonResponse(context)
    else:
        context={
             'test': 'error',
             'msg_count': 0,
        }
        return JsonResponse(context)

