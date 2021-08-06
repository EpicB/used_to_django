from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature
# Create your views here.
def index(request):
    return HttpResponse('<h1>Potato</h1>')
def potato(request):
    return HttpResponse('<h1>hahah you are in potato land</h1>')
def start(request):
    context = {
        'name':'Potato',
        'location':'africa',
        'sells':'shawrma'
    }
    return render(request,'index.html',context)
def counter(request):
    words = len(request.POST["words"].split(' '))
    return render(request,'counter.html',{'words': words})
def static(request):
    feature1 = feature()
    feature1.id = 1
    feature1.name = "Yes"
    feature1.details = "yay"
    return render(request,'static.html',{"feature1":feature1})
def static1(request):
    return render(request,'static1.html')
def model(request):
    features = feature.objects.all()
    return render(request,'modelsmaster.html',{"features":features})
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"this email has been already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"this name has been already used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"the {} are not the same".format(password))
    return render(request,'register.html')
def test(request):
    
    if "white" in request.POST:
        name = "white"
        return render(request,'test.html',{"name":name})
    elif "black" in request.POST: 
        name = "black"
        return render(request,'test.html',{"name":name})
    else:
        name = "white"
        return render(request,'test.html',{"name":name})
