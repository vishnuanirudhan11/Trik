from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model

# Create your views here.
User=get_user_model()

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        e=User.objects.filter(email=username)
        if e.exists():
            user_name=User.objects.get(email=username)
            password=request.POST.get('pass')
            user=auth.authenticate(username=user_name.username,password=password)
            auth.login(request, user)
            if user.is_superuser:
                return redirect('admin_home')
            return redirect('/')
        else:
            password = request.POST.get('pass')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.is_superuser:
                    return redirect('admin_home')
                return redirect('/')
            else:
                msg = 'invalid details'
                return render(request, 'login.html', {'msg': msg})

    msg=''
    return render(request, 'login.html', {'msg':msg})

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        profilephoto=request.FILES['img']
        if password1 != password2:
            a='password is not matching'
            return render(request, 'registration.html', {'k': a})
        elif User.objects.filter(username=username).exists():
            a="username already exist"
            return render(request,'registration.html',{'k':a})
        elif User.objects.filter(email=email).exists():
            a='email id is already exist'
            return render(request,'registration.html',{'k':a})
        elif first_name is None or last_name is None or username is None or len(phone)!=10:
            if len(phone)!=10:
                a="Wrong phone number"
            elif User.objects.filter(phone=phone).exists():
                a="Phone number already exists"
            else:
                a="ALl fields must fill"
            return render(request, 'registration.html', {'k': a})
        else:
            s=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1,
                   email=email, is_staff=gender ,img=profilephoto, phone=phone)
            s.save()
        return redirect('login')
    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')