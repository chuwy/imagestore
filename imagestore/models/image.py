#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from django.utils.translation import ugettext_lazy as _

from .bases.image import BaseImage
from imagestore.utils import load_class, get_model_string


class Image(BaseImage):
    class Meta(BaseImage.Meta):
        abstract = False
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        app_label = 'imagestore'