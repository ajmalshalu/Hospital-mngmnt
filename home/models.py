from django.db import models

# Create your models here.
class department(models.Model):
    dpt_name = models.CharField(max_length=100)
    dept_decription = models.TextField()

    def __str__(self):
        return self.dpt_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_spec = models.CharField(max_length=50)
    dep_name = models.ForeignKey(department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.doc_name + '-(' + self.doc_spec + ')'

class Booking(models.Model):  
    p_name = models.CharField(max_length=50)
    p_phone = models.CharField(max_length=50) 
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()  
    booked_on =  models.DateField(auto_now=True)

class Contactenquiry(models.Model):
    enq_type=models.CharField(max_length=20)
    c_name=models.CharField(max_length=30)
    c_email=models.EmailField()
    c_phone=models.CharField(max_length=10)
    c_address=models.CharField(max_length=255)
    c_country=models.CharField(max_length=25)
    c_message=models.TextField()   
