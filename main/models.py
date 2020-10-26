from django.db import models
from datetime import datetime

# Create your models here.


class Homepage(models.Model):
    what_i_do = models.CharField(max_length=500)

    def __str__(self):
        return "Homepage"

class Skills(models.Model):
    CHOICES = (
        ('LANGUAGES', 'Languages'),
        ('FRAMEWORKS_AND_LIBRARIES', 'Frameworks & libraries'),
        ('DATABASE', 'Database'),
        ('OTHER_TECHNOLOGIES', 'Other Technologies')
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='skills')
    timestamp = models.DateField(default=datetime.now)
    category = models.CharField(max_length=255, choices=CHOICES)
    
    def __str__(self):
        return self.title