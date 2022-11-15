from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Note

def notes(request, id = None):
    all_notes = [x for x in Note.objects.order_by('date_created')]
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