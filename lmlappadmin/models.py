from html import escape

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import datetime
from io import BytesIO
from PIL import Image
from django.core.files import File

# # Create your models here.
from django.db.models import Count, Q
from django.utils.safestring import mark_safe



def compress(image):
    im = Image.open(image)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class County(models.Model):
    county_number = models.IntegerField(null=False, blank=False)
    county = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.county)


class Region(models.Model):
    county_number = models.IntegerField(null=False, blank=False)
    region = models.CharField(max_length=200, null=False, blank=False)
    ward = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.region)


class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False)
    c_parent = models.ForeignKey('Category', related_name='job_category', on_delete=models.CASCADE, max_length=200,
                                 null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.category)

    @property
    def topcategories(self):
        customers = Customer.objects.filter(category=self)
        categories = []
        category = self

        for customer in customers:
            categories.append(customer.customer_categories)

        return list(set(categories))

    # @property
    # def customer_categories(self):
    #     category = Customer.objects.filter(category=self).annotate(itemcount=Count('id')).order_by('-itemcount')
    #     return category.category.category


class CustomerPayments(models.Model):
    pay_method = models.CharField(max_length=200, null=False, blank=False)

    payer_reg_no = models.CharField(max_length=200, null=True, blank=True)
    payer_full_name = models.CharField(max_length=200, null=True, blank=True)
    payer_paying_email = models.CharField(max_length=200, null=True, blank=True)
    business_email_paid = models.CharField(max_length=200, null=True, blank=True)

    country_code = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=200, null=False, blank=False)

    currency_amount = models.CharField(max_length=200, null=True, blank=True)
    currency_code = models.CharField(max_length=200, null=True, blank=True)
    currency_value = models.CharField(max_length=200, null=True, blank=True)

    pay_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    transaction_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    CUSTOMER_PAYMENT_STATUS = {
        ('UNPAID', 'Unpaid'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
        ('PARTIAL', 'Partial'),
    }
    payment_status = models.CharField(max_length=200, choices=CUSTOMER_PAYMENT_STATUS, default='UNPAYED', null=True, blank=True)
    transaction_status = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.payer_reg_no)

    @property
    def typeofpay(self):
        return 'Registration'

class CandidateRegPrice(models.Model):
    price = models.IntegerField( null=False, blank=False)
    CANDREGPRICE = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    }
    status = models.CharField(choices=CANDREGPRICE, default='INACTIVE', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' % (self.price)

class CompanyRegPrice(models.Model):
    price = models.IntegerField( null=False, blank=False)
    COMPREGPRICE = {
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    }
    status = models.CharField(choices=COMPREGPRICE, default='INACTIVE', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' % (self.price)

class Customer(get_user_model()):
    profile_image = models.ImageField(max_length=200, upload_to='customerImages', null=True, blank=True)
    regpayment = models.ForeignKey(CustomerPayments, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=100, null=False, blank=False)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_of_birth = models.DateField(default=datetime.datetime.now)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    huduma_no = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=200, null=False, blank=False)
    disability = models.TextField(null=True, blank=True)

    marital_status = models.CharField(max_length=100, null=True, blank=True)
    # driver_licence = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    biography = models.TextField()
    PERSONNEL_STATUS = {
        ('NEWBIE', 'Newbie'),
        ('DEACTIVATED', 'Deactivated'),
    }
    status = models.CharField(choices=PERSONNEL_STATUS, default='NEWBIE', max_length=200, null=False, blank=False)
    PAYMENT_STATUS = {
        ('PAID', 'Paid'),
        ('UNPAID', 'UnPaid'),
        ('PARTIAL', 'Partial'),
    }
    pay_status = models.CharField(choices=PAYMENT_STATUS, default='UNPAID', max_length=200, null=False, blank=False)

    RANK_STATUS = {
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ULTIMATE', 'Ultimate'),
    }
    rank_status = models.CharField(choices=RANK_STATUS, default='BASIC', max_length=200, null=False, blank=False)
    DISABILITY_STATUS = [
        ('DISABLED', 'Disabled'),
        ('NOT_DISABLED', 'Not_Disabled')
    ]
    disability_status = models.CharField(choices=DISABILITY_STATUS, default='NOT_DISABLED', max_length=200, null=True,
                                         blank=False)

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.rank_status)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def save(self, *args, **kwargs):
        new_image = compress(self.profile_image)
        self.profile_image = new_image
        super().save(*args, **kwargs)

    @property
    def cus_bio(self):
        data = mark_safe(self.biography)

        # data = mark_safe(self.biography)
        return data

    @property
    def customer_linkedin_social(self):
        social = Social_account.objects.filter(customer=self).first()
        if social:
            return social.account_url
        return False

    @property
    def customer_reg_payment_details(self):
        if self.regpayment:
            return self.regpayment
        else:
            return 'Not Paid'

    @property
    def skillset(self):
        skills = []
        skillz = Skills.objects.filter(customer=self).order_by('?')[:3]
        for skill in skillz:
            skills.append(skill)

        return list(set(skills))

    @property
    def skillcount(self):
        skill = Skills.objects.filter(customer=self).count()
        if skill > 3:
            my_skill = skill - 3
            return my_skill
        else:
            return False

    @property
    def customer_age(self):
        today = datetime.date.today().year
        birth = self.date_of_birth.year
        if birth:
            return int(today - birth)
        else:
            return 0

    @property
    def customer_reg_no(self):
        regno = CustomerRegNo.objects.filter(customer=self).first()
        if regno:
            return regno.personel_reg_no
        else:
            return 'NO_REGNO_ON_THIS_GUY'



