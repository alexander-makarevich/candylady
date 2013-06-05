from django.db import models
from cms.models.pluginmodel import CMSPlugin

class GalleryPluginModel(CMSPlugin):
    title = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

class Photo(models.Model):
    small = models.ImageField(upload_to='photogallery')
    big = models.ImageField(upload_to='photogallery')
    text = models.CharField(max_length=256)
    plugin = models.ForeignKey(
        GalleryPluginModel,
        related_name="associated_item"
        )

    def __unicode__(self):
        return self.text
