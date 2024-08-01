from django.urls import path
from . import views

urlpatterns=[
    path('',views.Django_form,name='Django_form'),
    path('Djangoform/',views.PasswordValidation,name='StudentForm'),
]