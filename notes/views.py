from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Note

def notes(request, id = None):
    all_notes = [x for x in Note.objects.order_by('id')]
    context = {
        'all_notes': all_notes
    }
    if id:
        context['chosen_note'] = Note.objects.filter(pk=id).first()
    return render(request, 'notes/notes.html', context)

def save_note(request):
    note = Note.objects.create(
        title = request.POST['title'],
        body = request.POST['body']
    )
    note.save()
    return HttpResponseRedirect("/notes")

def update_note(request, id):
    note_to_update = Note.objects.get(pk=id)
    note_to_update.title = request.POST['title']
    note_to_update.body = request.POST['body']
    note_to_update.save()
    return HttpResponseRedirect(f"/notes/{id}")