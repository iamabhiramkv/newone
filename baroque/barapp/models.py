from django.db import models

# Create your models here.
class userreg(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phn_no = models.IntegerField()
    uname = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class proreg(models.Model):
    barname = models.CharField(max_length=20)
    email = models.EmailField()
    license = models.FileField()
    uname = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    action = models.CharField(max_length=20)
    def __str__(self):
        return self.barname

class login(models.Model):
    uname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    action = models.CharField(max_length=20)
    def __str__(self):
        return self.uname

class tbooking(models.Model):
    name = models.CharField(max_length=20)
    phn_no = models.IntegerField()
    date = models.DateField(default=True)
    time = models.TimeField()
    no_of_people = models.IntegerField()
    comments = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class userfeedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class drinksaddwhis(models.Model):
    brandname = models.CharField(max_length=50)
    variant = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    image = models.FileField()
    def __str__(self):
        return self.brandname

class drinksaddrum(models.Model):
    brandname = models.CharField(max_length=50)
    variant = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    image = models.FileField()
    def __str__(self):
        return self.brandname

class drinksaddvod(models.Model):
    brandname = models.CharField(max_length=50)
    variant = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    image = models.FileField()
    def __str__(self):
        return self.brandname

class foodsaddnon(models.Model):
    foodname = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.CharField(max_length=50)
    def __str__(self):
        return self.foodname

class foodsaddveg(models.Model):
    foodname = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.CharField(max_length=50)
    def __str__(self):
        return self.foodname

class adminmessage(models.Model):
    # uname = models.CharField(max_length=20)
    message = models.CharField(max_length=300)
    def __str__(self):
        return self.message





