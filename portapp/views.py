from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
	    # a =dform()
        a =portsk() #delete this line
        a.name=request.POST['name']
        a.mail=request.POST['mail']
        a.subject=request.POST['subject']
        a.message = request.POST['message']
        a.save()
    return render(request, "index.html")


