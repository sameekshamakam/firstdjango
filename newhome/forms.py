from django import forms
from newhome.models import Book,Author,Publication

class BookForm(forms.Form):
    name=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name'}))
    book_author =forms.ModelChoiceField(
                    queryset=Author.objects.all(),
                    empty_label='Author',widget=forms.Select(attrs={'name':'book_author','id':'book_author'}))
                     

class ModelBookForm(forms.ModelForm):
    
    class Meta:
        model=Book
        fields='__all__'

class SearchForm(forms.Form):
    q=forms.CharField(label='',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Search','class':'form-control','minlength':'2'}))

    class Meta:
        model=Book
        fields='__all__'

'''class CustomForms(forms.Form):
    username=forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={'placeholder':'your username',
            'class':'form-control',
            'max':'20'
            }
        )
    )
    
    email=forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'placeholder':'ac@gmail.com','class':'form control'}))
'''