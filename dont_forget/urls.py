from django.urls import path, re_path
from . import views


urlpatterns = [
    #Homepage
    re_path(r'^$', views.index, name='index')
]