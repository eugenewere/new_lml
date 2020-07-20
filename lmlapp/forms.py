from datetime import date

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from lmlappadmin.models import *
from django import forms


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill','customer','referee_phonenumber', 'referee']





class CompanyUserupdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['email','first_name','last_name','username','logo','company_name', 'company_email', 'company_motto', 'category', 'bizness_entity_type', 'website','bussiness_reg_no','county', 'region','landmark','brief_details', 'date_created', 'description', 'kra_number','phone_number',]

class CompanyOtherDetailForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo','company_name', 'company_email', 'company_motto', 'category', 'bizness_entity_type', 'website','bussiness_reg_no','county', 'region','landmark','brief_details', 'date_created', 'description', 'kra_number']

class CompanySocialsForm(forms.ModelForm):
    class Meta:
        model = CompanySocialAccount
        fields = ['facebook','linkedin', 'googlr_plus', 'instagram', 'twitter', 'company', ]


class CustomerReviewsForm(forms.ModelForm):
    class Meta:
        model = CustomerReviews
        fields = ['customer', 'company', 'ratings', 'message']

class PersonelUpdateForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'profile_image',
            'county',
            'region',
            'country',
            'gender',
            'category',
            'phone_number',
            'date_of_birth',
            'landmark',
            'job_type',
            'marital_status',
            'biography',

        ]
    # def clean_username(self):
    #     super(PersonelUpdateForm, self).clean()
    #     username = self.cleaned_data.get('username')
    #     usernme = self.cleaned_data.get('usernme')
    #     if username == usernme:
    #         return username
    #     elif User.objects.filter(username__iexact=username).exists():
    #         raise forms.ValidationError('Username already exists')
    #     return username
    #
    # def clean_email(self):
    #     super(PersonelUpdateForm, self).clean()
    #     email = self.cleaned_data.get('email')
    #     emailix = self.cleaned_data.get('emailix')
    #     if email ==emailix:
    #         return email
    #     elif User.objects.filter(email__iexact=email).exists():
    #         raise forms.ValidationError('A user has already registered using this email')
    #     return email



    def clean_date_of_birth(self):
        '''
        Only accept users aged 13 and above
        '''
        userAge = 13
        dob = self.cleaned_data.get('date_of_birth')
        today = date.today()
        if (dob.year + userAge, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Users must be aged 18 years old and above.'.format(userAge))
        return dob


class PersonelRegisterForm(forms.Form, UserCreationForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password2',
            'password1',
            'profile_image',
            'county',
            'region',
            'country',
            'gender',
            'category',
            'phone_number',
            'date_of_birth',
            'landmark',
            'job_type',
            'disability',
            'marital_status',
            'biography',
            'disability_status',


        ]


    def clean_username(self):
        super(PersonelRegisterForm, self).clean()
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        super(PersonelRegisterForm, self).clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    def clean_password2(self):
        super(PersonelRegisterForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords must match')
        return password2

    def clean_date_of_birth(self):
        '''
        Only accept users aged 13 and above
        '''
        userAge = 13
        dob = self.cleaned_data.get('date_of_birth')
        today = date.today()
        if (dob.year + userAge, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Users must be aged 18 years old and above.'.format(userAge))
        return dob


class CompanyRegisterForm(forms.Form, UserCreationForm):

    class Meta:
        model = Company
        fields = [
            'email',
            'first_name',
            'last_name',
            'password2',
            'password1',
            'username',
            'logo',
            'company_name',
            'company_email',
            'company_motto',
            'category',
            'bizness_entity_type',
            'website',
            'bussiness_reg_no',
            'county',
            'region',
            'landmark',
            'brief_details',
            'date_created',
            'description',
            'kra_number',
            'phone_number',
        ]

    def clean_username(self):
        super(CompanyRegisterForm, self).clean()
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        super(CompanyRegisterForm, self).clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    def clean_password2(self):
        super(CompanyRegisterForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords must match')
        return password2

