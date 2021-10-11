from django.test import Client
import pytest


c = Client()


@pytest.fixture
def test_password():
    return 'strong-test-pass'


class TestUserComportment:
    """Tests of users logical comportment on app"""

    def setup_method(self):
        self.user_signup = {'username': 'TribuDesBois', 'email': 'desbois@gmail.com',
                            'password1': '1AQWXSZ2', 'password2': '1AQWXSZ2'}
        self.tutor_signup = {'tutor_username': 'didi', 'first_name': 'Judith', 'last_name': 'Delico',
                        'email': 'didelico@yahoo.fr'}
        self.tribut_signin = {'username': 'Pratrib', 'password': '1AQWXSZ2'}
        self.child_sign_up = {'child_username': 'lili', 'first_name': 'Luciane', 'last_name': 'Delico'}
        self.child_id = {'id_child': 1}
        self.childs_id = ['1', '2']
        self.article_id = {'id_article': 4}
        self.article_create = {'title': 'on regarde les mouches au plafond', 'objectif': 'du vide',
                               'content': 'du vide', 'pedagogic_aims': 'aucun', 'victory_celebration_display': 'youpi',
                               'id_badge': 1}
        self.article_create2 = {'title': 'on regarde les mouches au plafond qui tourne', 'objectif': 'du vide',
                               'content': 'du vide', 'pedagogic_aims': 'aucun', 'victory_celebration_display': 'youpi',
                               'id_badge': 1}
        self.article_image = {'description': 'description', 'authors': 'lui', 'title': 'un titre', 'num_apparition': 1,
                              'image_article': 'path'}
        self.article_equipment = {'text': 'text', 'quantity': 3, 'unity': 'metre'}

    @pytest.fixture
    def create_user(self, db, django_user_model, test_password):
        """User mock. """

        def make_user(**kwargs):
            kwargs['password'] = "1AQWXSZ2"
            if 'username' not in kwargs:
                kwargs['username'] = "Tribu"
            if 'email' not in kwargs:
                kwargs['email'] = "tribu@gmail.com"
            return django_user_model.objects.create_user(**kwargs)

        return make_user

    @pytest.fixture
    def auto_login_user(self, db, client, create_user, test_password):
        def make_auto_login(user=None):
            if user is None:
                user = create_user()
            client.login(email=user.email, password=test_password)
            return client, user

        return make_auto_login

    @pytest.mark.django_db
    def test_signup_logout(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        response = client.get('http://127.0.0.1:8000/UsersApp/accounts/logout/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_signup_login_article_read(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        response = client.get('http://127.0.0.1:8000/article/6/fabriquer-une-table-modulo/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_signup_login_signup_child(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        child_signup = self.child_sign_up
        response = c.post('/child_form/', child_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_signup_login_signup_child_success_article(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        child_signup = self.child_sign_up
        id_child = self.child_id
        response = c.post('/child_form/', child_signup)
        print(response)
        response2 = c.post('/articles_child_success/', id_child)
        assert response.status_code and response2.status_code == 302

    @pytest.mark.django_db
    def test_login_search_add_favorite(self, auto_login_user):
        # mock request.user and login
        client, user = auto_login_user()
        response = client.get('http://127.0.0.1:8000/article/6/fabriquer-une-table-modulo/')
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_signup_login_signup_child_success_article_trophy(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        child_signup = self.child_sign_up
        id_child = self.child_id
        response = c.post('/child_form/', child_signup)
        response2 = c.post('/articles_child_success/', id_child)
        response3 = c.post('/trophies_gallery/1', id_child)
        assert response.status_code and response2.status_code and response3.status_code == 302

    @pytest.mark.django_db
    def test_article_create_then_update(self, client):
        c.login(username='auteur1', password='1AQWXSZ2')
        article_create = self.article_create
        article_create2 = self.article_create2
        article_image = self.article_image
        article_equipment = self.article_equipment
        response = client.login(username='auteur1', password='1AQWXSZ2')
        response1 = client.post('/article/add/', post_form=article_create, formset=article_image,
                                formset_equipment=article_equipment)
        response2 = client.get('/article/10')
        response3 = client.post('/article/10/', post_form2=article_create2)
        assert response
        assert response1.status_code == 200
        assert response2.status_code == 301
        assert response3.status_code == 200

    @pytest.mark.django_db
    def test_article_create_then_delete(self, client):
        c.login(username='auteur1', password='1AQWXSZ2')
        article_create = self.article_create
        article_image = self.article_image
        article_equipment = self.article_equipment
        response = client.login(username='auteur1', password='1AQWXSZ2')
        response1 = client.post('/article/add/', post_form=article_create, formset=article_image,
                                formset_equipment=article_equipment)
        response2 = client.get('/article/delete/10')

        assert response
        assert response1.status_code == 200
        assert response2.status_code == 301
