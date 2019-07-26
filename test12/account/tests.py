from django.test import TestCase
from django.test import Client

from account.models import User
from test12 import logging

class AccountTest(TestCase):
    def setUp(self):
        '''
        Every test needs a client.
        '''
        self.client = Client()

    def test_main_page(self):
        '''
        Check main page response correctly
        '''
        response = self.client.get('/account/main/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "register")
        self.assertContains(response, "login")

    def test_login_page(self):
        '''
        Check login page response correctly
        '''
        response = self.client.get('/account/login/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "username")
        self.assertContains(response, "password")
        self.assertContains(response, "input")

    def test_login_process(self):
        '''
        Check login page work correctly
        '''

        # create a new user
        user = User.objects.create_user(username="testName", password="testPasswd")

        data = {'username': user.username, 
                'password': 'testPasswd'}
        response = self.client.post('/account/login/', 
                                    data, 
                                    follow=True)

        self.assertEqual(response.redirect_chain[0][0], '/account/main/')
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)

    def test_register_page(self):
        '''
        Check login page response correctly
        '''
        response = self.client.get('/account/register/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "username")
        self.assertContains(response, "password")
        self.assertContains(response, "password2")
        self.assertContains(response, "input")

    def test_register_process(self):
        '''
        Check login page work correctly
        '''

        data = {'username': 'testName', 
                'password': 'testPasswd', 
                'password2': 'testPasswd'}
        response = self.client.post('/account/register/', data, follow=True)

        self.assertEqual(response.redirect_chain[0][0], '/account/main/')
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "register")
        self.assertContains(response, "login")


