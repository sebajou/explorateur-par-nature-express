from django.contrib.auth.forms import UserCreationForm
from UsersApp.models import Account
from ArticlesApp.models import Author
from django import forms
from django.db import transaction


# noinspection PySuperArguments
class AuthorSignUpForm(UserCreationForm, forms.Form):
    """Form for fill sign up. """

    class Meta(UserCreationForm.Meta):
        model = Account

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_author = True
        user.save()
        author = Author.objects.create(user=user)
        return user
