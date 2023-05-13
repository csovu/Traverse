from django.db import models
from datetime import date
from django.contrib.auth import get_user_model


class Posts(models.Model):
    trip_title = models.CharField(max_length=50, blank=False) 
    trip_summery = models.CharField(max_length=2000, blank=False)
    trail_conditions = models.CharField(max_length=2000, null=True, blank=True)
    planning_info = models.CharField(max_length=2000, null=True, blank=True)
    other_details = models.CharField(max_length=2000, null=True, blank=True)
    date_posted = models.DateField(default=date.today)
    last_edited = models.DateTimeField(null=True, auto_now=True)
    location= models.CharField(max_length=100, null=True, blank=True)
    map_details = models.URLField(max_length=300, null=True, blank=True) 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title