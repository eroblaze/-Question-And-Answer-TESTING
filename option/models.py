from django.db import models


class Question(models.Model):

    question_text = models.CharField(max_length=400)
    user_answer = models.CharField(
        max_length=100, 
        null="Not found", 
        default="No Answer Chosen"
    )
    correct = models.CharField(
        max_length=100, 
        null="Not found", 
        blank=False
    )

    def __str__(self):
        return self.question_text
    
    def is_four(self):
        """
        This function will check if the total number of
        choices that a question have is 4
        """
        query_set = self.choice_set.all()

        return(len(query_set) == 4)

        # if len(query_set) == 4:
        #     return True
        # else:
        #     return False
    def correct_opt(self):
        return self.correct

    def correct_ans(self):
        return(self.user_answer == self.correct)


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option

    
        