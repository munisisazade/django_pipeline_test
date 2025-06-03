from django.test import TestCase, Client


class SampleTest(TestCase):

    def test_home_page_hello_world(self):
        client = Client()
        response = client.get("/")
        assert "Hello World" in response.content.decode("utf-8")