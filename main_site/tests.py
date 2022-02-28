from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import UploadSerializer
from .models import Upload
from django.core.files import File

class UploadTestCase(APITestCase):

    def test_upload(self):
        f = File(open('main_site/test_files/cloudofthings1.png', 'rb'))
        data = {"_name": "testcase","_file": f}
        response = self.client.post("http://127.0.0.1:8000/add/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

"""
    def test_failed_upload(self):
        f = File(open('main_site\test_files\cloudofthings2.jpg', 'rb'))
        data = {"_name": "testcase","_file": f}
        response = self.client.post("http://127.0.0.1:8000/add/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
"""
    def test_request(self):
        response = self.client.get('http://127.0.0.1:8000/')
        assert response.status_code == 200






