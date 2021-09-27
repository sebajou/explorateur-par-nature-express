from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Child
from django import forms
from UsersApp.models import Tribut
from django.utils.translation import gettext_lazy as _


# noinspection PySuperArguments
class ChildSignUpForm(forms.ModelForm):
    """Form for fill sign up. """

    class Meta:
        model = Child
        exclude = ('account_tribut', )
        fields = ('child_username', 'first_name', 'last_name', 'image_profile_child')
        labels = {
            'child_username': _('Pseudo de l\'enfant '),
            'first_name': _('Prénom '),
            'last_name': _('Nom de famille '),
            'image_profile_child': _('Image de l\'enfant '),
        }
