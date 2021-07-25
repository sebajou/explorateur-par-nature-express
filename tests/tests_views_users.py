from django.test import Client
import pytest

c = Client()


class TestGetRoutesGeneral:
    """Test index and homes pages routes """

    def test_home_page(self):
        response = c.get('/')
        assert response.status_code == 200

    def test_sign_up_page(self):
        response = c.get('/signup/')
        assert response.status_code == 200

    def test_login_page(self):
        response = c.get('/accounts/login/')
        assert response.status_code == 200

    def test_logout_page(self):
        response = c.get('/UsersApp/accounts/logout/')
        assert response.status_code == 200


class TestPostRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.tribut_sign_in_page = {'username': 'JoBru', 'password': '1AQWXSZ2'}
        # self.child_sign_in_page = {'username': 'Judith', 'password': '1AQWXSZ2'}
        # self.guardian_sign_up_page = {'username': 'Sausau', 'password': '1AQWXSZ2', 'tribut': 'Issacar',
        #                               'prenom': 'Saushana', 'nom': 'Sussman', 'email': 'sausau@gmail.com'}
        # self.child_sign_up_page = {'username': 'Eli', 'password': '1234'}

    @pytest.mark.django_db
    def test_tribut_sign_in_page(self):
        user_to_login = self.tribut_sign_in_page
        response = c.post('/accounts/login/', user_to_login)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_tutor_form_page(self, client, django_user_model):
        username = "user1"
        password = "bar"
        user = django_user_model.objects.create_user(username=username, password=password)
        client.force_login(user)
        response = client.get('/tutor_form/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_form_page(self, client, django_user_model):
        username = "user1"
        password = "bar"
        user = django_user_model.objects.create_user(username=username, password=password)
        client.force_login(user)
        response = client.get('/child_form/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_tribut_profile(self, client, django_user_model):
        username = "user1"
        password = "bar"
        user = django_user_model.objects.create_user(username=username, password=password)
        client.force_login(user)
        response = client.get('/tribut_profile/')
        assert response.status_code == 200
