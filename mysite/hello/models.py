from django.db import models


class Hello(models.Model):
    your_name = models.CharField(max_length=10)
