import unittest

from pylistshine import connection

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch



class ContactTest(unittest.TestCase):
    def setUp(self):
        self.conn = connection.LSConnection('fake_api_key')

    @patch('requests.post')
    def test_subscribe(self, _):
        contact = self.conn.contact("fake-list-uu-id")
        response = contact.subscribe("email@email.com", firstname="name")

    @patch("requests.post")
    def test_unsubscribe(self, _):
        contact = self.conn.contact("fake-list-uu-id")
        response = contact.unsubscribe("email@email.com")

    @patch("requests.get")
    def test_list(self, _):
        contact = self.conn.contact("fake-list-uu-id")
        response = contact.list()

    @patch("requests.get")
    def test_contactlist_list(self, _):
        cl = self.conn.contactlist()
        response = cl.list()

    @patch("requests.get")
    def test_contactlist_retrieve(self, _):
        cl = self.conn.contactlist()
        response = cl.retrieve("fake-list-uu-id")
