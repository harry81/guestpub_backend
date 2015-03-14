from django.test import TestCase
from helpers import MessageGateway

class MessageGatewayTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        self.assertEqual(False, True)
