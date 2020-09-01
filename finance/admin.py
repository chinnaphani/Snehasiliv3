from django.contrib import admin
from .models import MembershipFee,Payment_Register,Subscription

# Register your models here.
admin.site.register(MembershipFee)
admin.site.register(Payment_Register)
admin.site.register(Subscription)