#-*- coding: utf-8 -*-
from django.shortcuts import render
from form import RegisterForm

def register(request):
    error=[]
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            password2= data['password2']
            # user = AuthUser()
            try:
                AuthUser.objects.get(username=username)
            except:
                if form.pwd_validate(password, password2):
                    User = AuthUser()
                    User.username = username
                    User.password = make_password(password, None, 'pbkdf2_sha256')
                    User.email = email
                    User.is_superuser = 0
                    User.is_staff = 0
                    User.is_active = 1
                    User.date_joined = datetime.datetime.now()
                    User.save()
                    login_validate(request,username,password)
                    response = HttpResponseRedirect('/account/profile/')
                    response.set_cookie('username',username,3600)
                    return response
                    # return HttpResponseRedirect('/account/profile/')
                else:
                    error.append('请确认二次密码与新密码是否一致！')
            else:
                error.append('该账号已存在！')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form,'error':error})


