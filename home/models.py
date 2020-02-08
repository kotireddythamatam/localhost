from django.db import models

# Create your models here.
class Registration_Model(models.Model):
    STATUS_TYPE = ((0,'user'),(1,'manager'))
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
    status = models.SmallIntegerField(choices=STATUS_TYPE,default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.first_name

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_photos')

class Student_Education_Details(models.Model):
    course_name = models.CharField(max_length=64)
    college_name = models.CharField(max_length=64)
    percentage = models.CharField(max_length=64)
    passedout_year = models.DateField()

    def __str__(self):
        return self.college_name
