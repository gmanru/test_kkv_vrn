from django.contrib import admin


from .models import Route, Flight, Ticket, Carrier, Autostation

admin.site.register(Route)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Carrier)
admin.site.register(Autostation)

