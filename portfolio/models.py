from django.db import models
from datetime import datetime
# Create your models here.

class Project(models.Model):
    project_image = models.ImageField(upload_to="")
    project_title = models.CharField(max_length=50)
    project_text = models.TextField()
    project_date = models.DateTimeField(default = datetime.now, blank = True)
    project_slug = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
    	return self.project_title
