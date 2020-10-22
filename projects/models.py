from django.db import models
from datetime import datetime
# Create your models here.


class Project(models.Model):
    project_image = models.ImageField(upload_to="projects")
    project_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=1)
    project_intro = models.TextField(default=1)
    project_overview = models.TextField()
    project_github = models.CharField(max_length=100, blank=True)
    project_client = models.CharField(max_length=100, blank=True)
    project_client_website = models.CharField(max_length=100, blank=True)
    project_client_industry = models.CharField(max_length=100, blank=True)
    open_source = models.BooleanField(default=True)
    project_featured = models.BooleanField(default=False)
    project_date = models.DateField(default=datetime.now)

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at

    def __str__(self):
        return self.project_title
