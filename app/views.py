from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST['task']
        # print(task)

        obj = Todo(task = task)
        obj.save()
    

    objects = Todo.objects.all()
    return render(request, 'base/home.html', context={'objects':objects})


def delete_task(request, id):
    if request.method == 'POST':
        obj = Todo.objects.get(pk = id)
        obj.delete()
        return HttpResponseRedirect('/')
    