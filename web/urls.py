from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^science/$', ScienceItemListView.as_view(), name='science'),
    url(r'^technology/$', TechnologyItemListView.as_view(), name='technology'),
    url(r'^entertainment/$', EntertainmentItemListView.as_view(), name='entertainment'),
    url(r'^music/$', MusicItemListView.as_view(), name='music'),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
]
