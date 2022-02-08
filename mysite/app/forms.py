from django import forms

class Weather(forms.Form):
    city = forms.CharField(max_length=100)

class Bmi(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField()

class Notes(forms.Form):
    data = forms.CharField(max_length=500)

class Stocks(forms.Form):
    label = forms.CharField(max_length=100)

class Wikipedia(forms.Form):
    search = forms.CharField(max_length=200)

class Favorite(forms.Form):
    link = forms.CharField(max_length=100)

class Calc(forms.Form):
    expression = forms.CharField(max_length=100)