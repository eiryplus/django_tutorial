from django.test import TestCase


class MessageFormTest(TestCase):

    def _getClass(self):
        from crud.forms import MessageForm
        return MessageForm

    def test_valid(self):
        """
        validationが成功するケース
        """
        d = {'message': 'a'*255}
        form = self._getClass()(d)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, d)

    def test_invalid(self):
        """
        validationが失敗するケース
        """
        # max_length
        d = {'message': 'a'*256}
        form = self._getClass()(d)
        self.assertFalse(form.is_valid())

        # empty
        d = {'message': ''}
        form = self._getClass()(d)
        self.assertFalse(form.is_valid())
