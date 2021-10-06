from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Userinfo
from django.http import JsonResponse


def formView(request):
   if request.session.get('username'):
      username = request.session['username']
      return redirect(display)
   else:
      return render(request, 'login.html')

def user_login(request):
 
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            request.session['username'] = username
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            return JsonResponse(
                {'success':False},
                safe=False
            )

    return render(request,'login.html')


def signup(request):

        if request.method == 'POST':
            first_name  = request.POST['first_name']
            last_name   = request.POST['last_name']
            username    = request.POST['username']
            email_id    = request.POST['email']
            password_1  = request.POST['password1']
            password_2  = request.POST['password2']

            if password_1 == password_2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username taken')
                    return redirect(signup)
                elif User.objects.filter(email=email_id).exists():
                   messages.info(request,'Email taken')
                   return redirect(signup)
                else:
                   user = User.objects.create_user(username=username,password=password_1,email=email_id,first_name=first_name,last_name=last_name)
                   user.save();
                   return redirect(user_login)
               
            else:
                messages.info(request,'password not matching')
                return redirect(user_login)
            return redirect(signup)
        else:
            return render(request,'signup.html')


def display(request):   
    if request.session.get('username'):
        username = request.session['username']
        users = Userinfo.objects.all()
        return render(request,'display.html',{'login':True,'username':username,'users':users})
    else:
        return redirect(login)


def add_donor(request):
    if request.session.get('username'):
        username = request.session['username'] 
        if request.method == 'POST':
            name = (request.POST['name'])
            blood_group = (request.POST['blood_group'])
            phone = (request.POST['phone_no'])
            place = (request.POST['place'])


            users = Userinfo.objects.create(name=name,blood_group=blood_group,phone_number=phone,place=place)
            return redirect(display)

        else:
            return render(request,'add_donor.html',{'login':True,'username':username})
    else:
        return redirect(login)


def logout(request):
    try:
        del request.session['username']
        return redirect(formView)
    except:
        pass





