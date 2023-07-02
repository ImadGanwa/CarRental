import datetime

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone

class Marque(models.Model):
    nom = models.CharField(max_length=30, verbose_name="Nom marque")

    class Meta:
        verbose_name = "Marque"

    def __str__(self):
        return str(self.nom)

class marqueAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    ordering = ['nom']
    search_fields = ["nom"]


class Car(models.Model):
    carburant_choices = [
        ('Diesel', 'Diesel'),
        ('Essence', 'Essence')]

    transmission_choices = [
        ('Automatique', 'Automatique'),
        ('Manuelle', 'Manuelle')]

    matricule = models.IntegerField(verbose_name="Matricule")
    image = models.ImageField(verbose_name="Image", upload_to="static/images", default="static/default_image.jpg")
    marque = models.ForeignKey('Marque', null=True, on_delete=models.CASCADE, verbose_name="Marque")
    modele = models.CharField(max_length=20, verbose_name="Modele")
    annee = models.IntegerField(verbose_name="Annee")
    nbrPersonne = models.IntegerField(verbose_name="Nombre de Personnes")
    nbrPortes = models.IntegerField(verbose_name="Nombre de Portes")
    carburant = models.CharField(max_length=20, verbose_name="Carburant", choices=carburant_choices)
    transmission = models.CharField(max_length=20, verbose_name="Transmission", choices=transmission_choices)
    couleur = models.CharField(max_length=20, verbose_name="Couleur")
    consommation = models.IntegerField(verbose_name="Consommation (KM/L)")
    gps = models.BooleanField(default=True, verbose_name="GPS Availability")
    prix = models.IntegerField(verbose_name="Prix par jour(DH)")
    availability = models.BooleanField(default=True, verbose_name="Availability")
    description = models.TextField(max_length=1500, verbose_name="Description", null=True)

    class Meta:
        verbose_name = "Car"

    def __str__(self):
        return str(self.couleur) + " " + str(self.marque) + " " + str(self.modele)


class carAdmin(admin.ModelAdmin):
    list_display = (
    "matricule", "marque", "modele", "annee", "nbrPersonne", "nbrPortes", "carburant", "transmission", "couleur", "consommation", "gps",
    "prix", "availability")
    search_fields = ["matricule", "marque", "modele"]
    list_filter = (
    "availability", "marque", "modele", "annee", "nbrPersonne", "nbrPortes", "carburant", "transmission", "couleur",
    "prix", "consommation", "gps")
    ordering = ("matricule", "marque", "modele", "consommation")


class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cin = models.CharField(max_length=10, verbose_name="CIN")
    tel = models.CharField(max_length=10, verbose_name="Telephone")
    dateN = models.DateField(verbose_name="Date de naissance")

    class Meta:
        verbose_name = "Client"

    def __str__(self):
        return str(self.user)


class clientAdmin(admin.ModelAdmin):
    list_display = ("user", "cin", "tel", "dateN")
    ordering = ['user']
    search_fields = ("user", "cin", "tel", "dateN")


class Reservation(models.Model):
    client = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', null=True, on_delete=models.CASCADE, verbose_name="Rented Car")
    dateD = models.DateField(verbose_name="Pick-Up")
    dateF = models.DateField(verbose_name="Drop-Off")
    price = models.IntegerField(verbose_name="Prix Total", null=True)

    class Meta:
        verbose_name = "Reservation"

    def __str__(self):
        return str(self.client)

class reservationAdmin(admin.ModelAdmin):
    list_display = ("client", "car", "dateD", "dateF", "price")
    ordering = ['client']
    search_fields = ["client", "car", "dateD", "dateF"]
    list_filter = ('car', 'dateD', 'dateF')