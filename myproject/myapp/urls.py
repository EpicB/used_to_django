from django.urls import path
from . import views

urlpatterns = {
    path('',views.index,name='index'),
    path('downloads',views.potato,name='potato'),
    path('index',views.start,name="start")
}