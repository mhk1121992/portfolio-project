from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    text_body = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='images/')

