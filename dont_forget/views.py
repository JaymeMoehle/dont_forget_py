from django.shortcuts import render
from . models import Note

# Create your views here.

def index(request):
    '''The homepage of Dont Forget App '''
    return render(request, 'dont_forget/index.html')


def notes(request):
    '''List all notes'''
    notes = Note.objects.order_by('date_added')
    context = {'notes': notes}
    return render(request, 'dont_forget/notes.html', context)


def note(request, note_id):
    '''Show a single note and all of it's entries'''
    note = Note.objects.get(id=note_id)
    entries = note.entry_set.order_by('-date_added')
    context = {'note': note, 'entries': entries}
    return render(request, 'dont_forget/note.html', context)