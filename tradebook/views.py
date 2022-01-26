from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from .models import Note, NseIndexData, NseStockData
from .forms import NoteForm
from nsetools import Nse
import requests 
import json 


def home(request):
    
    indexAll = NseIndexData.objects.all()
    Icont = []
    
    stockAll = NseStockData.objects.all()
    Scont = []
    
    for index in indexAll:
        
        mData = Nse().get_index_quote(str(index))
        Icont.append(mData)
        
        name = mData['name']
        prc = mData['lastPrice']
        change = mData['change']
        pchange = mData['pChange']
        chart = mData['imgFileName']
        
        indContext = {'name': name, 'prc': prc, 'change':change, 'pchange': pchange, 'chart': chart}
        
        # print(indContext['name'], indContext['prc'])
        
        # return render(request, 'home.html', {'indContext':indContext, 'Icont': Icont})
        
    for stock in stockAll:
        
        mData = Nse().get_quote(str(stock))
        Scont.append(mData)
        
        name = mData['companyName']
        prc = mData['lastPrice']
        change = mData['change']
        pchange = mData['pChange']
        dhigh = mData['dayHigh']
        dlow = mData['dayLow']
        p_bnf = "{:.2f}".format(float(mData['pChange']) * 3.59712230216)
        
        bnf = Nse().get_index_quote("nifty bank")
        bnfpchange = bnf['pChange']
           
        stoContext = {'name': name, 'prc': prc, 'change':change, 'pchange': pchange, 'dhigh': dhigh, 'dlow': dlow, 'p_bnf': p_bnf}
        
        # print(stoContext['name'], stoContext['prc'])    
        
    return render(request, 'home.html', {'bnfpchange': bnfpchange, 'stoContext':stoContext, 'Scont': Scont, 'indContext':indContext, 'Icont': Icont})
    
    
# def stockLive(request):
    
#     stockAll = NseStockData.objects.all()
#     Scont = []
    
#     for stock in stockAll:
        
#         mData = Nse().get_quote(str(stock))
#         Scont.append(mData)
        
#         name = mData['companyName']
#         prc = mData['lastPrice']
#         change = mData['change']
#         pchange = mData['pChange']
#         dhigh = mData['dayHigh']
#         dlow = mData['dayLow']
#         p_bnf = "{:.2f}".format(float(mData['pChange']) * 3.59712230216)
        
#         stoContext = {'name': name, 'prc': prc, 'change':change, 'pchange': pchange, 'dhigh': dhigh, 'dlow': dlow, 'p_bnf': p_bnf}
        
#         print(stoContext['name'], stoContext['prc'])
        
#         return render(request, 'home.html', {'stoContext':stoContext, 'Scont': Scont})
    

    
    
    
    
        # notes = Note.objects.all()

	# if request.method == 'POST':
	# 	form = NseForm(request.POST or None)

	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('home')

	# else:	
	# 	ticker = NseData.objects.all()
	# 	output = []
	# 	for ticker_item in ticker:
	# 		api_request = Nse().get_index_quote(str(ticker_item))
	# 		try:
	# 			api = json.loads(api_request.content)
	# 			output.append(api)
	# 		except Exception as e:
	# 			api = "Error..."
		
	# 	return render(request, 'home.html', {'ticker': ticker, 'output': output})
    
    # nf = Nse().get_index_quote("nifty 50")
    # bnf = Nse().get_index_quote("nifty bank")
    # vix = Nse().get_index_quote("india vix")
    # nm = Nse().get_index_quote("nifty midcap 100")
    
    # nname = nf['name']
    # nprc = nf['lastPrice']
    # nchange = nf['change']
    # npchange = nf['pChange']
    # nchart = nf['imgFileName']
    
    # name = bnf['name']
    # prc = bnf['lastPrice']
    # change = bnf['change']
    # pchange = bnf['pChange']
    # chart = bnf['imgFileName']
    
    # vname = vix['name']
    # vprc = vix['lastPrice']
    # vchange = vix['change']
    # vpchange = vix['pChange']
    
    # n1name = nm['name']
    # n1prc = nm['lastPrice']
    # n1change = nm['change']
    # n1pchange = nm['pChange']
    # n1chart = nm['imgFileName']
    
    # vx = {'vname':vname, 'vprc':vprc, 'vchange':vchange, 'vpchange': vpchange}
    # n50 = {'nname':nname, 'nprc':nprc, 'nchange':nchange, 'npchange': npchange, 'nchart': nchart}
    # bn = {'name':name, 'prc':prc, 'change':change, 'pchange': pchange, 'chart': chart}
    # nm100 = {'n1name':n1name, 'n1prc':n1prc, 'n1change':n1change, 'n1pchange': n1pchange, 'n1chart': n1chart}
    
    # hdfcb = Nse().get_quote('hdfcbank')
    
    # hdname = hdfcb['companyName']
    # hdavg = hdfcb['lastPrice']
    # hdchange = hdfcb['change']
    # hdpchange = hdfcb['pChange']
    # hdhighd = hdfcb['dayHigh']
    # hdlowd = hdfcb['dayLow']
    # hd_bnf = "{:.2f}".format(float(hdfcb['pChange']) * 3.59712230216)
    
    # icici = Nse().get_quote('icicibank')
    
    # icname = icici['companyName']
    # icavg = icici['lastPrice']
    # icchange = icici['change']
    # icpchange = icici['pChange']
    # ichighd = icici['dayHigh']
    # iclowd = icici['dayLow']
    # ic_bnf = "{:.2f}".format(float(icici['pChange']) * 4.42086648983)
    
    # kotak = Nse().get_quote('kotakbank')
    
    # koname = kotak['companyName']
    # koavg = kotak['lastPrice']
    # kochange = kotak['change']
    # kopchange = kotak['pChange']
    # kohighd = kotak['dayHigh']
    # kolowd = kotak['dayLow']
    # ko_bnf = "{:.2f}".format(float(kotak['pChange']) * 8.61326442722)
    
    # hdfcbank = {'hdname':hdname, 'hdavg': hdavg, 'hdchange': hdchange, 'hdpchange': hdpchange, 'hdhighd':hdhighd, 'hdlowd': hdlowd, 'hd_bnf': hd_bnf}
    # icic = {'icname': icname, 'icavg': icavg, 'icchange': icchange, 'icpchange': icpchange, 'ichighd': ichighd, 'iclowd': iclowd, 'ic_bnf': ic_bnf}
    # kot = {'koname': koname, 'koavg': koavg, 'kochange': kochange, 'kopchange': kopchange, 'kohighd': kohighd, 'kolowd': kolowd, 'ko_bnf': ko_bnf}
    
    
    # return render(request, 'home.html', {'notes': notes, 'bn':bn, 'n50':n50, 'vx':vx, 'nm100': nm100, 'hdfcbank': hdfcbank, 'icic': icic, 'kot': kot})


    
    
4.42086648983

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
            form.save()
            return redirect('dashboard')
            
    else:
        form = NoteForm()

    return render(request, 'newnote.html', {'form': form})

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    
@login_required   
def dashboard(request):
    notes = Note.objects.all()
    return render(request, 'dashboard.html', {'notes': notes})

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
