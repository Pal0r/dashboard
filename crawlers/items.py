import scrapy
from scrapy_djangoitem import DjangoItem

from web.models import EntertainmentItem, MusicItem, TechnologyItem, \
    ScienceItem


class TechnologyDjangoItem(DjangoItem):
    django_model = TechnologyItem


class EntertainmentDjangoItem(DjangoItem):
    django_model = EntertainmentItem


class MusicDjangoItem(DjangoItem):
    django_model = MusicItem


class ScienceDjangoItem(DjangoItem):
    django_model = ScienceItem
