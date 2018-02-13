from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . models import Topic, Entry, Note, NoteEntry
from . forms import TopicForm, NoteForm, EntryForm, NoteEntryForm


#Topic section of the app

def index(request):
    """The homepage of Dont Forget App"""
    return render(request, 'dont_forget/index.html')


def topics(request):
    """List all topics"""
    topics = Topic.objects.order_by('created_on')
    context = {'topics': topics}
    return render(request, 'dont_forget/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all of it's entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-created_on')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dont_forget/topic.html', context)



def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dont_forget:topics'))
    context = {'form': form}
    return render(request, 'dont_forget/new_topic.html', context)


def new_entry(request, topic_id):
    """Add new entry for a topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('dont_forget:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'dont_forget/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit and existing topic entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dont_forget:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form }
    return render(request, 'dont_forget/edit_entry.html', context)


#Note section of the app

def notes(request):
    '''List all notes'''
    notes = Note.objects.order_by('created_on')
    context = {'notes': notes}
    return render(request, 'dont_forget/notes.html', context)



def note(request, note_id):
    '''Show a single note and all of its content'''
    note = Note.objects.get(id=note_id)
    note_entries = note.noteentry_set.all()
    context = {'note': note, 'note_entries': note_entries}
    return render(request, 'dont_forget/note.html', context)



def new_note(request):
    """Add a new note"""
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dont_forget:notes'))
    context = {'form': form}
    return render(request, 'dont_forget/new_note.html', context)


def new_note_entry(request, note_id):
    """Add new entry for a topic"""
    note = Note.objects.get(id=note_id)

    if request.method != 'POST':
        form = NoteEntryForm()

    else:
        form = NoteEntryForm(data=request.POST)
        if form.is_valid():
            new_note_entry = form.save(commit=False)
            new_note_entry.note = note
            new_note_entry.save()
            return HttpResponseRedirect(reverse('dont_forget:note', args=[note_id]))

    context = {'note': note, 'form': form}
    return render(request, 'dont_forget/new_note_entry.html', context)


def edit_note_entry(request, note_entry_id):
    """Edit and existing topic entry"""
    note_entry = NoteEntry.objects.get(id=note_entry_id)
    note = note_entry.note

    if request.method != 'POST':
        form = NoteEntryForm(instance=note_entry)
    else:
        form = NoteEntryForm(instance=note_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dont_forget:note', args=[note.id]))
    context = {'note_entry': note_entry, 'note': note, 'form': form }
    return render(request, 'dont_forget/edit_note_entry.html', context)
