from django.test import Client
import pytest

c = Client()


class TestRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.guardian_sign_in_page = {'username': 'David', 'password': '1AQWXSZ2'}
        self.child_sign_in_page = {'username': 'Judith', 'password': '1AQWXSZ2'}
        self.guardian_sign_up_page = {'username': 'Sausau', 'password': '1AQWXSZ2', 'tribut': 'Issacar',
                                      'prenom': 'Saushana', 'nom': 'Sussman', 'email': 'sausau@gmail.com'}
        self.child_sign_up_page = {'username': 'Eli', 'password': '1234'}

    def test_home_page(self):
        response = c.get('/')
        assert response.status_code == 200

    def test_guardian_sign_up_page(self):
        response = c.get('/guardian_sign_up_page/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_guardian_sign_in_page(self):
        user_to_login = self.guardian_sign_in_page
        response = c.post('/guardian_sign_in_page/', user_to_login)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_sign_up_page(self):
        user_to_login = self.guardian_sign_in_page
        response_one = c.post('/guardian_sign_in_page/', user_to_login)
        response_two = c.get('/guardian_sign_up_page/')
        assert response_one.status_code == 200 and response_two.status_code == 200

    @pytest.mark.django_db
    def test_child_sign_in_page(self):
        user_to_login = self.guardian_sign_in_page
        child_to_login = self.child_sign_in_page
        response_one = c.post('/guardian_sign_in_page/', user_to_login)
        response_two = c.post('/guardian_sign_in_page/', child_to_login)
        assert response_one.status_code == 200 and response_two.status_code == 200

    @pytest.mark.django_db
    def test_guardian_sign_up_page(self):
        user_to_sign = self.guardian_sign_up_page
        response = c.post('/guardian_sign_up_page/', user_to_sign)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_child_sign_up_page(self):
        user_to_login = self.guardian_sign_in_page
        child_to_sign = self.guardian_sign_up_page
        response_one = c.post('/guardian_sign_in_page/', user_to_login)
        response_two = c.post('/child_sign_up_page/', child_to_sign)
        assert response_one.status_code == 200 and response_two.status_code == 200
