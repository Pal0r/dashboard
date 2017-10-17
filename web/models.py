# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BaseAbstractItem(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class EntertainmentItem(BaseAbstractItem):
    pass


class MusicItem(BaseAbstractItem):
    pass


class TechnologyItem(BaseAbstractItem):
    pass


class ScienceItem(BaseAbstractItem):
    title = models.CharField(max_length=255)
