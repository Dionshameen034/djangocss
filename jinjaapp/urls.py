from django.urls import path
from jinjaapp import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('About/', views.about, name='About'),
    path('contact/', views.contact, name='Contact')
]
