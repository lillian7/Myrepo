from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    age = models.PositiveIntegerField()

    def __unicode__(self):
        return self.user.first_name