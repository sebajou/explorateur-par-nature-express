from django.test import Client
import pytest
from UsersApp.models import Tribut

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

    @pytest.mark.django_db
    def test_logout_page(self):
        response = c.get('/UsersApp/accounts/logout/')
        assert response.status_code == 200


class TestPostRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.tutor_signup = {'tutor_username': 'didi', 'first_name': 'Judith', 'last_name': 'Delico',
                        'email': 'didelico@yahoo.fr'}
        self.tribut_signin = {'username': 'JoBru', 'password': '1AQWXSZ2'}
        self.child_sign_up = {'child_username': 'lili', 'first_name': 'Luciane', 'last_name': 'Delico'}

    @pytest.mark.django_db
    def test_tribut_sign_in_page(self):
        user_to_login = self.tribut_signin
        response = c.post('/accounts/login/', user_to_login)
        assert response.status_code == 200 or response.status_code == 302

    @pytest.mark.django_db
    def test_tutor_form_page(self, client, django_user_model):
        # username = "user1"
        # password = "bar"
        # user = django_user_model.objects.create_user(username=username, password=password)
        # client.force_login(user)
        # response = client.get('/tutor_form/')
        c.login(username='JoBru', password='1AQWXSZ2')
        response = c.get('/tutor_form/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_form_page(self, client, django_user_model):
        # username = "user1"
        # password = "bar"
        # user = django_user_model.objects.create_user(username=username, password=password)
        # client.force_login(user)
        # response = client.get('/child_form/')
        c.login(username='JoBru', password='1AQWXSZ2')
        response = c.get('/child_form/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_tribut_profile(self, client, django_user_model):
        # username = "JoBru"
        # password = "1AQWXSZ2"
        # user = django_user_model.objects.create_user(username=username, password=password)
        # client.force_login(user)
        # response = client.get('/tribut_profile/')
        c.login(username='JoBru', password='1AQWXSZ2')
        response = c.get('/tribut_profile/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_signup(self, client, django_user_model):
        child_signup = self.child_sign_up
        c.login(username='JoBru', password='1AQWXSZ2')
        response = c.post('/child_form/', child_signup)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_tutor_signup(self, client, django_user_model):
        tutor_signup = self.tutor_signup
        c.login(username='JoBru', password='1AQWXSZ2')
        response = client.post('/tutor_form/', tutor_signup)
        assert response.status_code == 302
