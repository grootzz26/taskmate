from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def todolist(request):
    if request.method == 'POST':
       form = TaskForm(request.POST or None)
       if form.is_valid():
           instance = form.save(commit=False)
           instance.manage = request.user
           instance.save()
       messages.success(request, ("New Task Added!"))
       return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,('Access Restricted!, you are not Allowed.'))
    return redirect('todolist')


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,('Access Restricted!, you are not Allowed.'))
    return redirect('todolist')

@login_required
def incomplete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request,('Access Restricted!, you are not Allowed.'))
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated!"))
        return  redirect('todolist')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html',{'task':task})


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')