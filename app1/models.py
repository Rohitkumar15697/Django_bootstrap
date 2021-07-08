from django.db import models

class ShowData(models.Model):
    name=models.CharField(max_length=100)