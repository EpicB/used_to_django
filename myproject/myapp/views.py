from django.shortcuts import render
from django.http import HttpResponse
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
    feature1 = feature()
    feature1.id = 1
    feature1.name = "Yes"
    feature1.details = "yay"

    feature2 = feature()
    feature2.id = 2
    feature2.name = "Yes"
    feature2.details = "yay"

    feature3 = feature()
    feature3.id = 3
    feature3.name = "Yes"
    feature3.details = "yay"

    feature4 = feature()
    feature4.id = 4
    feature4.name = "Yes"
    feature4.details = "yay"
    features = [feature1,feature2,feature3,feature4]
    return render(request,'modelsmaster.html',{"features":features})