from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User



from .models import Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError, transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import AppointmentForm, ServiceForm,  GalleryImageForm
from .models import Appointment, Service, GalleryImage, SalonSetting
from .sms import send_booking_sms

@login_required
def salon_setting():
    obj = SalonSetting.objects.first()
    if not obj:
        obj = SalonSetting.objects.create()
    return obj



def home(request):
    return render(request, "home.html", {
    "services": Service.objects.filter,
    "gallery": GalleryImage.objects.all()[:12],
    "settings": SalonSetting(),
    "form": AppointmentForm(),
})




def book_appointment(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
        
    if request.method == "POST":


        form = AppointmentForm(request.POST)

        if form.is_valid():

            # Save appointment
            appointment = form.save()

            # ==========================================
            # SEND SMS TO SALON OWNER
            # ==========================================

            sms_sent, sms_response = send_booking_sms(
                appointment
            )

            if sms_sent:

                messages.success(
                    request,
                    "Your appointment has been "
                    "booked successfully."
                )

                print(
                    "Appointment SMS sent successfully."
                )

            else:

                messages.warning(
                    request,
                    "Your appointment was saved, "
                    "but the salon notification "
                    "could not be sent."
                )

                print(
                    "SMS failed:",
                    sms_response
                )

            return redirect(
                "book_appointment",
                
            )

    else:

        form = AppointmentForm()

    return render(
        request,
        "booking.html",
        {
            "form": form
        }
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successful')
            
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')
            return redirect('home')  # FIXED - was 'user'
        else:
            messages.error(request, "There was error")
            return redirect("login_view")
    else:
        return render(request, 'login_view.html', {})

def logout_view(request):
    logout(request)
    return redirect('login_view');


def register(request):
    # If user already logged in, don't show register
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/admin/')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # validation
        if password1 != password2:
            messages.error(request, "Passwords don't match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        # create user
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password1,
            first_name=first_name,
            last_name=last_name
            

        )
        user.save()
        
        messages.success(request, "Account created! You are now logged in")
        login(request, user)  # auto login after register
        return redirect('home')

    return render(request, 'register.html')


def gallery(request):
    return render(request, 'gallery.html')