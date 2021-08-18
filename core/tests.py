from django.test import TestCase

# Create your tests here.
class HomeTestCase(TestCase):
    def test_home_success(self):
        response = self.client.get("/")
        assert response.status_code == 200
