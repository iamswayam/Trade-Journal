from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})


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
                return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'Hey! This username already been taken! Try a new one.'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Password did not match'})


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist!")
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, User)
            return redirect('home')
        else: 
            print("Username or Password is incorrect!")
        
        
    return render(request, "tradebook/login-signup.html")

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
            return redirect('home')
            # return HttpResponseRedirect(reverse(home, args=(home,)))
    else:
        form = NoteForm()

    return render(request, 'newnote.html', {'form': form})

