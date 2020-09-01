from django.shortcuts import render, redirect, HttpResponse
from .forms import ReceiptFirstForm,ReceiptForm
from memberprofile.models import MemberProfile


def payment_receipt_view(request):
    if request.method == 'POST':
        payment_form = ReceiptForm(request.POST)
        if payment_form.is_valid():
            print(request.POST.get('termmonth'))
            # user = MemberProfile.objects.get(id=request.user.id)
            termmonth = request.POST.get('termmonth')
            MemberProfile.objects.update(monthsub_paiddate=termmonth)
            payment_form.save()
            # print(user)
            return redirect('payment')
    else:
        payment_form = ReceiptForm()

    context = {'form':payment_form}

    return render(request,'payment_form.html',context)

# Create your views here.





