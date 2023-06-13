from django.db import models

# Create your models here.

STATUS = (
    ('active', 'active'),
    ('inactive', 'inactive'),
)

class Service(models.Model):
    img = models.ImageField(upload_to = 'media/services')
    title = models.CharField(max_length = 200, blank = True)
    content = models.TextField(blank= True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Slider(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'media/slider')
    status = models.CharField(choices=STATUS, max_length=200)
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class Techs(models.Model):
    name = models.CharField(max_length=100)
    logo_img = models.ImageField(upload_to = 'media/Techs')
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    

class About(models.Model):
    title = models.CharField(max_length=500)
    title_description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    
class Connect_Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=500)
    services = models.CharField(max_length=100)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'