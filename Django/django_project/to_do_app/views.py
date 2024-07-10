from django.shortcuts import render,redirect, HttpResponse
from .models import to_do

# Create your views here


def home(request):
    todos = to_do.objects.all()
    return render(request, 'index.html',{'todos':todos})

def add_to_do(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        new_todo = to_do(title=title, description=description) 
        new_todo.save()
        return redirect('home')
    
def show_update(request,todo_id):
    update_todo = to_do.objects.get(pk=todo_id)
    return render(request, 'update.html', {'todo':update_todo})

def update(request,todo_id):
    if request.method == 'POST':
        update_todo = to_do.objects.get(pk=todo_id)
        update_todo.title = request.POST['title']
        update_todo.description = request.POST['description']
        update_todo.save()
        return redirect('/home')
    
def delete(request,todo_id):
    delete_todo = to_do.objects.get(pk=todo_id)
    delete_todo.delete()
    return redirect('/home')

    

