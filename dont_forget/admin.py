from django.contrib import admin

# Register your models here.

from dont_forget.models import Topic, Entry, Note, NoteEntry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Note)
admin.site.register(NoteEntry)

