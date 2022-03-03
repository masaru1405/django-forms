from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
   class Meta:
      model = Pizza
      fields = ['topping1', 'topping2', 'size']
      labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

""" class PizzaForm(forms.Form):
   topping1 = forms.CharField(label='Topping 1', max_length=100)
   topping2 = forms.CharField(label='Topping2', max_length=100)
   size = forms.ChoiceField(label='Size', choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]) """