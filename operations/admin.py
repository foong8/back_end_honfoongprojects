from django.contrib import admin
from .models import Country, Assignment, Qcticket, Qclog, QcLogNote

admin.site.register(Country)
admin.site.register(Assignment)
admin.site.register(Qcticket)
admin.site.register(Qclog)
admin.site.register(QcLogNote)