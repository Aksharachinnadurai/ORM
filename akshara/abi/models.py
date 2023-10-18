


from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    no_of_teams=models.IntegerField()
    no_of_goals=models.IntegerField()
    score=models.IntegerField()
class FootballAdmin(admin.ModelAdmin):
    list_display=["name","dob","age","no_of_teams","no_of_goals","score"]

     
