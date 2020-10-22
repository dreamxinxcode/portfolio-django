from django.db import models
from datetime import datetime
# Create your models here.


class BlogPost(models.Model):
    blog_image = models.ImageField(upload_to="blog")
    blog_title = models.CharField(max_length=50)
    blog_text = models.TextField()
    blog_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(max_length=200, default=1)

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
        return self.blog_title
