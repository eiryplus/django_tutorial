from django.core.urlresolvers import resolve
from django.test import TestCase
from .. import views


class UrlResolveTest(TestCase):

    def test_index(self):
        """
        views.index が呼び出されることを検証する
        """
        found = resolve('/crud/')
        self.assertEqual(found.func, views.index)

    def test_add(self):
        """
        views.add が呼び出されることを検証する
        """
        found = resolve('/crud/add/')
        self.assertEqual(found.func, views.add)

    def test_edit(self):
        """
        views.edit が呼び出されることを検証する
        """
        found = resolve('/crud/edit/1/')
        self.assertEqual(found.func, views.edit)

    def test_delete(self):
        """
        views.add が呼び出されることを検証する
        """
        found = resolve('/crud/delete/')
        self.assertEqual(found.func, views.delete)

