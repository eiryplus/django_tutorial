from django.urls import reverse
from django.test import TestCase
from django.template.response import TemplateResponse
from django.core.paginator import Page

from guestboard.test import factory


class ListVIewTest(TestCase):
    @staticmethod
    def _getUrl():
        return reverse("guestboard:index")

    def _makeResponse(self, data=None) -> TemplateResponse:
        return self.client.get(self._getUrl(), data=data)

    def setUp(self):
        for _ in range(100):
            factory.PostingFactory()

    def test_get_without_param(self):
        response = self._makeResponse()
        self.assertEqual(200, response.status_code)
        paginator: TemplateResponse = response.context_data["paginator"]
        page_obj: Page = response.context_data["page_obj"]
        self.assertEqual(50, paginator.num_pages)
        self.assertEqual(1, page_obj.number)
        self.assertFalse(page_obj.has_previous())
        self.assertTrue(page_obj.has_next())
        self.assertEqual(2, len(page_obj.object_list))

    def test_get_first_page(self):
        response = self._makeResponse(dict(page=1))
        self.assertEqual(200, response.status_code)
        paginator: TemplateResponse = response.context_data["paginator"]
        page_obj: Page = response.context_data["page_obj"]
        self.assertEqual(50, paginator.num_pages)
        self.assertEqual(1, page_obj.number)
        self.assertFalse(page_obj.has_previous())
        self.assertTrue(page_obj.has_next())
        self.assertEqual(2, len(page_obj.object_list))

    def test_get_middle_page(self):
        response = self._makeResponse(dict(page=2))
        self.assertEqual(200, response.status_code)
        paginator: TemplateResponse = response.context_data["paginator"]
        page_obj: Page = response.context_data["page_obj"]
        self.assertEqual(50, paginator.num_pages)
        self.assertEqual(2, page_obj.number)
        self.assertTrue(page_obj.has_previous())
        self.assertTrue(page_obj.has_next())
        self.assertEqual(2, len(page_obj.object_list))

    def test_get_last_page(self):
        response = self._makeResponse(dict(page=50))
        self.assertEqual(200, response.status_code)
        paginator: TemplateResponse = response.context_data["paginator"]
        page_obj: Page = response.context_data["page_obj"]
        self.assertEqual(50, paginator.num_pages)
        self.assertEqual(50, page_obj.number)
        self.assertTrue(page_obj.has_previous())
        self.assertFalse(page_obj.has_next())
        self.assertEqual(2, len(page_obj.object_list))

    def test_get_with_invalid_param(self):
        with self.subTest("範囲外（最小）"):
            response = self._makeResponse(dict(page=0))
            self.assertEqual(404, response.status_code)
        with self.subTest("範囲外（最大）"):
            response = self._makeResponse(dict(page=51))
            self.assertEqual(404, response.status_code)
        with self.subTest("ページ番号に数字以外を指定"):
            response = self._makeResponse(dict(page="a"))
            self.assertEqual(404, response.status_code)


class CreateViewTest(TestCase):
    def _getResponse(self, data=None) -> TemplateResponse:
        url = reverse("guestboard:create")
        return self.client.post(url, data=data)

    @staticmethod
    def _get_count() -> int:
        from guestboard.models import Posting
        return Posting.objects.count()

    def test_post_valid(self):
        raise ValueError()  # またあとでやる

    def test_post_invalid(self):
        raise ValueError()  # またあとでやる
