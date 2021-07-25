from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Tutor, Tribut
from django import forms
from UsersApp.models import Tribut


# noinspection PySuperArguments
class TutorSignUpForm(forms.ModelForm):
    """Form for fill sign up. """

    class Meta:
        model = Tutor
        exclude = ('id_tribut', )
        fields = ('tutor_username', 'first_name', 'last_name', 'email', 'image_profile_tutor')
