from django.contrib import admin
from .models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'password')

admin.site.register(Fcuser, FcuserAdmin)


