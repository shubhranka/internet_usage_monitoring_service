from django.db import models

class UserUsage(models.Model):

    username = models.CharField(max_length=100)    
    mac_address = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    usage_time = models.DurationField()
    upload = models.BigIntegerField()
    download = models.BigIntegerField()

    class Meta:
        verbose_name = _("UserUsage")
        verbose_name_plural = _("UserUsages")

    def __str__(self):
        return self.name

