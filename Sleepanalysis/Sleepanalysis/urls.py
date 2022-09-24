from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.nope, name='Home'),
    path('new',views.okay,name='Anything'),
    path("",views.text, name="some name"),
    path('okay',views.average,name="name"),
    path('endpoint',views.index,name="index"),
]
