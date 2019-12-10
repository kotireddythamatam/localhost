from django.db import models

# Create your models here.
class Registration_Model(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_id = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=15)
    conform_password = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
