
from django import forms


class QuestionListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name asc'),
        ('-name', 'Name desc'),
        ('created', 'created asc'),
        ('-created', 'created desc'),
        ('updated', 'updated asc'),
        ('-updated', 'updated desc')
    ),  required=False)

    search = forms.CharField(required= False)
