from django.shortcuts import render
from .forms import CreateList
from .models import List
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if '_user' in request.session:
        user = request.session.get('_user')
        print user
        list_data = List.objects.filter(user=user)

        if 'del' in request.GET:
            print request.GET['del']
            id_num = request.GET['del']
            pardata = List.objects.filter(id=id_num)
            pardata.delete()        

        if 'com' in request.GET:
            print request.GET['com']
            id_num = request.GET['com']
            pardata = List.objects.filter(id=id_num)
            List.objects.filter(id=id_num).update(complete=True)
        
        data = []
        for each in list_data:
            title = each.title
            username = each.user
            content = each.content
            level = each.level
            complete = each.complete
            uid = each.id
            data.append(dict(title=title,username=username,content=content,level=level,id=uid,complete=complete))

        return render(request, 'index.html', {'data':data,'user':user})
    else:
        _user = None
        return render(request, 'index.html', {'user':_user})

    return render(request, 'index.html', {'user':_user})

def register_view(request):
    errors = []
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username:
            errors.append('Please fill username')
            return render(request, 'register.html' ,{'errors':errors})
        if not email:
            errors.append('Please fill eamil')
            return render(request, 'register.html' ,{'errors':errors})
        if not password:
            errors.append('Please fill password')
            return render(request, 'register.html' ,{'errors':errors})
        if User.objects.filter(username=username):
            errors.append('user has been taken')
            return render(request, 'register.html' ,{'errors':errors})
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            print user.is_staff #True
            user.save()
            return redirect(reverse('todolist.views.index' , args=[]))

    return render(request, 'register.html')

def login_view(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['_user'] = username
                return redirect(reverse('todolist.views.index' , args=[]))
            else:
                print 'disabled account'
                return redirect(reverse('todolist.views.index' , args=[]))
        else:
            errors.append('login error,please check username and password')
    return render(request, 'login.html' , {'errors':errors})

def logout_view(request):
    try:
        del request.session['_user']
        print 'logout successed'
    except:
        print 'logout error'

    logout(request)
    return HttpResponseRedirect('/')

@login_required
def create_view(request):
    #form = CreateList()

    if '_user' in request.session:
        user = request.session.get('_user')
    else:
        print 'user error'
        #return 

    if request.method=='POST':
        form = CreateList(request.POST)
        print form.is_valid()
        if form.is_valid():
            form.save()
            print 'save successed'
            return redirect(reverse('todolist.views.index' , args=[]))
            #return render(request,'index.html',{'user':user})

    return render(request, 'create.html' ,{'user':user})

@login_required
def complete(request):
    if '_user' in request.session:
        user = request.session.get('_user')
        print user
        list_data = List.objects.filter(user=user)

        if 'del' in request.GET:
            print request.GET['del']
            id_num = request.GET['del']
            pardata = List.objects.filter(id=id_num)
            pardata.delete()        
        
        data = []
        for each in list_data:
            title = each.title
            username = each.user
            content = each.content
            level = each.level
            complete = each.complete
            uid = each.id
            data.append(dict(title=title,username=username,content=content,level=level,id=uid,complete=complete))

    return render(request, 'complete.html', {'data':data,'user':user})
