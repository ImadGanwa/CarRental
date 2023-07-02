from datetime import date, datetime

from django.contrib.auth.decorators import login_required

from Rental.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Rental.models import *
from django.contrib.auth.models import User



# Create your views here.
from Rental.forms import createUserForm


def loginPage(request):
    if request.method == 'POST':
        us = request.POST.get('username')
        ps = request.POST.get('password')

        user = authenticate(request, username=us, password=ps)
        if user is not None:
            login(request, user)
            if not request.user.first_name:
                return redirect('userinfo')
            else:
                return redirect('home')
        else:
            messages.error(request, "Login or password is incorrect, try again.. or create an account")
    return render(request, "Login/login.html", locals())

def registerPage(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, 'Try again')
    return render(request, "Login/register.html", {'form': form})

def homePage(request):
    cars = Car.objects.all()
    usr = request.user
    return render(request, "Home/home.html", locals())



def carPage(request):
    cars = Car.objects.all()
    usr = request.user
    return render(request, "Home/car.html", locals())


def detailPage(request, pk):
    car = Car.objects.filter(id=pk)
    usr = request.user
    if request.method == 'POST':
        dateD = request.POST.get('dateD')
        dateF = request.POST.get('dateF')
        if Car.objects.get(id=pk).availability == True:
            return redirect("booking/" + pk)
        else:
            messages.error(request, 'This car isn`t available at this date')
    #related_cars = Car.objects.filter(Car.marque)
    return render(request, "Home/detail.html", locals())



def userInfoPage(request):
    form = completeUserForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            usr = request.user
            usr.first_name = request.POST.get('firstName')
            usr.last_name = request.POST.get('lastName')
            usr.save()
            form.save(commit=False)
            client= Client.objects.create(user=request.user, cin=request.POST.get('cin'), tel=request.POST.get('tel'), dateN=request.POST.get('dateN'))
            client.save()
            return redirect("home")
    else:
        return redirect("login")
    return render(request, "Home/userInfo.html", locals())


@login_required
def bookingPage(request, pk):
    car = Car.objects.filter(id=pk)
    usr = request.user
    form = reservationForm()
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            if Car.objects.get(id=pk).availability == True:
                form.save(commit=False)
                Res = Reservation.objects.create(client=request.user, car_id=pk, dateD=request.POST.get('dateD'), dateF=request.POST.get('dateF'))
                Res.save()
                Rs = Reservation.objects.get(car_id=pk, client=request.user)
                Rs.price = (Rs.dateF - Rs.dateD).days * Car.objects.get(id=pk).prix
                Rs.save()
                cr = Car.objects.get(id=pk)
                cr.availability = False
                cr.save()
                return redirect('reservations')
            else:
                messages.error(request, 'This car isn`t available at the moment')
    if Car.objects.get(id=pk).availability == True:
        return render(request, "Home/booking.html", locals())
    else:
        return redirect('detail/' + pk)


@login_required
def allReservationsPage(request):
    resv = Reservation.objects.filter(client=request.user)
    usr = request.user
    return render(request, "Reservation/allReservations.html", locals())


@login_required
def deleteReservationPage(request, pk):
    usr = request.user
    if request.method == 'POST':
        re = Reservation.objects.get(client=request.user, car_id=pk)
        re.delete()
        cr = Car.objects.get(id=pk)
        cr.availability = True
        cr.save()
        return redirect('reservations')
    return render(request, "Reservation/deleteReservation.html", locals())


