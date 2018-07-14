from django.test import TestCase
from ..forms import (
    MessageForm
)


class MessageFormTest(TestCase):

    def test_valid(self):
        """
        validationが成功するケース
        """
        d = {'message': 'a'*255}
        form = MessageForm(d)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, d)

    def test_invalid(self):
        """
        validationが失敗するケース
        """
        # max_length
        d = {'message': 'a'*256}
        form = MessageForm(d)
        self.assertFalse(form.is_valid())

        # empty
        d = {'message': ''}
        form = MessageForm(d)
        self.assertFalse(form.is_valid())
