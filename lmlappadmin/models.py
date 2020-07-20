from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import datetime

# # Create your models here.
from django.db.models import Count, Q


class County(models.Model):
    county_number = models.IntegerField(null=False,blank=False)
    county = models.CharField(max_length=200,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.county)


class Region(models.Model):
    county_number = models.IntegerField(null=False,blank=False)
    region = models.CharField(max_length=200,null=False,blank=False)
    ward = models.CharField(max_length=200,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.region)

class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False)
    c_parent = models.ForeignKey('Category', related_name='job_category', on_delete=models.CASCADE, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.category)

    @property
    def topcategories(self):
        customers = Customer.objects.filter(category=self)
        categories = []
        category =  self

        for customer in customers:
            categories.append(customer.customer_categories)

        return list(set(categories))

    # @property
    # def customer_categories(self):
    #     category = Customer.objects.filter(category=self).annotate(itemcount=Count('id')).order_by('-itemcount')
    #     return category.category.category



class CustomerPayments(models.Model):
    amount = models.FloatField()
    recipt_no = models.CharField(max_length=200, null=False, blank=False)
    CUSTOMER_PAYMENT_STATUS = {
        ('UNPAYED', 'Unpayed'),
        ('PAYED', 'Payed'),
    }
    payment_status = models.CharField(max_length=200, choices=CUSTOMER_PAYMENT_STATUS, default='UNPAYED', null=False,
                                      blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.amount)

class Customer(get_user_model()):
    profile_image = models.ImageField(max_length=200, upload_to='customerImages', null=True, blank=True)
    regpayment = models.ForeignKey(CustomerPayments, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=100,null=False, blank=False)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    gender = models.CharField(max_length=100,null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_of_birth = models.DateField(default=datetime.datetime.now)
    landmark = models.CharField(max_length=100,null=True, blank=True)
    huduma_no = models.CharField(max_length=100,null=True, blank=True)
    job_type = models.CharField(max_length=200, null=False, blank=False)
    disability = models.TextField(null=True, blank=True)

    marital_status = models.CharField(max_length=100,null=True, blank=True)
    # driver_licence = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    biography = models.TextField()
    PERSONNEL_STATUS = {
        ('NEWBIE', 'Newbie'),
        ('REGISTERED_CONFIRMED', 'Registerd_confirmed'),
        ('DEACTIVATED', 'Deactivated'),

    }
    status = models.CharField(choices=PERSONNEL_STATUS, default='NEWBIE', max_length=200, null=False, blank=False)
    RANK_STATUS = {
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ULTIMATE', 'Ultimate'),

    }
    rank_status = models.CharField(choices=RANK_STATUS, default='BASIC', max_length=200, null=False, blank=False)
    DISABILITY_STATUS=[
        ('DISABLED','Disabled'),
        ('NOT_DISABLED','Not_Disabled')
    ]
    disability_status =models.CharField(choices=DISABILITY_STATUS, default='NOT_DISABLED', max_length=200, null=True, blank=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


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
        skill =  Skills.objects.filter(customer=self).count()
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



class CustomerRegNo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    personel_reg_no = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.personel_reg_no)

class Education(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    qualifications=models.CharField(max_length=200,null=False, blank=False)
    school = models.CharField(max_length=200,null=False, blank=False)
    course = models.CharField(max_length=200,null=False, blank=False)
    graduation_date = models.DateTimeField(blank=False, null=False,default=datetime.datetime.now())
    reg_number = models.CharField(max_length=200, null=False,blank=False)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.qualifications)


class Experience(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    employer_name = models.CharField(max_length=200,null=True, blank=True)
    company_name =models.CharField(max_length=200,null=True, blank=True)
    comapny_email = models.CharField(max_length=200,null=True, blank=True)
    company_phone =models.CharField(max_length=200,null=True, blank=True)
    position_held = models.CharField(max_length=200,null=True, blank=True)
    date_from = models.DateField(default=datetime.datetime.now)
    date_to = models.DateField(default=datetime.datetime.now)
    experience = models.TextField()
    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.company_name)

class Skills(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    skill =  models.CharField(max_length=100,null=False, blank=False)
    referee = models.CharField(max_length=100,null=False, blank=False)
    referee_phonenumber = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return '%s' % (self.skill)

class Social_account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    account_url = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.customer.first_name, self.account_url)

class CompanyRegistrationPayment(models.Model):
    recipt_no = models.CharField(max_length=200, null=False, blank=False)
    amount = models.CharField(max_length=200, null=False, blank=False)
    PAYMENT_STATUS = {
        ('UNPAYED', 'Unpayed'),
        ('PAYED', 'Payed'),
    }
    payment_status = models.CharField(max_length=200, choices=PAYMENT_STATUS, default='UNPAYED', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' % (self.recipt_no)

class Company(get_user_model()):
    logo = models.ImageField(max_length=200, upload_to='employerlogo', null=True, blank=True)
    regpayment = models.ForeignKey(CompanyRegistrationPayment, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=200, null=False, blank=False, default='0700000000')
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    landmark = models.CharField(max_length=100,null=False, blank=False)
    company_motto =models.CharField(max_length=100,null=False, blank=False)
    brief_details = models.TextField()
    bizness_entity_type = models.CharField(max_length=100,null=False, blank=False)
    date_created = models.DateField(default=datetime.datetime.now, null=False, blank=False )
    description = models.TextField()
    website = models.CharField(max_length=100,null=True, blank=True)
    company_email = models.CharField(max_length=100,null=False, blank=False)
    kra_number = models.CharField(max_length=100,null=False, blank=False)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    bussiness_reg_no = models.CharField(max_length=100,null=True, blank=True,unique=True, validators=[alphanumeric])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    COMPANY_STATUS ={
        ('NEWBIE','Newbie'),
        ('REGISTERED_CONFIRMED','Registerd_confirmed'),
        ('DEACTIVATED','Deactivated'),

    }
    status = models.CharField( choices=COMPANY_STATUS, default='NEWBIE', max_length=200, null=False, blank=False)
    RANK_STATUS = {
        ('UNDEFINED','Undefined'),
        ('BASIC','Basic'),
        ('PREMIUM', 'Premium'),
        ('ULTIMATE', 'Ultimate'),
        ('PRO_BASIC', 'Pro_basic'),
        ('PRO_ULTIMATE', 'Pro_ultimate'),
        ('PLATINUM', 'Platinum'),


    }
    rank_status = models.CharField( choices=RANK_STATUS, default='UNDEFINED', max_length=200, null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    @property
    def reg_payment_details(self):
        if self.regpayment:
            return self.regpayment
        else:
            return 'Not Paid'

    @property
    def companyregno(self):
        reg_no = CompanyRegNo.objects.filter(company=self).first()
        print(reg_no)
        if reg_no:
            return reg_no.company_reg_no
        return 'N/A'

class CompanyRegNo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_reg_no = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.company.company_name,self.company_reg_no)





class CompanyStatusPayment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recipt_no = models.CharField(max_length=200, null=False, blank=False)
    amount = models.CharField(max_length=200, null=False, blank=False)
    PAYMENT_STATUS = {
        ('UNPAYED', 'Unpayed'),
        ('PAYED', 'Payed'),
    }
    payment_status = models.CharField(max_length=200, choices=PAYMENT_STATUS, default='UNPAYED', null=False,
                                      blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.company.company_name)


class CompanyShortlistCustomers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.company.company_name)






class CompanySocialAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    googlr_plus = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.company.company_name)



