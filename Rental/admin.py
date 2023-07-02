from django.contrib import admin

# Register your models here.
from Rental.models import *

admin.site.register(Car, carAdmin)
admin.site.register(Client, clientAdmin)
admin.site.register(Reservation, reservationAdmin)
admin.site.register(Marque, marqueAdmin)