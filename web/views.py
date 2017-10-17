# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import ScienceItem, MusicItem, EntertainmentItem, TechnologyItem


class ScienceItemListView(ListView):
    model = ScienceItem
    paginate_by = 10


class TechnologyItemListView(ListView):
    model = TechnologyItem
    paginate_by = 10


class EntertainmentItemListView(ListView):
    model = EntertainmentItem
    paginate_by = 10


class MusicItemListView(ListView):
    model = MusicItem
    paginate_by = 10


class HomeTemplateView(TemplateView):
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        c = super(HomeTemplateView, self).get_context_data(**kwargs)

        c['science_count'] = ScienceItem.objects.count()
        c['music_count'] = MusicItem.objects.count()
        c['entertainment_count'] = EntertainmentItem.objects.count()
        c['technology_count'] = TechnologyItem.objects.count()

        return c
