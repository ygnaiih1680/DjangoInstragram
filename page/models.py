from django.db import models


class Content(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
