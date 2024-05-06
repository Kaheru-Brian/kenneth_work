from typing import Any
from django import forms 

class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control fname'}),required=False)
    details = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    no_people = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),required=False)
    day_of_week = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    date_created = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'form-control'}),required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        details = cleaned_data.get('details')
        no_people = cleaned_data.get('no_people')
        day_of_week = cleaned_data.get('day_of_week')
        date_created = cleaned_data.get('date_created')
        
        if not name:
            self.add_error('name', 'Please provide a name')
        elif len(name) < 3:
            self.add_error('name', 'Name must be at least 3 characters')
            
        return cleaned_data   
        