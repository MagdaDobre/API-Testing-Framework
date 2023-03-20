from random import randint
from Requests.api_clients import *

from API_project.Requests.api_clients import login


class TestApiClient:
    nr = randint(1, 9999999)
    clientName = 'Keith'
    clientEmail = f'valid_email_test{nr}@mailinator.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_succesful_login(self):
        assert self.response.status_code == 201, 'Actual status code is not correct'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in the response'

    def test_login_already_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'Status code is not OK'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.response = login('Name_client_email', 'invalid_email')
        assert self.response.status_code == 400, 'Actual status code is not correct'
        assert self.response.json()['error'] == 'Invalid or missing client email.'

