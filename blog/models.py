from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    blogs_body = models.TextField()


    def __str__(self):
        return self.title


    def summary(self):
        return self.blogs_body[:100]

    def modified_publish_date(self):
        return self.publish_date.strftime("%d %B, %Y")
