from django.urls import path, include
from personal import views

urlpatterns = [
    path('',views.index, name='index'),
    path('analyse',views.analyse, name='analyse'),
    path('contact_us',views.contact_us, name='contact_us'),
    
]

