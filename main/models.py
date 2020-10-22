from django.db import models

# Create your models here.


class Homepage(models.Model):
    what_i_do = models.CharField(max_length=500)

    def __str__(self):
        return "Homepage"
