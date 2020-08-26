from django.db import models

class Location(models.Model):
    management = models.CharField(max_length=30)
    S_address = models.TextField()
    L_address = models.TextField()
    purpose = models.TextField()
    camera_num = models.PositiveIntegerField()
    camera_pixel = models.PositiveIntegerField()
    shoot_info= models.TextField()
    storage_days = models.PositiveIntegerField()
    phone = models.TextField()
    latitude= models.TextField()
    longitude = models.TextField()
    data_date=  models.DateField()
    alarm = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)+"."+self.management