class CustomerCvFiles(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    file = models.FileField(upload_to='candidatecv')
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.file.size)


class CustomerRegNo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    personel_reg_no = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.personel_reg_no)


class Education(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    qualifications = models.CharField(max_length=200, null=False, blank=False)
    school = models.CharField(max_length=200, null=False, blank=False)
    course = models.CharField(max_length=200, null=False, blank=False)
    graduation_date = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now())
    reg_number = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.qualifications)


class Experience(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    employer_name = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    comapny_email = models.CharField(max_length=200, null=True, blank=True)
    company_phone = models.CharField(max_length=200, null=True, blank=True)
    position_held = models.CharField(max_length=200, null=True, blank=True)
    date_from = models.DateField(default=datetime.datetime.now)
    date_to = models.DateField(default=datetime.datetime.now)
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.company_name)


class Skills(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    skill = models.CharField(max_length=100, null=False, blank=False)
    referee = models.CharField(max_length=100, null=False, blank=False)
    referee_phonenumber = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s' % (self.skill)


class Social_account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    account_url = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.account_url)


class CompanyRegistrationPayment(models.Model):
    pay_method = models.CharField(max_length=200, null=False, blank=False)

    payer_reg_no = models.CharField(max_length=200, null=True, blank=True)
    payer_full_name = models.CharField(max_length=200, null=True, blank=True)
    payer_paying_email = models.CharField(max_length=200, null=True, blank=True)
    business_email_paid = models.CharField(max_length=200, null=True, blank=True)

    country_code = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=200, null=False, blank=False)

    currency_amount = models.CharField(max_length=200, null=True, blank=True)
    currency_code = models.CharField(max_length=200, null=True, blank=True)
    currency_value = models.CharField(max_length=200, null=True, blank=True)

    pay_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    transaction_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    CUSTOMER_PAYMENT_STATUS = {
        ('UNPAID', 'Unpaid'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
        ('PARTIAL', 'Partial'),
    }
    payment_status = models.CharField(max_length=200, choices=CUSTOMER_PAYMENT_STATUS, default='UNPAYED', null=True,
                                      blank=True)
    transaction_status = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.payer_reg_no)

    @property
    def typeofpay(self):
        return 'Registration'


class Company(get_user_model()):
    logo = models.ImageField(max_length=200, upload_to='employerlogo', null=True, blank=True)
    regpayment = models.ForeignKey(CompanyRegistrationPayment, on_delete=models.SET_NULL, null=True )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True )
    company_name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=200, null=False, blank=False, default='0700000000')
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    landmark = models.CharField(max_length=100, null=False, blank=False)
    company_motto = models.CharField(max_length=100, null=False, blank=False)
    brief_details = models.TextField()
    bizness_entity_type = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateField(default=datetime.datetime.now, null=False, blank=False)
    description = models.TextField()
    website = models.CharField(max_length=100, null=True, blank=True)
    company_email = models.CharField(max_length=100, null=False, blank=False)
    kra_number = models.CharField(max_length=100, null=False, blank=False)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    bussiness_reg_no = models.CharField(max_length=100, null=True, blank=True, unique=True, validators=[alphanumeric])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    COMPANY_STATUS = {
        ('NEWBIE', 'Newbie'),
        ('REGISTERED_CONFIRMED', 'Registerd_confirmed'),
        ('DEACTIVATED', 'Deactivated'),

    }
    status = models.CharField(choices=COMPANY_STATUS, default='NEWBIE', max_length=200, null=False, blank=False)
    RANK_STATUS = {
        ('UNDEFINED', 'Undefined'),
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ULTIMATE', 'Ultimate'),
        ('PRO_BASIC', 'Pro_basic'),
        ('PRO_ULTIMATE', 'Pro_ultimate'),
        ('PLATINUM', 'Platinum'),

    }
    rank_status = models.CharField(choices=RANK_STATUS, default='UNDEFINED', max_length=200, null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def save(self, *args, **kwargs):
        new_image = compress(self.logo)
        self.logo = new_image
        super().save(*args, **kwargs)

    @property
    def reg_payment_details(self):
        if self.regpayment:
            return self.regpayment
        else:
            return 'Not Paid'

    @property
    def companyregno(self):
        reg_no = CompanyRegNo.objects.filter(company=self).first()
        if reg_no:
            return reg_no.company_reg_no
        return 'N/A'


class CompanyRegNo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_reg_no = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.company.company_name, self.company_reg_no)


