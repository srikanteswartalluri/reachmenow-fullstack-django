from django.db import models

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  subject = models.CharField(max_length=1000)
  message = models.CharField(max_length=9999999)

  def __str__(self):
      return self.message
  