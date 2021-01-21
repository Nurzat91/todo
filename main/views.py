from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Books

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is  page test3.")


def tom(request):
    books_page = Books.objects.all()
    return render(request, "books.html", {"books_page": books_page})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    # return HttpResponse("Форма получена")  
    return redirect(test)  