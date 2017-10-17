# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EntertainmentItem, MusicItem, TechnologyItem, ScienceItem


admin.site.register(EntertainmentItem)
admin.site.register(MusicItem)
admin.site.register(TechnologyItem)
admin.site.register(ScienceItem)
