from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


 
class PostsAPIViewTest(APITestCase):

    def __init__(self, method_name):
        super().__init__(methodName=method_name)
        self.client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user_token = Token.objects.create(user=self.user).key
        self.posts_url = reverse('posts-list')

    def test_auth_response(self):
        """Authorized user have access to posts list"""

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.user_token}')
        
        resp = self.client.get(self.posts_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_unauth_response(self):

        resp = self.client.get(self.posts_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
