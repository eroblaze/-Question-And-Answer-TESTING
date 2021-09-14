from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    query_set = Question.objects.all()

    return render(request, "index.html", {'query_set': query_set})

def process(request):
    if request.method == 'POST':
        try:
            all_query = Question.objects.all()
            for one in all_query:
                one.user_answer = None
                one.save()
        except:
            print("No object in the database")

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