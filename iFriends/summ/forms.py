from django import forms

class Output(forms.Form):
    input1 = forms.IntegerField(max_value=10)
    input2 = forms.IntegerField(max_value=10)

    
    
