from django.test import TestCase


class FormTest(TestCase):

    @staticmethod
    def _getTarget():
        from guestboard.forms import PostingForm
        return PostingForm

    def test_valid(self):
        """
        validationの正常系を検証する
        """
        with self.subTest("最大の入力値"):
            data = {
                "name": "あ" * 64,
                "message": "あ" * 255
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertTrue(is_valid)
            cleaned_data = form.cleaned_data
            self.assertEqual(cleaned_data["name"], "あ" * 64)
            self.assertEqual(cleaned_data["message"], "あ" * 255)
        with self.subTest("最小の入力値"):
            data = {
                "name": "a",
                "message": "a"
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertTrue(is_valid)
            cleaned_data = form.cleaned_data
            self.assertEqual(cleaned_data["name"], "a")
            self.assertEqual(cleaned_data["message"], "a")

    def test_invalid_name(self):
        """
        nameの入力値エラーを検証する
        """
        with self.subTest("maxlengthを超えた文字数"):
            data = {
                "name": "あ" * 65,
                "message": "あ" * 255
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertFalse(is_valid)
            self.assertEqual("この値は 64 文字以下でなければなりません( 65 文字になっています)。",
                             form.errors["name"][0])
            self.assertNotIn("message", form.errors)

        with self.subTest("0文字"):
            data = {
                "name": "",
                "message": "あ"
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertFalse(is_valid)
            self.assertEqual("名前を入力してください。",  form.errors["name"][0])
            self.assertNotIn("message", form.errors)

    def test_invalid_message(self):
        """
        messageの入力エラーを検証する
        """
        with self.subTest("maxlengthを超えた値"):
            data = {
                "name": "あ" * 64,
                "message": "あ" * 256
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertFalse(is_valid)
            self.assertEqual("この値は 255 文字以下でなければなりません( 256 文字になっています)。",
                             form.errors["message"][0])
            self.assertNotIn("name", form.errors)
        with self.subTest("0文字"):
            data = {
                "name": "あ" * 64,
                "message": ""
            }
            form = self._getTarget()(data)
            is_valid = form.is_valid()
            self.assertFalse(is_valid)
            self.assertEqual("メッセージを入力してください。",
                             form.errors["message"][0])
            self.assertNotIn("name", form.errors)
