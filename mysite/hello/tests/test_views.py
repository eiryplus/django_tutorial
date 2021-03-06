from django.urls import reverse
from django.test import TestCase


class HelloWorldTestTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_world")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello World!')


class HelloTemplateTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_template")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)


class HelloIfTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_if")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)


class HelloForTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_for")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)


class HelloGetQueryTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_get_query")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)


class HelloFormsTest(TestCase):
    def test_valid(self):
        url_ = reverse("hello:hello_forms")
        with self.subTest("data is valid"):
            response = self.client.get(url_, data={"your_name": "aaaa"})
            self.assertEqual(response.status_code, 200)

    def test_invalid(self):
        url_ = reverse("hello:hello_forms")
        response = self.client.get(url_, data={"your_name": ""})
        self.assertEqual(response.status_code, 200)


class HelloSampleFormsTest(TestCase):
    def test_it(self):
        url_ = reverse("hello:hello_sample_forms")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)


class HelloModelsTest(TestCase):

    def _get_count(self) -> int:
        from hello.models import Hello
        return Hello.objects.count()

    def test_get(self):
        url_ = reverse("hello:hello_models")
        response = self.client.get(url_)
        self.assertEqual(response.status_code, 200)

    def test_post_valid(self):
        before_cnt = self._get_count()
        url_ = reverse("hello:hello_models")
        data = {"your_name": "Test"}
        response = self.client.post(url_, data=data, follow=True)
        after_cnt = self._get_count()
        self.assertEqual(response.redirect_chain,  [(url_, 302)])
        self.assertEqual(before_cnt+1, after_cnt)

    def test_post_invalid(self):
        before_cnt = self._get_count()
        url_ = reverse("hello:hello_models")
        data = {"": ""}
        response = self.client.post(url_, data=data, follow=True)
        after_cnt = self._get_count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_cnt, after_cnt)