class CompanyPricingPlan(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField()
    MONTHLY = 0
    YEARLY = 1
    TIME = {
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=TIME, default=MONTHLY)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def _str__(self):
        return '%s  ' % (self.title)

    def companyPD(self):
        return CompanyPricingDetails.objects.filter(pricing_id=self.id).first()


class CompanyPricingDetails(models.Model):
    pricing = models.ForeignKey(CompanyPricingPlan, related_name="companypricingdetails", on_delete=models.CASCADE, null=False, blank=False)
    shortlist_access = models.BooleanField(default=False,null=False, blank=False)
    review_access = models.BooleanField(default=False,null=False, blank=False)
    no_of_candidates = models.CharField(max_length=200, null=False, blank=False)
    chat_with_candidates = models.BooleanField(default=False,null=False, blank=False)
    view_lml_cv = models.BooleanField(default=False,null=False, blank=False)
    view_user_own_cv = models.BooleanField(default=False,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
       return '%s  ' % (self.pricing.title)


class CompanyStatusPayment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL , null=True)
    cpp = models.ForeignKey(CompanyPricingPlan, on_delete=models.SET_NULL , null=True)
    pay_method = models.CharField(max_length=200, null=False, blank=False)

    payer_reg_no = models.CharField(max_length=200, null=True, blank=True)
    payer_full_name = models.CharField(max_length=200, null=True, blank=True)
    payer_paying_email = models.CharField(max_length=200, null=True, blank=True)
    business_email_paid = models.CharField(max_length=200, null=True, blank=True)

    country_code = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=200, null=False, blank=False)

    currency_amount = models.CharField(max_length=200, null=True, blank=True)
    currency_code = models.CharField(max_length=200, null=True, blank=True)
    currency_value = models.CharField(max_length=200, null=True, blank=True)

    pay_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    transaction_recipt_no = models.CharField(max_length=200, null=False, blank=False)
    CUSTOMER_PAYMENT_STATUS = {
        ('UNPAID', 'Unpaid'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
        ('PARTIAL', 'Partial'),
    }
    payment_status = models.CharField(max_length=200, choices=CUSTOMER_PAYMENT_STATUS, default='UNPAYED', null=True, blank=True)
    transaction_status = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.company.company_name)



    @property
    def typeofpay(self):
        p = self.cpp.title
        return str(p)+' Package Subscription'

    @property
    def getexpiry(self):

        monthh_days = 31
        year_days = 365
        exp = self.cpp.status
        created_at = self.created_at
        id = CompanyStatusPayment.objects.filter(company=self.company).order_by('-created_at').first()
        c = CompanyStatusPayment.objects.filter(company=self.company, id=self.id).order_by('-created_at').first()
        if c.id == id.id:
            if exp.upper() == 'MONTHLY':
                expiry_date = created_at.date() + datetime.timedelta(days=monthh_days)
                return expiry_date.strftime("%d-%m-%Y")
            elif exp.upper() == 'YEARLY':
                expiry_date = created_at.date() + datetime.timedelta(days=year_days)
                return expiry_date.strftime("%d-%m-%Y")

        else:
            return 'Inactive'

    @property
    def getexpiryremainingdays(self):
        import datetime
        monthh_days = 31
        year_days = 365
        exp = self.cpp.status
        created_at = self.created_at
        id = CompanyStatusPayment.objects.filter(company=self.company).order_by('-created_at').first()
        c = CompanyStatusPayment.objects.filter(company=self.company, id=self.id).order_by('-created_at').first()
        if c.id == id.id:
            if exp.upper() == 'MONTHLY':
                expiry_date = created_at.date() + datetime.timedelta(days=monthh_days)
                start_date = datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d")
                end_date = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d")
                diff = abs((end_date - start_date).days)
                if diff > 0:
                    return str(diff) + ' Days remaining'
                else:
                    return 'EXPIRED'
            elif exp.upper() == 'YEARLY':
                expiry_date = created_at.date() + datetime.timedelta(days=year_days)
                start_date = datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d")
                end_date = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d")
                diff = abs((end_date - start_date).days)
                if diff > 0:
                    return str(diff) + ' Days remaining'
                else:
                    return 'EXPIRED'
        else:
            return 'Inactive'




