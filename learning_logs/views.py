from django.shortcuts import render, redirect
from . models import Topic, Entry
from . forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Show all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request , 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''Show all entries of a topic'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''Add new topics'''
    if request.method != 'POST':
        '''No post data submitted: create a blank form'''
        form = TopicForm()
    else:
        '''Post data submitted: process the dat'''
        form = TopicForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''Add a new entry to a particular topic'''
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        '''No data submitted: create a blank form'''
        form = EntryForm()
    else:
        '''post data submitted: process the data'''
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id)
        
    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)
