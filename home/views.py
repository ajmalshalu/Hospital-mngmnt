from django.shortcuts import render
# from django.http import  HttpResponse
from . import models

from .forms import BookingForm
def department(request):
    dict_dpt={
        'dept':models.department.objects.all()
    }
    return render(request,'department.html',dict_dpt)

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
         'form': form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors' : models.Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs) 

def contact(request):
    return render(request,'contact.html') 


def saveEnquiry(request):
    if request.method=="POST":
        enq_type=request.POST.get('enq_type')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        country=request.POST.get('country')
        msg=request.POST.get('msg')
        en=Contactenquiry(enq_type=enq_type,c_name=name,c_email=email,c_phone=phone,c_address=address,c_country=country,c_message=msg)
        en.save()
    return render(request,'enquiry.html')      
  
def anaesthesiology(request):
    return render(request,'anaesthesiology.html') 

def arthroscopy(request):
    return render(request,'arthroscopy.html') 

def audiology(request):
    return render(request,'audiology.html') 

def cardiac(request):
    return render(request,'cardiac.html') 

def cardio(request):
    return render(request,'cardio.html') 

def cardiology(request):
    return render(request,'cardiology.html') 

def childcare(request):
    return render(request,'childcare.html') 

def criticalcare(request):
    return render(request,'criticalcare.html')     

