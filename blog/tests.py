from django.utils import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client

class BlogTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
    
    def test_single_entry(self):
        
        response = self.client.get(reverse(args=["entry_detail", entry] ))
        
        self.assertEqual(response.status_code, 200)
    
    def test_list(self):
        # Issue a GET request.
        response = self.client.get(reverse(args=["home"]))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
