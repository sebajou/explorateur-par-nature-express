from django.test import Client
import pytest
from UsersApp.models import Tribut

c = Client()


class TestGetRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.child_id = {'id_child': 2}

    @pytest.mark.django_db
    def test_home_page(self):
        response = c.get('/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_sign_up_page(self):
        response = c.get('/signup/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_login_page(self):
        response = c.get('/accounts/login/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_logout_page(self):
        response = c.get('/UsersApp/accounts/logout/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_gallery_of_child_trophies(self, client):
        id_child = self.child_id
        response = client.get('trophies_gallery', id_child)
        return response.status_code == 200

    @pytest.mark.django_db
    def test_profile(self):
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.get('profile')
        return response.status_code == 200


class TestPostRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.user_signup = {'username': 'TribuDesBois', 'email': 'desbois@gmail.com',
                            'password1': '1AQWXSZ2', 'password2': '1AQWXSZ2'}
        self.tutor_signup = {'tutor_username': 'didi', 'first_name': 'Judith', 'last_name': 'Delico',
                        'email': 'didelico@yahoo.fr'}
        self.tribut_signin = {'username': 'Pratrib', 'password': '1AQWXSZ2'}
        self.child_sign_up = {'child_username': 'lili', 'first_name': 'Luciane', 'last_name': 'Delico'}
        self.child_id = {'id_child': 2}
        self.childs_id = ['1', '2']
        self.article_id = {'id_article': 4}

    @pytest.mark.django_db
    def test_run_login_page(self):
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.get('/accounts/login/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_logout_page(self):
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.get('/UsersApp/accounts/logout/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_user_form(self):
        user_signup = self.user_signup
        response = c.post('/signup/', user_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_tribut_sign_in_page(self):
        user_to_login = self.tribut_signin
        response = c.post('/accounts/login/', user_to_login)
        assert response.status_code == 200 or response.status_code == 302

    @pytest.mark.django_db
    def test_tutor_form_page(self):
        tutor_signup = self.tutor_signup
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.post('/tutor_form/', tutor_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_child_form_page(self):
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.get('/child_form/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_tribut_profile(self):
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.get('/tribut_profile/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_signup(self):
        child_signup = self.child_sign_up
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = c.post('/child_form/', child_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_tutor_signup(self, client):
        tutor_signup = self.tutor_signup
        c.login(username='Pratrib', password='1AQWXSZ2')
        response = client.post('/tutor_form/', tutor_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_child_one_article_success(self, client):
        response = c.login(username='Pratrib', password='1AQWXSZ2')
        id_childs = self.childs_id
        id_article = self.article_id
        id_to_post = {'id_child': id_childs, 'id_article': id_article}
        response1 = client.post('articles_child_success', id_to_post)
        assert response
        assert response1.status_code == 302

    @pytest.mark.django_db
    def test_run_gallery_of_child_trophies(self, client):
        c.login(username='Pratrib', password='1AQWXSZ2')
        id_child = self.child_id
        response = client.post('trophies_gallery', id_child)
        return response.status_code == 200
