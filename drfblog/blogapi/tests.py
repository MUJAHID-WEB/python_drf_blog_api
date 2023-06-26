from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myblog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('blogapi:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blogapi:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 6)
        root = reverse(('blogapi:detailcreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