class Query(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField()

    QUERYSTATUS = {
        ('READ','Read'),
        ('UNREAD','Unread'),
        ('TRASH', 'Trash'),

    }
    status = models.CharField(choices=QUERYSTATUS, default='UNREAD', max_length=100,null=False, blank=False)
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
    email=models.CharField(max_length=200, null=False, blank=False)
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
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False)
    email = models.CharField(max_length=200,null=False,blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str__(self):
        return '%s (%s) ' % (self.company.company_name, (self.message))

class ContactUsHome(models.Model):

    name = models.CharField(max_length=200,null=False,blank=False)
    email = models.CharField(max_length=200,null=False,blank=False)
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
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False)
    email = models.CharField(max_length=200,null=False,blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str__(self):
        return '%s (%s) ' %(self.customer, (self.message))

class CompanyPricingPlan(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField()

    def _str__(self):
        return '%s  ' %(self.title)



class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE,null=False, blank=False)
     reciever = models.ForeignKey(User, related_name="reciever",on_delete=models.CASCADE, null=False, blank=False)
     msg_content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     room = models.IntegerField(null=False, blank=False)
     MESSAGECHOICES = {
         ('READ', 'Read'),
         ('UNREAD', 'Unread'),
         ('TRASH', 'Trash'),
     }
     status = models.CharField(max_length=200, null=True, blank=True, choices=MESSAGECHOICES, default='UNREAD')
     def _str__(self):
         return '%s  ' % (self.sender)

     # def chat_room_messages(self, sender, receiver):



class Newsletter(models.Model):
    email = models.CharField(max_length=200, null=False, blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.email)

class AdvertCarousel(models.Model):
    carousel_image = models.ImageField(upload_to='home_couresel',max_length=250,null=False, blank=False  ) #height_field=None, width_field=None,
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

