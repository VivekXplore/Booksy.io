from django.shortcuts import render,redirect ,HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.forms import forms
from .models import Feedback
from .forms import  signinform

# Create your views here.
def home(request):
    return render(request,'home.html')

def plan(request):
    # Check if user is authenticated and get their username (or email)
    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'plan.html', {'user_name': user_name})


def blog(request):
    return render(request,'blog.html')

from django.contrib.auth import get_user_model

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check for user by email
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = None

        if user and user.check_password(password):
            messages.success(request, "Login successful")
            login(request, user)
            return redirect('plan')  # Redirect to a valid page
        else:
            messages.error(request, "Invalid email or password!")  # Error message
    
    return render(request, 'login.html')

import random
from django.conf import settings
from django.core.mail import send_mail


       



 

def signin(request):
    if request.method == 'POST':
        form = signinform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST['email']  

              
            user.username = user.email  
            user.save()

            messages.success(request, "You have successfully signed up!")

            # Authenticate user with email and password
            user = authenticate(request, username=user.email, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('plan')
            else:
                messages.error(request, "Authentication failed.")
        else:
            messages.error(request, "There was an error with your sign-up form.")
    else:
        form = signinform()

    return render(request, 'signup.html', {'form': form})




def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')


def feedback(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        suggestion=request.POST.get('suggestion')

        Feedback.objects.create(name=name, email=email, suggestion=suggestion)
        messages.success(request,"Thank You for your feedback ! we will get to you ASAP.")
        
    return render(request,'feedback.html')


def payment(request):
    return render(request,'payment.html')


def booking(request):
    if not request.user.is_authenticated:
        messages.warning(request,"You have to login before making booking! ")
        return redirect('login')
    return render(request, 'booking.html')

from django.http import JsonResponse
from .models import Booking

def get_available_slots(request, event_type, date):
    all_slots = ['9:00 AM - 12:00 PM', '1:00 PM - 4:00 PM', '5:00 PM - 8:00 PM']
    booked_slots = Booking.objects.filter(event_type=event_type, date=date).values_list('time_slot', flat=True)
    available_slots = [slot for slot in all_slots if slot not in booked_slots]
    return JsonResponse({'available_slots': available_slots})

import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = 'your-openai-api-key'  # Use environment variables in production

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Answer concisely and professionally."},
                    {"role": "user", "content": user_message}
                ]
            )
            answer = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(e)
            answer = "There was an error with the AI service. Try again later."

        return JsonResponse({'response': answer})

    return render(request, 'chatbot.html')
