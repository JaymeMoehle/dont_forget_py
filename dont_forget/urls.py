from django.urls import path, re_path
from . import views



app_name = 'dont_forget'
urlpatterns = [
    #Home page
    re_path(r'^$', views.index, name='index'),

    #Topics
    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    re_path(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name='delete_topic'),


    re_path(r'^note/$', views.note, name='note'),
    re_path(r'^addNote/$', views.addNote, name='addNote'),
    re_path(r'^complete_note/(?P<note_id>\d+)/$', views.complete_note, name='complete_note'),
    re_path(r'^delete_note/$', views.delete_note, name='delete_note'),
    re_path(r'^delete_all_notes/$', views.delete_all_notes, name='delete_all_notes'),


]

