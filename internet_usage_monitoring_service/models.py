from django.db import models

# User Model
class User(models.Model):
    username = models.CharField(max_length=100)

# User Usage Model
class UserUsage(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)   
    mac_address = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    usage_time = models.DurationField()
    upload = models.BigIntegerField()
    download = models.BigIntegerField()

