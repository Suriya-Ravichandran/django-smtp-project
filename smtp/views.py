from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method =="POST":
        form=ContactForm(request.POST)
        name=request.POST.get("name")
        phone=request.POST.get("phoneno")
        email=request.POST.get("email")
        message_form=request.POST.get("message")

        if form.is_valid():
            sendemail="info@gocosys.com"
            subject="You Got a Enquiry in Website name"
            message=render_to_string("contactmail.html",{
                "name":name,
                "phoneno":phone,
                "email":email,
                "message":message_form
            })
            messages.success(request,"Form submitted successfully")
            send_mail(subject,message,"noreplay@gocosys.com",[sendemail])
            return render(request,"index.html",{"form":form})
        else:
            return render(request,"index.html",{"form":form})
    return render(request,"index.html")