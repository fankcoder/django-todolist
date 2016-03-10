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
    print 'index'
    
    if request.method == 'POST':
        print 'post sd'
        if '_user' in request.session:
            user = request.session.get('_user')
        else:
            print 'user error'

        data = List.object.filter(user=user)
        for each in data:
            print each.title
            

    return render(request, 'index.html')
    '''
    form = CreateList()
    
    if request.method=='POST':
        form = CreateList(request.POST)
        if form.is_valid():
            form.save()
            data = List.objects.all()[::-1]
            context = {'form':form,'data':data}
            #for each in  data:
            #    print each.levelist[0]
            return render(request,'index.html',context)

    elif 'del' in request.GET:
        print request.GET['del']
        id_num = request.GET['del']
        List.objects.filter(id=id_num).delete()
        data = List.objects.all()[::-1]
        context = {'data':data}
        return render(request,"index.html",context)

    elif 'create' in request.GET:
        return render(request,"create.html")

    try:
        data = List.objects.all()[::-1]
    except:
        print "there is no data"
    return render(request,'index.html',{'data':data})
    '''
    #return render(request, 'index.html')

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
                #print request.session.get('_user')
                return redirect(reverse('todolist.views.index' , args=[]))
                #return render(request, 'index.html', {'user':username})
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
    form = CreateList()

    if '_user' in request.session:
        user = request.session.get('_user')
    else:
        print 'user error'
        #return 

    if request.method=='POST':
        '''
        username = request.POST.get('user')
        title = request.POST.get('title')
        content = request.POST.get('content')
        level = request.POST.get('level')
        print username,title,content,level
        '''

        form = CreateList(request.POST)
        print form.is_valid()
        if form.is_valid():
            form.save()
            print 'save successed'
            return render(request,'index.html')

    return render(request, 'create.html' ,{'user':user})

