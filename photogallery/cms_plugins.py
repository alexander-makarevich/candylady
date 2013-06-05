# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _
from photogallery.models import Photo
from photogallery.models import GalleryPluginModel

class PhotoGalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    name = _("Photo Gallery Plugin")
    render_template = "plugin2.html"

    def render(self, context, instance, placeholder):
        context.update({
            'photos': Photo.objects.filter(tag=instance.tag),
            'instance': instance
        })
        return context

plugin_pool.register_plugin(PhotoGalleryPlugin)

