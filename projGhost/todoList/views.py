from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(request):
	todos = Todo.objects.all()[:10]
	context = {
		'name':'Ethan',
		'todos':todos
	}
	return render(request,'index.html',context)

def details(request, id):
	todo = Todo.objects.get(id=id)
	context = {
		'name':'Ethan',
		'todo':todo
	}
	return render(request, 'details.html', context)

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		todo = Todo(title=title, text=text)
		todo.save()
		return redirect('/todoList')
	else:
		context = { 'name':'Ethan' }
		return render(request, 'add.html', context)