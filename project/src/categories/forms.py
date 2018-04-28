
from django import forms

class CategoriesListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name asc'),
        ('-name', 'Name desc'),
        ('id', 'id'),
    ),  required=False)

    search = forms.CharField(required= False)
