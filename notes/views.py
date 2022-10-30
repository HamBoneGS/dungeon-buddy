from django.shortcuts import render
from django.http import HttpResponse

from .models import Note

def index(request):
    return render(request, 'notes/index.html')

def save_note(request):
    note = Note.objects.create(
        title = request.POST['title'],
        body = request.POST['body']
    )
    note.save()
    return HttpResponse("Saved!")