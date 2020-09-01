from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberForm,ExtendedUserCreationForm

# Create your views here.


def addmember(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        member_profile = MemberForm(request.POST,request.FILES)
        if form.is_valid() and member_profile.is_valid():
            user = form.save()
            member_profile = member_profile.save(commit=False)
            member_profile.user = user
            member_profile.save()
            context = {'datasave':"Member Created"}
            return render(request, 'index.html', context)
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username,password=password)
            # login(request,user)
            # messages.info(request, 'UserAdded')
            # return HttpResponse ("Data Saved")
    else:
        form = ExtendedUserCreationForm()
        member_profile = MemberForm()


    context = {'form':form, 'member_profile':member_profile}
    return render(request,'addmember.html',context)

def admin_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def logged_in(request):
    context ={}
    return render(request,'index.html',context)

def mylogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect("/")
    else:
        return render(request,'login.html')