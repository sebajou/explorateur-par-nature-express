from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Tutor, Tribut
from django import forms
from UsersApp.models import Tribut
from django.utils.translation import gettext_lazy as _


# noinspection PySuperArguments
class TutorSignUpForm(forms.ModelForm):
    """Form for fill sign up. """

    class Meta:
        model = Tutor
        exclude = ('account_tribut', )
        fields = ('tutor_username', 'first_name', 'last_name', 'email', 'image_profile_tutor')
        labels = {
            'tutor_username': _('Pseudo du tuteur '),
            'first_name': _('Prénom '),
            'last_name': _('Nom de famille '),
            'image_profile_tutor': _('Image du tuteur '),
        }
