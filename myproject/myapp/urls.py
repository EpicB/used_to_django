from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('downloads',views.potato,name='potato'),
    path('index',views.start,name="start"),
    path('counter',views.counter,name ="counters"),
    path('static',views.static,name="static"),
    path('static1',views.static1,name="static1"),
    path('model',views.model,name="model")
]