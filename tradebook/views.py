from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

# def newnote(request):
#     if request.method == "GET":
#         return render(request, 'newnote.html', {'form': NoteForm()})
#     else:
#         try:
#             form = NoteForm(request.POST)
#             newnote = form.save(commit=False)
#             newnote.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/createtodo.html', {'form': NoteForm(), 'error': 'Bad data! Try again.'})


def newnote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            newnote = form.save()
            return HttpResponseRedirect(reverse(newnote, args=(newnote.html,)))
    else:
        form = NoteForm()

    return render(request, 'newnote.html', {'form': form})

