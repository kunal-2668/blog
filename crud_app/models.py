from django.db import models

# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField(max_length=150)
    rtime = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=40)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField(max_length=10000)
    upload_by = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    item = models.CharField(max_length=1000)

    def __str__(self):
        return self.item