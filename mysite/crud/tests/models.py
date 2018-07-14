from django.test import TestCase
from ..models import Message


class MessageTest(TestCase):
    def setUp(self):
        self.m1 = Message(message="A"*30)
        self.m1.save()
        self.m2 = Message(message="B"*255)
        self.m2.save()

    def tearDown(self):
        self.m1.delete()
        self.m2.delete()

    def test_to_str(self):
        self.assertEqual(str(self.m1), ("1:" + "A"*30))
        self.assertEqual(str(self.m2), ("2:" + "B" * 27 + "..."))

    def test_values(self):
        self.assertEqual(self.m1.message, "A"*30)
        self.assertEqual(self.m2.message, "B"*255)
