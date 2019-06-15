from django.test import TestCase

"""
views.py で意味のあるテストは？
- 使われている template が正しいこと
- request に応じてCRUDが正しく行われていること
   - validation はforms.pyの責務
   - CRUD自体はModelの責務
- request に対して正しい response を返していること

- request.method == "GET" and not request.GET
- request.method == "GET" and request.GET and form.is_valid
- request.method == "GET" and request.GET and not form.is_valid
- request.method == "POST" and not form.is_valid
- request.method == "POST" and form.is_valid

is_no_query
is_valid_post
is_invalid_post
is_valid_get
is_invalid_get
"""


class IndexViewsTest(TestCase):
    """
    views.indexのテスト
    """

    def test_is_no_query(self):
        pass

    def test_is_valid_post(self):
        pass

    def test_is_invalid_post(self):
        pass

    def test_is_valid_get(self):
        pass

    def test_is_invalid_get(self):
        pass
