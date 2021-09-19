from django.contrib.auth.forms import UserCreationForm
from ArticlesApp.models import Article, Image, Equipment
from UsersApp.models import Badge
from django import forms


class ArticleCreationForm(forms.ModelForm):
    """Form for fill article creation. """

    # Add video, image and badge from many to many and many to one relationship
    # badge_name = forms.MultipleChoiceField(
    #     required=True,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=Badge.objects.all(),
    # )

    # image_load = forms.ModelChoiceField(
    #     required=False,
    #     queryset=Image.objects.all()
    # )

    class Meta:
        model = Article
        fields = ('title', 'objectif', 'content', 'pedagogic_aims', 'victory_celebration_display',
                  'article_cover_image', 'id_badge')


class ImageUploadForm(forms.ModelForm):
    # image = forms.ImageField(label='image_article')

    class Meta:
        model = Image
        fields = ('description', 'authors', 'title', 'num_apparition', 'image_article')


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('text', 'quantity', 'unity')

# class BadgeForm(forms.ModelForm):
#     """Form for fill article creation. """
#
#     # Add video, image and badge from many to many and many to one relationship
#
#     class Meta:
#         model = Badge
#         fields = ('title', 'category', 'level', 'image_badge')
