from django.db import models


class Navisu(models.Model):
    navisu_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.navisu_text


class Home_item(models.Model):
    hometem_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.hometem_text
    

class Us_item(models.Model):
    ustem_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.ustem_text


class Service_item(models.Model):
    servicetem_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.servicetem_text


class Support_item(models.Model):
    supporttem_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.supporttem_text

# Create your models here.
