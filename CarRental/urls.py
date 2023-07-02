"""CarRental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.contrib import admin
from django.urls import path, include

from Rental.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view=homePage, name="home"),
    url('home', view=homePage, name="home"),
    url('login', include("django.contrib.auth.urls")),
    url('login', view=loginPage, name="login"),
    url('register', view=registerPage, name="register"),
    url(r'booking/(?P<pk>\d+)', view=bookingPage, name="booking"),
    url('car', view=carPage, name="car"),
    url(r'detail/(?P<pk>\d+)', view=detailPage, name="detail"),
    url('userinfo', view=userInfoPage, name="userinfo"),
    url(r'delreservation/(?P<pk>\d+)', view=deleteReservationPage, name="delReservation"),
    url('reservations', view=allReservationsPage, name="reservations"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
