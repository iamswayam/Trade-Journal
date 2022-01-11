from .models import Note
from django import forms
# from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['date','time', 'index', 'strike_price', 'position', 'call_type', 'avg_price', 'sqo_price', 'sqo_price2', 'swing_high', 'swing_low', 'profit_loss', 'upload']

    # class DateForm(forms.Form):
    #     date = forms.DateTimeField(
    #         input_formats=['%d/%m/%Y %H:%M'],
    #         widget=DateTimePickerInput()
    #     )

        widgets = {
            'index': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            # 'index': forms.TextInput(attrs={'class': 'form-control'}),
            # 'index': forms.TextInput(attrs={'class': 'form-control'}),
            # 'index': forms.TextInput(attrs={'class': 'form-control'}),
            # 'index': forms.TextInput(attrs={'class': 'form-control'}),
        }
