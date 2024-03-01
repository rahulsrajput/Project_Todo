from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST['task']
        # print(task)

        obj = Todo(task = task)
        obj.save()
    

    objects = Todo.objects.all()
    return render(request, 'base/home.html', context={'objects':objects})