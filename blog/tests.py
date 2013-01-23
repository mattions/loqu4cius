from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

class BlogTest(TestCase):
    fixtures = ['test_blog_fixture.json']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def test_single_entry(self):
        
        response = self.client.get(reverse("entry-detail", args=["my-first-entry",] ))
        
        self.assertEqual(response.status_code, 200)
    
    def test_list(self):
        # Issue a GET request.
        response = self.client.get(reverse("home"))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the link to the 2 entries.
        self.assertContains(response, '<a href="/my-first-entry/">')
        self.assertContains(response, '<a href="/sdadsad/">')
