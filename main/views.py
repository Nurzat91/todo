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

def add_book(request):
    form = request.POST
    title = form["book.title"]
    subtitle = form["book.subtitle"]
    description = form["book.description"]
    price = form["book.price"]
    genre = form["book.genre"]
    author = form["book.author"]
    year = form["book.year"]
    # date = form["date"]
    books = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    books.save()
    return redirect(tom)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)  


