from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from .serializers import NoteSerializer

from . models import Topic, Entry, Note
from . forms import TopicForm, EntryForm


#Topic section of the app

def index(request):
    """The homepage of Dont Forget App"""
    return render(request, 'dont_forget/index.html')

@login_required
@csrf_exempt
def topics(request):
    """List all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('created_on')
    context = {'topics': topics}
    return render(request, 'dont_forget/topics.html', context)

@login_required
@csrf_exempt
def topic(request, topic_id):
    """Show a single topic and all of it's entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-created_on')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'dont_forget/topic.html', context)


@login_required
@csrf_exempt
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
@csrf_exempt
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
@csrf_exempt
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
@csrf_exempt
def note(request):
    context= {}
    context['note'] = Note.objects.all()

    html = TemplateResponse(request, 'dont_forget/note.html', context)
    return HttpResponse(html.render())

@login_required
@method_decorator(csrf_exempt, name='dispatch')
class NoteViewSet(viewsets.ModelViewSet):
    """API endpoint that allows notes to be viewed or edited"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
