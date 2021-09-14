from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Question, Choice


def index(request):
    query_set = Question.objects.all()

    return render(request, "index.html", {'query_set': query_set})

def process(request):
    if request.method == 'POST':
        all_query = Question.objects.all()

        if all_query:
            for one in all_query:
                one.user_answer = None
                one.save()

        li = []

        for k in request.POST.items():
            if k[0][0] == 'p':
                li.append(k[0]) # ['p-1-paul', 'p-2-2']

        new_li = []
        new_id = []

        for one in li:
            new = one.split("-")
            new_id.append(new[1])
            new_li.append(new[2])

        print("Selected:",new_li)

        if new_id:
            i = 0
            for one in new_id:
                if all_query:
                    question = Question.objects.get(id=one)
                    question.user_answer = new_li[i]
                    question.save()
                    i += 1

        return redirect(reverse("option:result"))

    else:
        return render(request, "result.html")

def result(request):
    query_set = Question.objects.all()

    return render(request, "result.html", {'query_set': query_set})

def create(request):
    if request.method == 'POST':
        try:
            question_text = request.POST.get('question_text').strip()
            correct = request.POST.get('correct').strip()
            option1 = request.POST.get('option1').strip()
            option2 = request.POST.get('option2').strip()
            option3 = request.POST.get('option3').strip()
            option4 = request.POST.get('option4').strip()
            
        except Exception:
            messages.info(request, "Incomplete Data!")
            return render(request, "create.html")
        
        all_choices = [option1, option2, option3, option4]

        if correct in all_choices:
            question = Question.objects.create(
                question_text=question_text,
                correct=correct
            )
            question.save()
        else:
            messages.info(request, "Invalid option for 'Correct Answer'!")
            return render(request, "create.html")

        question.choice_set.create(option=option1)
        question.choice_set.create(option=option2)
        question.choice_set.create(option=option3)
        question.choice_set.create(option=option4)
        question.save()

        query_set = question.choice_set.all().count()

        if query_set == 4:
            messages.info(request, "Question Successfully Created!")
            return render(request, "create.html")
        
    else:
        return render(request, "create.html")

def delete(request):
    if request.method == 'POST':
        decision = request.POST.get('yes')

        if decision == 'yes':
            Question.objects.all().delete()
            return redirect(reverse("option:index"))
        else:
            return redirect(reverse("option:create"))

    else:
        return render(request, "delete.html")