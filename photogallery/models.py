from django.db import models
from cms.models.pluginmodel import CMSPlugin

class GalleryPluginModel(CMSPlugin):
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag

class Photo(models.Model):
    small = models.ImageField(upload_to='photogallery')
    big = models.ImageField(upload_to='photogallery')
    text = models.CharField(max_length=256)
    tag = models.CharField(max_length=256)

    def __unicode__(self):
        return self.text
