from django.urls import path, re_path
from . import views



app_name = 'dont_forget'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    re_path(r'^notes/$', views.notes, name='notes'),
    re_path(r'^notes/(?P<note_id>\d+)/$', views.note, name='note'),
    re_path(r'^new_note/$', views.new_note, name='new_note'),
    re_path(r'^new_note_entry/(?P<note_id>\d+)/$', views.new_note_entry, name='new_note_entry'),

]
