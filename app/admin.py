from django.contrib import admin
from . models import Appointment, Service, SalonSetting, GalleryImage, Appointment_Status
# Register your models here.


admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(SalonSetting)
admin.site.register(GalleryImage)
admin.site.register(Appointment_Status)