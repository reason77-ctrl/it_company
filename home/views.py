from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class BaseView(View):
    views = {}

class HomeView(BaseView):

    def get(self, request):
        self.views['services'] = Service.objects.all()
        self.views['slider'] = Slider.objects.filter(status='active')
        self.views['abouts'] = About.objects.all()
        self.views['techs'] = Techs.objects.all()

        return render(request, 'index.html', self.views)



def contact(request):

    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if len(full_name)<10 or len(email)<10 or len(subject)< 10 or len(message)<20:
            messages.error(request, 'Please fill the form Correctly!')
        else:
            data = Contact.objects.create(
                full_name = full_name,
                email = email,
                subject = subject,
                message = message,
            )
            data.save()
            send_mail(
            subject='Contact form submission',
            message=f"Name: {full_name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECIPIENT,settings.EMAIL_RECIPIENT2],
            fail_silently=False,
            )
            messages.success(request, 'Your Message Has Been Sent.')
        return redirect('home:index')
    return render(request, 'index.html')

def connect_form(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        services = request.POST.get('services')
        message = request.POST['message']
        if len(email)<10 or len(phone)< 10 or len(message)<20:
            messages.error(request, 'Please fill the form Correctly!')
        else:
            data = Connect_Form.objects.create(
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                email = email,
                address = address,
                services = services,
                message = message,
            )
            data.save()
            send_mail(
            subject='Contact form submission',
            message=f"First_Name: {first_name}\nLast_Name: {last_name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nMessage: {message}\nServices: {services}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECIPIENT,settings.EMAIL_RECIPIENT2],
            fail_silently=False,
            )
            messages.success(request, 'Your Message Has Been Sent.')
        return redirect('home:index')
    return render(request, 'index.html')