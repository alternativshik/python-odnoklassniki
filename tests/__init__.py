__author__ = 'mark'
import unittest
from odnoklassniki import signature

class TestSignature(unittest.TestCase):

    def test_signature(self):
        application_secret_key = '1'
        application_key = '2'
        params = {'method': '3',
                  'application_key': application_key}
        sig = signature(application_secret_key, '', params)
        self.assertEqual(sig, '42501554288d3bb6a1ba9ee035743315')
