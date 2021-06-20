from django.contrib import admin
from .models import Airport, Flight,Passenger
# Register your models here.
# Indicamos  que podemos editar estos datos
#StackedInline nos permite añadir relacion con otros objetos
#PassengerInline Representa la interfaz de administracion donde me gustaria poder agregar y modificar pasajeros
#la palabra through es la tabla de relacion intermedia entre Passenger y flights
#extra significa que me permita agregar en este caso un pasajero a la vez
class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra =1
#FlightAdmin estoy diciendo que quiero agregar esta seccion adicional en linea de la pagina de admin
class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)
