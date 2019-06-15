from django.urls import resolve
from django.test import TestCase
from .. import views


class UrlResolveTest(TestCase):

    def _getViews(self):
        from crud import views
        return views

    def test_index(self):
        """
        views.index が呼び出されることを検証する
        """
        found = resolve('/crud/')
        self.assertEqual(found.func, self._getViews().list_)

    def test_create(self):
        """
        views.add が呼び出されることを検証する
        """
        found = resolve('/crud/create/')
        self.assertEqual(found.func, self._getViews().create)

    def test_edit(self):
        """
        views.edit が呼び出されることを検証する
        """
        found = resolve('/crud/update/1/')
        self.assertEqual(found.func, self._getViews().update)

    def test_delete(self):
        """
        views.delete_ が呼び出されることを検証する
        """
        found = resolve('/crud/delete/1/')
        self.assertEqual(found.func, self._getViews().delete_)
