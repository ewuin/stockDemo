from django.conf.urls import url, static
from . import views           # This line is new!
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index),
    ]
