from .models import Payment_Register
from django import forms
import fiscalyear
import datetime
import calendar


class ReceiptFirstForm(forms.ModelForm):
    class Meta:
        model =Payment_Register
        fields = '__all__'


MONTH_CHOICE = [('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')]
months_str = calendar.month_name
# for x in months_str:
#     tes = (x,x)
#     bal_month_choices.append(tes)
#     print(x)
#
# print(bal_month_choices)

YEAR_CHOICES = [(y,y) for y in range(1968, datetime.date.today().year+1)]
# MONTH_CHOICE = [(m,m) for m in months_str]



# class ReceiptForm(ReceiptFirstForm):
#     termmonth = forms.MultipleChoiceField(required=False,
#                 widget=forms.CheckboxSelectMultiple,
#                 choices=MONTH_CHOICE)
#
#     class Meta:
#         model=Payment_Register
#         fields = '__all__'


class ReceiptForm(ReceiptFirstForm):
    termmonth = forms.MultipleChoiceField(choices=MONTH_CHOICE,
                  widget=forms.CheckboxSelectMultiple)

    class Meta:
        model=Payment_Register
        fields = '__all__'