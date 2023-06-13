from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name= 'index'),
    path('contact', contact, name='contact'),
    path('connect_form', connect_form, name='connect_form'),
]