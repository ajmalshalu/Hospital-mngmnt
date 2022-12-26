from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('saveenquiry',views.saveEnquiry,name='saveenquiry'),
    path('anaesthesiology',views.anaesthesiology,name='anaesthesiology'),
    path('arthroscopy',views.arthroscopy,name='arthroscopy'),
    path('audiology',views.audiology,name='audiology'),
    path('cardiac',views.cardiac,name='cardiac'),
    path('cardio',views.cardio,name='cardio'),
    path('cardiology',views.cardiology,name='cardiology'),
    path('childcare',views.childcare,name='childcare'),
    path('criticalcare',views.criticalcare,name='criticalcare'),
]