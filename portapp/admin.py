from django.contrib import admin
from.models import portsk
#from .models import dform

admin.site.register(portsk)
#admin.site.register(dform)

class port(admin.ModelAdmin):
    list_display = ('id', 'name','mail','subject','message')

#class dformAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'name','email','subject','message')


# Register your models here.
