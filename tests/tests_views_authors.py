from django.test import Client
import pytest
from UsersApp.models import Tribut

c = Client()


# class TestGetRoutesGeneral:
#     """Test pages routes """
#
#     def setup_method(self):
#         self.articles_pk = {'pk': 6}
#         self.articles_title = {'slug': 'fabriquer-une-table-modulo'}
#
#     def test_article_read_view(self, client):
#         # {% url 'article_read' articles.pk articles.title|slugify
#         pk = self.articles_pk
#         slug = self.articles_title
#         response = client.get('article_read', pk, slug)
#         print(response)
#         assert response.status_code == 200


class TestPostRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.article_create = {'title': 'on regarde les mouches au plafond', 'objectif': 'du vide',
                               'content': 'du vide', 'pedagogic_aims': 'aucun', 'victory_celebration_display': 'youpi',
                               'id_badge': 1}
        self.article_image = {'description': 'description', 'authors': 'lui', 'title': 'un titre', 'num_apparition': 1,
                              'image_article': 'path'}
        self.article_equipment = {'text': 'text', 'quantity': 3, 'unity': 'metre'}

    @pytest.mark.django_db
    def test_article_create_view(self, client):
        c.login(username='auteur1', password='1AQWXSZ2')
        article_create = self.article_create
        article_image = self.article_image
        article_equipment = self.article_equipment
        client.login(username='auteur1', password='1AQWXSZ2')
        response = client.post('/article/add/', post_form=article_create, formset=article_image,
                               formset_equipment=article_equipment)
        assert response.status_code == 200

