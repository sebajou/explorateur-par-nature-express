from UsersApp.models import Child, Tribut
from django import forms


# noinspection PySuperArguments
class InsidePageChildForm(forms.ModelForm):
    """Form for fill sign up. """

    class Meta:
        model = Tribut
        fields = ('account_tribut')
