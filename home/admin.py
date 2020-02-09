from django.contrib import admin

# Register your models here.
from .models import Registration_Model, Profile,Student_Education_Details,Comments

class Admin_class(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email_id','phone_number','password','conform_password','status','qualification']
admin.site.register(Registration_Model,Admin_class)
admin.site.register(Profile)
admin.site.register(Student_Education_Details)
admin.site.register(Comments)
