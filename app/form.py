from django import forms
from app.models import customer

class customerform(forms.ModelForm):
    class Meta:
        model =customer
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add attributes to the entire form
        self.fields['name'].widget.attrs.update({
            'class': 'class1',
            'placeholder': 'Your placeholder text',
        })
        
        self.fields['email'].widget.attrs.update({
            'class':'class3',
            'placeholder':'your email',
        })
        self.fields['chat'].widget.attrs.update({
            'class':'class2',
            
        })