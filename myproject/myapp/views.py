from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request,'static.html')
def static1(request):
    return render(request,'static1.html')