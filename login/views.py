
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login as user_login
from django.contrib import messages
from django.contrib.auth.models import User
from Hotels.models import Company

def login(request):        
    return render(request, 'login.html')

def signin(request):
    
        LOGINuser = request.POST.get('LOGINuser')
        LOGINpass = request.POST.get('LOGINpass')

        userinfo = authenticate(username=LOGINuser , password=LOGINpass)

        if userinfo != None:
            user_login(request, userinfo)
            return redirect('/')
            
        else:
            messages.error(request, "Incorrect user or password")
            return redirect('/login') 

def signup(request):

    if request.method == "POST":

        email       = request.POST.get('email')
        password    = request.POST.get('pass')
        confirmation = request.POST.get('cpass')
        username    = request.POST.get('user')
        fname       = request.POST.get('fname')
        lname       = request.POST.get('lname')


        if password != confirmation:
            messages.error(request, "Passwords don't match, please check them")
            return redirect('/login') 

        elif User.objects.filter(email=email).first() != None:
            messages.error(request, "Email already on use, select another or log in")
            return redirect('/login') 
        
        elif User.objects.filter(username=username).first() != None:
            messages.error(request, "Username already on use, please select another Username")            
            return redirect('/login') 

        else:
            newuser = User.objects.create_user(username, email, password)
            newuser.first_name = fname
            newuser.last_name = lname
            newuser.save()
            messages.error(request, "User created! you may now log in to your account")

    return redirect('/login')

def signout(request):
    logout(request)
    return redirect('/')

def companylogin(request):
    return render(request, 'companylogin.html')

def companysignup(request):

    email        = request.POST.get('email')
    password     = request.POST.get('pass')
    confirmation = request.POST.get('cpass')
    username     = request.POST.get('user')

    if password != confirmation:
        messages.error(request, "Passwords don't match, please check them")
        return redirect('/login') 

    elif User.objects.filter(email=email).first() != None:
        messages.error(request, "Email already on use, select another or log in")
        return redirect('/login') 
        
    elif User.objects.filter(username=username).first() != None:
        messages.error(request, "A company with this name has already registered")            
        return redirect('/login') 

    else:
        newuser = User.objects.create_user(username, email, password)
        newuser.is_staff = True
        newuser.save()
        newuser.company_set.create(name=username)
        messages.error(request, "Company created! you may now log in to the company account")

    return render(request, 'companylogin.html')
