from django.db import models

class Photo(models.Model):
    small = models.ImageField(upload_to='photogallery')
    big = models.ImageField(upload_to='photogallery')
    text = models.CharField(max_length=256)

    def __unicode__(self):
        return self.text

