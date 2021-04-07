from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
# from django_daraja.mpesa.exceptions import IllegalPhoneNumberException
from requests.auth import HTTPBasicAuth
import json

# Create your views here.
from lmlappadmin.models import *
from mpesa_api.mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword


def getAccessToken(request):
    consumer_key = 'hAAktGjatKXAj9zAXDKLjooL799UM7bz'
    consumer_secret = 'xj4MmNm90E0b1W3A'
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    # api_url = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    phone_number = 254700020958
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA":  format_phone_number(phone_number),  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber":  format_phone_number(phone_number),  # replace with your phone number to get stk push
        "CallBackURL": "https://536095ee014f.ngrok.io/api/c2b/confirmation",
        "AccountReference": "LABOUR MARKET LINK LIMITED",
        "TransactionDesc": "Pay Registration Number"
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response)
    return HttpResponse(response)

# def lipa_na_mpesa_online(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     request = {
#         "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#         "Password": LipanaMpesaPpassword.decode_password,
#         "Timestamp": LipanaMpesaPpassword.lipa_time,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": 1,
#         "PartyA": 254700020958,  # replace with your phone number to get stk push
#         "PartyB": LipanaMpesaPpassword.Business_short_code,
#         "PhoneNumber": 254700020958,  # replace with your phone number to get stk push
#         "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
#         "AccountReference": "LABOUR MARKET LINK LIMITED",
#         "TransactionDesc": "Testing stk push"
#     }
#     response = requests.post(api_url, json=request, headers=headers)
#     return HttpResponse('success')


def format_phone_number(phone_number):
    if len(str(phone_number)) < 9:
        return 'Phone number too short'
    else:

        r = '254' + str(phone_number)[-9:]
        return r


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {
               "ShortCode": LipanaMpesaPpassword.Business_short_code,
               "ResponseType": "Completed",
               "ValidationURL": "https://536095ee014f.ngrok.io/api/c2b/validation",
               "ConfirmationURL": "https://536095ee014f.ngrok.io/api/c2b/confirmation",
             }
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)




@csrf_exempt
def call_back(request):
    print('__callback__' + request)
    # mpesa_body = request.body.decode('utf-8')
    # mpesa_payment = json.loads(mpesa_body)
    # print(mpesa_payment)
    pass


@csrf_exempt
def validation(request):
    print('__validation__', request)

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    print(request)
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    customer = Customer.objects.filter(user_ptr_id=request.user.id).first()
    cust_reg_ammount = CandidateRegPrice.objects.filter(status='ACTIVE').first()
    curr = CurrencyValue.objects.first()

    # payment = MpesaPayment(
    #     first_name=mpesa_payment['FirstName'],
    #     last_name=mpesa_payment['LastName'],
    #     middle_name=mpesa_payment['MiddleName'],
    #     description=mpesa_payment['TransID'],
    #     phone_number=mpesa_payment['MSISDN'],
    #     amount=mpesa_payment['TransAmount'],
    #     reference=mpesa_payment['BillRefNumber'],
    #     organization_balance=mpesa_payment['OrgAccountBalance'],
    #     type=mpesa_payment['TransactionType'],
    #
    # )
    pay_method = "MPESA"
    payer_reg_no = customer.customer_reg_no
    name = mpesa_payment['FirstName'] + mpesa_payment['LastName'] + mpesa_payment['MiddleName']
    description = mpesa_payment['TransID'],
    expected_amount = cust_reg_ammount.price
    phone_number = mpesa_payment['MSISDN'],
    amount = mpesa_payment['TransAmount'],
    reference = mpesa_payment['BillRefNumber'],
    # if amount >= expected_amount:
    #     payment_status = 'COMPLETED'
    # elif amount < expected_amount:
    #     payment_status = 'PARTIAL'


    organization_balance = mpesa_payment['OrgAccountBalance'],
    type = mpesa_payment['TransactionType'],
    # CustomerPayments.objects.create(
    #     pay_method=pay_method,
    #     payer_reg_no=payer_reg_no,
    #     payer_full_name=name,
    #     amount=amount,
    #     pay_recipt_no=reference,
    #     transaction_recipt_no=reference,
    #     transaction_status='COMPLETED',
    #     payment_status='COMPLETED',
    #     type=type,
    #     description=description,
    #     phone_number=phone_number,
    #     organization_balance=organization_balance,
    # )


    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse(dict(context))