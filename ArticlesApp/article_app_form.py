from ArticlesApp.models import Article, Image, Equipment
from django import forms


class ArticleCreationForm(forms.ModelForm):
    """Form for fill article creation. """

    class Meta:
        model = Article
        fields = ('title', 'objectif', 'content', 'pedagogic_aims', 'victory_celebration_display',
                  'article_cover_image', 'id_badge')


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('description', 'authors', 'title', 'num_apparition', 'image_article')


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('text', 'quantity', 'unity')

