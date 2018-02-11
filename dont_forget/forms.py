from django import forms
from . models import Topic, Entry, Note, NoteEntry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}


class NoteEntryForm(forms.ModelForm):
    class Meta:
        model = NoteEntry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 2})}