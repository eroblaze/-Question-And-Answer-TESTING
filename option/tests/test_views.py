from django.test import TestCase
from django.urls import reverse

from ..models import Question


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.index = reverse("option:index")

        self.question1 = Question.objects.create(
            question_text="What is my name?",
        )
        self.question1 = Question.objects.create(
            question_text="What is my laptop's name?",
        )
        self.question1 = Question.objects.create(
            question_text="What is my project's name?",
        )
    
    def test_index_view_status_code(self):
        """
        Test if the GET request on index view
        returns a successful status code.
        """
        response = self.client.get(self.index)

        self.assertEqual(response.status_code, 200)

    def test_index_view_returns_context_with_no_data(self):
        """
        Test if index view will not return anything
        to the template if the database is empty
        """
        Question.objects.all().delete()
        response = self.client.get(self.index)

        self.assertQuerysetEqual(response.context['query_set'], [])

    def test_index_view_returns_context_with_data(self):
        """
        Test if index view returns all the questions in the 
        database on a GET request
        """
        response = self.client.get(self.index)
        query_set = Question.objects.all()

        self.assertQuerysetEqual(
            response.context['query_set'], 
            query_set,
            ordered=False
        )
    
    def test_index_view_template_used(self):
        """
        Test if the index view uses the right
        template
        """
        response = self.client.get(self.index)

        self.assertTemplateUsed(response, "index.html")

    
class TestProcessView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.question = Question.objects.create(
            question_text="What is my name?",
        )
        self.question2 = Question.objects.create(
            question_text="What is my age?",
        )
        self.question3 = Question.objects.create(
            question_text="What is my ge?",
        )
        self.question.choice_set.create(
            option="Paul"
        )
        self.question.choice_set.create(
            option="Favour"
        )
        self.question.choice_set.create(
            option="Tope"
        )
        self.question.choice_set.create(
            option="Joshua"
        )

        self.process = reverse("option:process")

    def test_process_view_renders_template_on_GET_request(self):
        """
        Test if 'process view' will return the 'result.html'
        template when a GET request is made
        """
        response = self.client.get(self.process)

        self.assertTemplateUsed(response, "result.html")
        self.assertEqual(response.status_code, 200)

    def test_process_view_saves_the_checked_answer_to_the_user_answer_attribute(self):
        """
        Test if the 'process view' updates the user_answer attribute of  
        multiple questions on a POST request.
        """
        data = {
            'p-1-Tope': "checked",
            'p-2-dkfjd': "checked",
            'p-3-fine': "checked"
        }
        response = self.client.post(
            self.process, 
            data
        )
        question = Question.objects.get(id=1)
        question2 = Question.objects.get(id=2)
        question3 = Question.objects.get(id=3)

        self.assertEqual(question.user_answer, "Tope")
        self.assertEqual(question2.user_answer, "dkfjd")
        self.assertEqual(question3.user_answer, "fine")

    
    def test_process_view_on_POST_redirects_to_result_page(self):
        """
        Test if after the processing of the user answers, the
        'process view' redirects the user to the 'result page'
        """
        response = self.client.post(
            self.process, 
            {'p-1-3': "checked"}
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("option:result"))


class TestResultView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.result = reverse("option:result")

        self.question1 = Question.objects.create(
            question_text="What is my name?",
        )
        self.question1 = Question.objects.create(
            question_text="What is my laptop's name?",
        )
        self.question1 = Question.objects.create(
            question_text="What is my project's name?",
        )
    
    def test_result_view_status_code(self):
        """
        Test if the GET request on result view
        returns a successful status code.
        """
        response = self.client.get(self.result)

        self.assertEqual(response.status_code, 200)

    def test_result_view_returns_context_with_no_data(self):
        """
        Test if result view will not return anything
        to the template if the database is empty
        """
        Question.objects.all().delete()
        response = self.client.get(self.result)

        self.assertQuerysetEqual(response.context['query_set'], [])

    def test_result_view_returns_context_with_data(self):
        """
        Test if result view returns all the questions in the 
        database on a GET request
        """
        response = self.client.get(self.result)
        query_set = Question.objects.all()

        self.assertQuerysetEqual(
            response.context['query_set'], 
            query_set,
            ordered=False
        )
    
    def test_result_view_template_used(self):
        """
        Test if the result view uses the right
        template
        """
        response = self.client.get(self.result)

        self.assertTemplateUsed(response, "result.html")
