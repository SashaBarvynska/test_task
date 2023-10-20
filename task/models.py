from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='members', null=True)
