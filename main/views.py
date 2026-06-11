from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

import smtplib


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def resume(request):
    return render(request,'resume.html')

def contact(request):
    return render(request,'contact.html')

def contact(request):
    # DEBUG PRINT 1: Check if the view is being loaded at all
    print(f"--- Contact View Triggered! Method: {request.method} ---")
    
    if request.method == "POST":
        # DEBUG PRINT 2: Check if Django is successfully entering the POST block
        print("--- POST request detected! Extracting data... ---")
        
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        
        print(f"Data received -> Name: {user_name}, Email: {user_email}")

        email_subject = f"Portfolio Message from {user_name}"
        email_body = f"Name: {user_name}\nEmail: {user_email}\n\nMessage:\n{user_message}"

        try:
            print("Attempting to connect to Google SMTP...")
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Mail sent successfully by Django core module!")
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')
            
        except smtplib.SMTPAuthenticationError as auth_err:
            print(f"Google Authentication Failed: {auth_err}")
            messages.error(request, "❌ Mail failed: Check your App Password.")
        except Exception as e:
            print(f"System/Network Error caught: {e}")
            messages.error(request, f"❌ Mail failed due to system error: {e}")

    return render(request, 'contact.html')