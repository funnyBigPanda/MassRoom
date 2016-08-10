from django.contrib import admin

# Register your models here.
from massRoom.models import Staff, Service, Record

admin.site.register(Staff)
admin.site.register(Service)
admin.site.register(Record)