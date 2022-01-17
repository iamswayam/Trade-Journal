from .models import Note
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Nse


class NseForm(forms.ModelForm):
    class Meta:
        model = Nse
        fields = ["ticker"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['date','time', 'index', 'strike_price', 'position', 'call_type', 'lot', 'avg_price', 'sqo_price', 'sqo_price2', 'swing_high', 'swing_low', 'profit_loss', 'upload']

    # class DateForm(forms.Form):
    #     date = forms.DateTimeField(
    #         input_formats=['%d/%m/%Y %H:%M'],
    #         widget=DateTimePickerInput()
    #     )

        widgets = {
            'index': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'lot': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'call_type': forms.Select(attrs={'class': 'form-control'}),
            'strike_price': forms.TextInput(attrs={'class': 'form-control'}),
            'avg_price': forms.TextInput(attrs={'class': 'form-control'}),
            'sqo_price': forms.TextInput(attrs={'class': 'form-control'}),
            'sqo_price2': forms.TextInput(attrs={'class': 'form-control'}),
            'swing_high': forms.TextInput(attrs={'class': 'form-control'}),
            'swing_low': forms.TextInput(attrs={'class': 'form-control'}),
            'profit_loss': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profit_loss': forms.ImageInput(attrs={'class': 'form-control'}),
        }
