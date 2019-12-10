from django.contrib import admin

# Register your models here.
from .models import Registration_Model

class Admin_class(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id','phone_number','password','conform_password','qualification']
admin.site.register(Registration_Model,Admin_class)
