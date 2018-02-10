from django.shortcuts import render

# Create your views here.

def index(request):
    '''The homepage of Dont Forget App '''
    return render(request, 'dont_forget/index.html')