from django.urls import resolve
from django.test import TestCase


class UrlResolveTest(TestCase):

    def _getViews(self):
        from guestboard import views
        return views

    def test_index(self):
        """
        views.index が呼び出されることを検証する
        """
        found = resolve("/guestboard/")
        self.assertEqual(found.func, self._getViews().index_)

    def test_create(self):
        """
        views.index が呼び出されることを検証する
        """
        found = resolve("/guestboard/create/")
        self.assertEqual(found.func, self._getViews().create)

