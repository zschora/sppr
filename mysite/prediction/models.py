from django.db import models

# Create your models here.
class Artist(models.Model):
  Artist_id = models.PositiveIntegerField()
  Artist_name = models.CharField('Имя исполнителя', max_length=255)

class User(models.Model):
  User_id = models.PositiveIntegerField()
  Artist_id = models.PositiveIntegerField()
  Scrobbles = models.PositiveIntegerField()