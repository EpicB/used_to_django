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