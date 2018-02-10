from django.urls import path, re_path
from . import views



app_name = 'dont_forget'
urlpatterns = [
    #Homepage
    re_path(r'^$', views.index, name='index'),
    re_path(r'^notes/$', views.notes, name='notes'),
    re_path(r'^notes/(?P<note_id>\d+)/$', views.note, name= 'note'),
]