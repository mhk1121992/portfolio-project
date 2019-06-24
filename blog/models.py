from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    text_body = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text_body[:100]

    def pub_date_new(self):
        return self.publish_date.strftime(' %b %e %Y')