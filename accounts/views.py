from django.shortcuts import render,redirect
from .forms import LoginForm
from .models import Signup,UserProfile
from .forms import SignupForm,UserprofileForm

from django.contrib import messages
# Create your views here.
def login(request):
    vv =Signup.objects.count()
    if request.session.get('email'):
        return redirect('profile')
    form =LoginForm(request.POST or None)
    if form.is_valid():
        a=request.POST.get('email1')
        b=request.POST.get('password1')
        # form.cleaned_data.get('email1')

        # print(a,b)
        s=Signup.objects.filter(email=a,password=b)
        if s:
            print('data match')

            request.session['email']=a

            return redirect('profile')

        else:
            print('Invalid email and Password')
            messages.error(request, 'Invalid email and Password.')

    context ={
        'vv':vv,
        'form':form
    }
    return render(request,'login.html',context)


def home(request):
    name=request.session.get('em')
    context = {
        'name': name
    }
    return render(request,'home.html',context)
import random
def signup(request):
    myform =SignupForm(request.POST or None)
    if myform.is_valid():
        username =myform.cleaned_data.get('username')
        email =myform.cleaned_data.get('email')
        password =myform.cleaned_data.get('password')
        mobile =myform.cleaned_data.get('mobile')

        request.session['username']=username
        request.session['email']=email
        request.session['password']=password
        request.session['mobile']=mobile

        otp =random.randrange(1111,9999)
        request.session['otp']=otp
        return render(request,'verify.html',{'otp':otp})

        # myform.save()
        # return redirect('login')

    if 'otpv' in request.POST:
        uotp = request.POST.get('uotp')
        otp1 = request.session.get('otp')

        if int(uotp) == int(otp1):
            print('otp match')
            s=Signup()
            s.username=request.session.get('username')
            s.email=request.session.get('email')
            s.password=request.session.get('password')
            s.mobile=request.session.get('mobile')
            s.save()
            return redirect('login')



        else:
            return render(request, 'verify.html')
    context={
        'form':myform
    }
    return render(request,'signup.html',context)


def profile(request):
    if not request.session.get('email'):
        return redirect('login')
    b=request.session.get('email')
    u =Signup.objects.get(email=b)


    upro =UserProfile.objects.get(user=u)

    context ={
        'u':u,
        'upro':upro
    }
    return render(request,'profile.html',context)

def mylogout(request):
    del request.session['email']
    return redirect('login')

def edit_profile(request):
    get_email =request.session.get('email')
    s_obj =Signup.objects.get(email=get_email)
    p_obj = UserProfile.objects.get(user=s_obj)

    form =UserprofileForm(request.POST or None, request.FILES or None,instance=p_obj)
    if form.is_valid():
        form.save()
        return redirect('profile')



    context = {
        'form':form
    }
    return render(request, 'epro.html', context)

def ind(request):
    return render(request, 'ind.html')

def aaa(request):
    return render(request, 'a.html')