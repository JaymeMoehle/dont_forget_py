from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . models import Topic, Entry
from . forms import TopicForm, EntryForm


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












