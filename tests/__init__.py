import unittest

from odnoklassniki import Odnoklassniki


class TestSecretKey(unittest.TestCase):

    def test_signature(self):
        application_key = '1'
        application_secret = '2'
        access_token = '3'

        ok = Odnoklassniki(application_key, application_secret, access_token)
        secret = ok.secret

        self.assertEqual(secret, '6364d3f0f495b6ab9dcf8d3b5c6e0b01')


class TestSignature(unittest.TestCase):

    def test_signature(self):
        application_key = '1'
        application_secret = '2'
        access_token = '3'

        params = {
            'method': 'friends.get',
            'application_key': application_key,
            'format': 'json',
        }

        ok = Odnoklassniki(application_key, application_secret, access_token)

        sig = ok._signature(params)

        self.assertEqual(sig, 'd7348fe0d7d735aa2156fa5c596ab8cc')
