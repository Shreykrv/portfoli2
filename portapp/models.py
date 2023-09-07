from django.db import models

class portsk(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    
# class dform(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     subject = models.CharField(max_length=100)
#     message = models.CharField(max_length=50)



# Create your models here.
