from django.shortcuts import render,redirect,get_object_or_404
#return http response
from django.http import HttpResponse
from .models import Task,Category
from .forms import TaskForm,CategoryForm
# Create your views here.

#function base view
def index(request):
	tasks=Task.objects.all().order_by('deadlin')
	categories=Category.objects.all()
	context={
		 'tasks':tasks,'categories':categories
	 }
	
	return render(request,'main/index.html',context)


def detailed_task(request,pk):
	task=Task.objects.get(id=pk)
	context={
		'task':task,
	}
	return render(request,'main/detailed.html',context)

def todo_by_status(request,st):
	todos=Task.objects.filter(status=st)
	context={
		'todos':todos
	}

	return render(request,'main/todosstatus.html',context)


def Createtodo(request):
	if request.method == 'POST':
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	
	else:
		form=TaskForm()


	return render(request,'main/create_todo.html',{'form':form})

def Createcategory(request):
	if request.method == 'POST':
		form=CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	
	else:
		
		form=CategoryForm()
	return render(request,'main/createCategorys.html',{'form':form})

def update_task(request , id ):
    task = get_object_or_404(Task , id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save()           
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form})

def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')
	
#class base view