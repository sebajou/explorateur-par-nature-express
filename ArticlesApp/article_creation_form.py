from django.contrib.auth.forms import UserCreationForm
from ArticlesApp.models import Article
from django import forms


class ArticleCreationForm(forms.ModelForm):
    """Form for fill article creation. """

    # Add video, image and badge from many to many and many to one relationship

    class Meta:
        model = Article
        fields = ('title', 'objectif', 'content', 'pedagogic_aims', 'victory_celebration_display')
