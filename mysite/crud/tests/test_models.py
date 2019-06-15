from django.test import TestCase


class MessageTest(TestCase):

    def _getClass(self):
        from crud.models import Message
        return Message

    def setUp(self):
        self.m1 = self._getClass()(message="A"*30)
        self.m1.save()
        self.m2 = self._getClass()(message="B"*255)
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
