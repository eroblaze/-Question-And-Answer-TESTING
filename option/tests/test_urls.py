from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import index, process, result


class TestViews(SimpleTestCase):
    def setUp(self):
        self.index = reverse("option:index")
        self.check = reverse("option:process")
        self.result = reverse("option:result")

    def test_index_url(self):
        """
        Test index url calls the right function
        and uses the correct path name
        """
        the_resolved = resolve(self.index)

        self.assertEqual(the_resolved.func, index)
        self.assertEqual(the_resolved.url_name, "index")
    
    def test_check_url(self):
        """
        Test check url calls the right function
        and uses the correct path name
        """
        the_resolved = resolve(self.check)

        self.assertEqual(the_resolved.func, process)
        self.assertEqual(the_resolved.url_name, "process")
    
    def test_result_url(self):
        """
        Test result url calls the right function
        and uses the correct path name
        """
        the_resolved = resolve(self.result)

        self.assertEqual(the_resolved.func, result)
        self.assertEqual(the_resolved.url_name, "result")
    