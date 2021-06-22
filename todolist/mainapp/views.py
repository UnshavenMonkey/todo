from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from mainapp.models import Utask, Category
from authapp.models import TaskUser




def index(request):
    task_list = []
    category_list = []
    if request.user.is_authenticated:
        task_list = request.user.tasks.all()
        category_list = Category.objects.all()
        

    return render(request, 'mainapp/index.html', {'task_list': task_list, 'category_list': category_list})

def by_category(request):
    pass

def add_task(request):
    category_list = Category.objects.all()
    if not category_list:
        Category.objects.create(category_name='Home')
        category_list = Category.objects.all()
    if request.method == 'POST':
        Utask.objects.create(title=request.POST.get('title'), author=request.user,
                             category=Category.objects.get(category_name=request.POST.get('cat.category_name')))
        
        return redirect(index)
    else:
        return render(request,'mainapp/add.html', {'category_list': category_list})

def delete_task(request, id):
    task = Utask.objects.get(id=id)
    task.delete()
    return redirect(index)


def add_category(request):

    category_list = Category.objects.all()
    if not category_list:
        Category.objects.create(category_name='Home')
        category_list = Category.objects.all()
    if request.method == 'POST':
        Category.objects.create(category_name=request.POST.get('categoryname'))
        
        return redirect(index)
    else:
        return render(request,'mainapp/add_category.html', {'category_list': category_list})

def filter_category(request, category_name):
    
    category_name = Category.objects.get(category_name=category_name)
    category_list = []
    if request.user.is_authenticated:
        task_list = request.user.tasks.filter(category__category_name=category_name)
        category_list = Category.objects.all()
    return render(request, 'mainapp/index.html', {'task_list': task_list, 'category_list': category_list})


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(index)


def complite_task(request, id):
    task = Utask.objects.get(id=id)
    if task.achievement == False:
        task.achievement = True
    else:
        task.achievement = False
    task.save()

    return redirect(index)