from django.db import models


class Scheduling(models.Model):
    date_time = models.DateTimeField()
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
