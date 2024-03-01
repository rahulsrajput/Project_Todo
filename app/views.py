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
    try:
        if request.method == 'POST':
            obj = Todo.objects.get(pk = id)
            obj.delete()
        return HttpResponseRedirect('/')
    
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/')



def update_task(request, id):
    try:

        if request.method == 'POST':
            task = request.POST['task']
            update_obj = Todo(pk=id, task=task)
            update_obj.save()
            return HttpResponseRedirect('/')

        obj = Todo.objects.get(pk=id)
        return render(request, 'base/update.html',context={'obj':obj})
    
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/') 