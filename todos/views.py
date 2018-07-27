from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.


def index(request):

    todos=Todo.objects.all()[:5]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':

        title = request.POST['title']
        text = request.POST['text']
        created_at = request.POST['date']

        todo = Todo(title=title, text=text, created_at=created_at)
        todo.save()

    else:
        return render(request, 'add.html')

"""Function to delete a record in todos"""


def delete(request, id):
    todo_to_delete = Todo.objects.get(id=id)
    if todo_to_delete==None:
        return HttpResponse('NOT FOUND')
    else:
        todo_to_delete.delete()
        return HttpResponse('deleted')







