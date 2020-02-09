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

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_photos')

class Student_Education_Details(models.Model):
    course_name = models.CharField(max_length=64)
    college_name = models.CharField(max_length=64)
    percentage = models.CharField(max_length=64)
    passedout_year = models.DateField()

    def __str__(self):
        return self.college_name

class Comments(models.Model):
    COMMENT_CATEGORY =((1,'Home'),(2,'Python'),(3,'Django'),(4,'Restapi'),(5,'HTML'),(6,'CSS'),(7,'JS'),(8,'Bootstrap'),(9,'Mysql'),(9,'Mongodb'))
    comment = models.TextField(max_length=10000)
    like = models.IntegerField(default=0)
    comment_category = models.SmallIntegerField(choices=COMMENT_CATEGORY)
    user = models.ForeignKey(Registration_Model,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    dislike = models.IntegerField(default=0)
    reply_comment = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.comment


