
from django.contrib import admin
from django.urls import path
from Rcfapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('fellowships/', views.fellowships, name='fellowships'),
]
 