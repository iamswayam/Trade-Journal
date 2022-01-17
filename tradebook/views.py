from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.urls import reverse
from .models import Note
from .forms import NoteForm
from nsetools import Nse


def home(request):
    notes = Note.objects.all()
    
    nf = Nse().get_index_quote("nifty 50")
    bnf = Nse().get_index_quote("nifty bank")
    vix = Nse().get_index_quote("india vix")
    
    nname = nf['name']
    nprc = nf['lastPrice']
    nchange = nf['change']
    npchange = nf['pChange']
    nchart = nf['imgFileName']
    
    name = bnf['name']
    prc = bnf['lastPrice']
    change = bnf['change']
    pchange = bnf['pChange']
    chart = bnf['imgFileName']
    
    vname = vix['name']
    vprc = vix['lastPrice']
    vchange = vix['change']
    vpchange = vix['pChange']
    
    vx = {'vname':vname, 'vprc':vprc, 'vchange':vchange, 'vpchange': vpchange}
    n50 = {'nname':nname, 'nprc':nprc, 'nchange':nchange, 'npchange': npchange, 'nchart': nchart}
    bn = {'name':name, 'prc':prc, 'change':change, 'pchange': pchange, 'chart': chart}
    
    return render(request, 'home.html', {'notes': notes, 'bn':bn, 'n50':n50, 'vx':vx})


def SignupPage(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Hey! This username already been taken! Try a new one.'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Password did not match'})


def LoginPage(request):
    
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Username & Password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def newnote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            newnote = form.save()
            return redirect('home')
            
    else:
        form = NoteForm()

    return render(request, 'newnote.html', {'form': form})

# def nse_data(request):
#     bnf = Nse().get_index_quote("nifty bank")
#     name = bnf['name']
#     prc = bnf['lastPrice']
#     bn = {'name':name, 'prc':prc}
    
#     return render(request, 'home.html', {'bn':bn})
    

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
