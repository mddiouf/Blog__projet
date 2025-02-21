from django.forms import ModelForm
from django import forms
from .models import Post
class PostForm(forms.ModelForm):
     class Meta:
        model=Post
        fields=['title','content']
        widgets={
            'title':forms.TextInput(
                attrs={
                    'placeholder':'Entrer votre titre',
                    'class':'form-control'
                }
            ),
            'content':forms.TextInput(
                attrs={
                    'placeholder':'Entrer votre contenue',
                    'class':'form-control'
                }
        
        ),
}