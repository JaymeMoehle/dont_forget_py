from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


from . models import Topic, Entry, Note
from . forms import TopicForm, EntryForm, NoteForm


#Topic section of the app

def index(request):
    """The homepage of Dont Forget App"""
    return render(request, 'dont_forget/index.html')

@login_required
def topics(request):
    """List all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('created_on')
    context = {'topics': topics}
    return render(request, 'dont_forget/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all of it's entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-created_on')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dont_forget/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('dont_forget:topics'))
    context = {'form': form}
    return render(request, 'dont_forget/new_topic.html', context)

@login_required
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

@login_required
def edit_entry(request, entry_id):
    """Edit and existing topic entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dont_forget:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form }
    return render(request, 'dont_forget/edit_entry.html', context)


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id).delete()
    return redirect('dont_forget:topics')


@login_required
def note(request):

    note_list = Note.objects.filter(owner=request.user).order_by('id')
    form = NoteForm()
    context={'note_list': note_list, 'form': form}

    return render(request, 'dont_forget/note.html', context)


@require_POST
@login_required
def addNote(request):
    form = NoteForm(data=request.POST)

    if form.is_valid():
        new_note = Note(text=request.POST['text'])
        new_note.owner=request.user
        new_note.save()

    return redirect('dont_forget:note')

@login_required
def complete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.complete = True
    note.save()

    return redirect('dont_forget:note')

@login_required
def delete_note(request):
    Note.objects.filter(complete__exact=True).delete()


    return redirect('dont_forget:note')

@login_required
def delete_all_notes(request):
    Note.objects.all().delete()

    return redirect('dont_forget:note')


def logout_view(request):
    """Log out the user"""
    logout(request)
    return HttpResponseRedirect(reverse('dont_forget:index'))



def register(request):
    """Register a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.isvalid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('dont_forget:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)