class CompanyShortlistCustomers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    SHORTLIST_STATUS = {
        ('SHORTLISTED', 'Shortlisted'),
        ('UNSHORTLISTED', 'Unshortlisted'),
    }
    payment_status = models.CharField(max_length=200, choices=SHORTLIST_STATUS, default='SHORTLISTED', null=False,
                                      blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.company.company_name, self.customer.first_name)
    # def customerShortlist(self, company, customer):


class WhatWeOffer(models.Model):
    icon = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.title, self.description)


class CompanySocialAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    googlr_plus = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.facebook, self.googlr_plus, self.twitter)


class Query(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField()

    QUERYSTATUS = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('TRASH', 'Trash'),

    }
    status = models.CharField(choices=QUERYSTATUS, default='UNREAD', max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.customer, self.status)


class Reply(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    query = models.ForeignKey(Query, on_delete=models.CASCADE, null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.customer)


class Contacts(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s (%s)' % (self.email, self.phone_number, (self.address))


class EmployerPayments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField()
    paid_to = models.CharField(max_length=200, null=True, blank=True)
    paid_date = models.DateField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s (%s) %s' % (self.employer, (self.customer), self.amount)


class ContactUsCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    COMPANYMESSAGECHOICES = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('TRASH', 'Trash'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=COMPANYMESSAGECHOICES, default='UNREAD')

    def _str__(self):
        return '%s (%s) ' % (self.company.company_name, (self.message))


class ContactUsHome(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    HOMEMESSAGECHOICES = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('TRASH', 'Trash'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=HOMEMESSAGECHOICES, default='UNREAD')

    def _str__(self):
        return '%s (%s) ' % (self.name, (self.message))


class ContactUsEmployee(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    EMPLOYEEMESSAGECHOICES = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
        ('TRASH', 'Trash'),
    }
    status = models.CharField(max_length=200, null=True, blank=True, choices=EMPLOYEEMESSAGECHOICES, default='UNREAD')

    def _str__(self):
        return '%s (%s) ' % (self.customer, (self.message))






class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE, null=False, blank=False)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE, null=False, blank=False)
    reply = models.ForeignKey('self', related_name="messagereply", on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=260, null=True, blank=True, default='No Subject')
    file = models.FileField(upload_to='documents')
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    room = models.IntegerField(null=False, blank=False)
    MESSAGE_CHOICES = {
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
    }
    readstatus = models.CharField(max_length=200, null=False, blank=False, choices=MESSAGE_CHOICES, default='UNREAD')
    LABELS = {
        ('PRODUCT', 'Product'),
        ('WORK', 'Work'),
        ('MISC', 'Misc'),
        ('UNDEFINED', 'Undefined'),
    }
    label = models.CharField(max_length=200, null=False, blank=False, choices=LABELS, default='UNDEFINED')

    def _str__(self):
        return '%s  ' % (self.sender)

    def get_replys(self):
        mm = Message.objects.filter(id=self.id).first()
        messages = Message.objects.filter(reply_id=mm.id).all()
        if messages:
            return messages

    @property
    def delstar_status(self):
        d = MsgStatus.objects.filter(message=self).first()
        if d:
            return d.delstar
        else:
            return False


class MsgStatus(models.Model):
    m_user = models.ForeignKey(User, related_name="m_user", on_delete=models.CASCADE, null=False, blank=False)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=False, blank=False)
    DELETE_STAR = {
        ('DELETE', 'Delete'),
        ('STARRED', 'Starred'),
        ('NORMAL', 'Normal'),
    }
    delstar = models.CharField(max_length=200, null=False, blank=False, choices=DELETE_STAR, default='NORMAL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        return '%s  ' % (self.m_user)


class Newsletter(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.email)


class AdvertCarousel(models.Model):
    carousel_image = models.ImageField(upload_to='home_couresel', max_length=250, null=False,
                                       blank=False)  # height_field=None, width_field=None,
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.carousel_image)


class CustomerReviews(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    message = models.TextField()
    ratings = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.company.company_name)
    # def customer_rating_average(self):


class ShortCode(models.Model):
    short_code = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=220, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.short_code)

class CurrencyValue(models.Model):
    currency =  models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.currency)
