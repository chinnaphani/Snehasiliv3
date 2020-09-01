from django.db import models
from memberprofile.models import MemberProfile
from django.contrib.auth.models import User


# Create your models here.

class MembershipFee(models.Model):
    financeyear = models.CharField(max_length=45)
    monthly_fee = models.IntegerField()
    education_fee = models.IntegerField()
    penal_interest = models.IntegerField()
    dividend = models.IntegerField()
    due_date = models.IntegerField()

    def __str__(self):
        return self.financeyear

def increment_receipt_number():
    last_receipt = Payment_Register.objects.all().order_by('id').last()
    if not last_receipt:
         return 'SN1'
    receipt_no = last_receipt.receipt_no
    receipt_int = int(receipt_no.split('SN')[-1])
    new_receipt_int = receipt_int + 1
    new_receipt_no = 'SN' + str(new_receipt_int)
    return new_receipt_no



class Payment_Register(models.Model):
    receipt_no = models.CharField(max_length=10, default=increment_receipt_number, null=True, blank=True)
    user = models.ForeignKey(User,models.CASCADE)
    date = models.DateField()
    termmonth = models.CharField(max_length=200)
    amt = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.receipt_no


class Subscription(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    is_paid = models.BooleanField(default=False)
    month_term = models.DateField()
    receiptno = models.CharField(max_length=10,default='')














