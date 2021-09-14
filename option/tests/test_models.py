from django.test import TestCase

from ..models import Question, Choice


class TestQuestion(TestCase):
    """
    test if the function('isfour()') returns true
    if a question has 4 options
    """
    @classmethod
    def setUpTestData(self):
        self.question = Question.objects.create(
            question_text="What is my name?",
            correct="Eboselume",
        )
    
    def test_if_str_function_returns_question_text(self):
        """
        Test if the '__str__()' function returns the 
        question text of a particular question
        """
        self.assertEqual(
            self.question.__str__(),
            "What is my name?"
        )

    def test_if_iffour_function_returns_false_if_choices_less_than_4(self):
        """
        Test if 'if_four()' function returns false if the choices of a 
        question are less than four
        """
        self.question.choice_set.create(
        option="Joshua"
        )
        result = self.question.is_four()

        self.assertEqual(result, False)

    def test_if_iffour_function_returns_True_if_choices_is_equals_to_4(self):
        """
        Test if 'if_four()' function returns true if the choices of a 
        question are exactly four
        """
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
        result = self.question.is_four()

        self.assertEqual(result, True)

    def test_if_iffour_function_returns_false_if_choices_greater_than_4(self):
        """
        Test if 'if_four()' function returns false if the choices of a 
        question are greater than four
        """
        self.question.choice_set.create(
            option="Joshua"
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
        result = self.question.is_four()

        self.assertEqual(result, False)

    def test_correct_opt_function_returns_correct(self):
        """
        Test if the 'correct_opt()' function returns
        the correct answer
        """
        self.assertEqual(self.question.correct_opt(), "Eboselume")

    def test_correct_ans_function_returns_True_for_correct_answer(self):
        """
        Test if the 'correct_ans()' returns true if the user_answer
        is equals to the correct option
        """
        self.question.user_answer = "Eboselume"

        self.assertEqual(self.question.correct_ans(), True)

    def test_correct_ans_function_returns_False_for_wrong_answer(self):
        """
        Test if the 'correct_ans()' returns false if the user_answer
        is is not equals to the correct option
        """
        self.question.user_answer = "Paul"

        self.assertEqual(self.question.correct_ans(), False)


class TestChoice(TestCase):

    def setUp(self):
        self.question = Question.objects.create(
            question_text="What is my name?"
        )
        self.question.choice_set.create(
            option="Paul"
        )
    
    def test_if_str_function_returns_option(self):
        """
        Test if the '__str__()' function returns the 
        option of a particular question
        """
        the_option = self.question.choice_set.first()

        self.assertEqual(
            the_option.__str__(),
            "Paul"
        )
    