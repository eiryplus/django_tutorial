from django.urls import resolve
from django.test import TestCase


class UrlResolveTest(TestCase):

    def _getViews(self):
        from hello import views
        return views

    def test_index(self):
        """
        views.hello_world が呼び出されることを検証する
        """
        found = resolve("/hello/")
        self.assertEqual(found.func, self._getViews().hello_world)

    def test_template(self):
        """
        views.hello_template が呼び出されることを検証する
        """
        found = resolve("/hello/template/")
        self.assertEqual(found.func, self._getViews().hello_template)

    def test_if(self):
        """
        views.hello_if が呼び出されることを検証する
        """
        found = resolve("/hello/if/")
        self.assertEqual(found.func, self._getViews().hello_if)

    def test_for(self):
        """
        views.hello_for が呼び出されることを検証する
        """
        found = resolve("/hello/for/")
        self.assertEqual(found.func, self._getViews().hello_for)

    def test_get(self):
        """
        views.hello_get_query が呼び出されることを検証する
        """
        found = resolve("/hello/get/")
        self.assertEqual(found.func, self._getViews().hello_get_query)

    def test_forms(self):
        """
        views.hello_forms が呼び出されることを検証する
        """
        found = resolve("/hello/forms/")
        self.assertEqual(found.func, self._getViews().hello_forms)

    def test_sample_forms(self):
        """
        views.hello_sample_forms が呼び出されることを検証する
        """
        found = resolve("/hello/sample_forms/")
        self.assertEqual(found.func, self._getViews().hello_sample_forms)

    def test_models(self):
        """
        views.hello_models が呼び出されることを検証する
        """
        found = resolve("/hello/models/")
        self.assertEqual(found.func, self._getViews().hello_models)

