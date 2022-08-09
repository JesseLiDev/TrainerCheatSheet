from django.db import models

class Client(models.Model):
    clientID = models.IntegerField()
    clientFirstName = models.CharField(max_length=30)
    clientLastName = models.CharField(max_length=30)


class trainerLogin(models.Model): 
    trainerUserName = models.CharField(max_length=50)
    trainerPassword = models.CharField(max_length=50)