from django.test import SimpleTestCase, override_settings
from django.urls import reverse

from .urls import DummyFormViewWithMsg


@override_settings(ROOT_URLCONF='core.tests.urls')
class SuccessMessageMixinTests(SimpleTestCase):

    def test_set_messages_error(self):
        author = {'name': ''}
        add_url = reverse('add_error_msg')
        req = self.client.post(add_url, author)
        self.assertIn(DummyFormViewWithMsg.error_message, req.content.decode('utf-8'))
