from django.shortcuts import render
from .forms import CreateList
from .models import List
from django.contrib.auth.models import User

# Create your views here.
def index(request):
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

def register(request):
    errors = []
    if request.method == "POST":
        username = request.POST.get('username',)
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
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
