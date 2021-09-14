from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import index, process, result, create, delete


class TestViews(SimpleTestCase):
    def setUp(self):
        self.index = reverse("option:index")
        self.check = reverse("option:process")
        self.result = reverse("option:result")
        self.create = reverse("option:create")
        self.delete = reverse("option:delete")

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

    def test_create_url(self):
        """
        Test create url calls the right function
        and uses the correct path name
        """
        the_resolved = resolve(self.create)

        self.assertEqual(the_resolved.func, create)
        self.assertEqual(the_resolved.url_name, "create")

    def test_delete_url(self):
        """
        Test delete url calls the right function
        and uses the correct path name
        """
        the_resolved = resolve(self.delete)

        self.assertEqual(the_resolved.func, delete)
        self.assertEqual(the_resolved.url_name, "delete")
    