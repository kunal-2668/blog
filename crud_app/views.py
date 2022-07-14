from django.shortcuts import redirect, render
from crud_app.forms import Detail_form , Blog_form
from .models import Detail , Blog , Todo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('main')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('main')

            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                return redirect('main')
        else:
            messages.info(request,'Try Matching Password')
            return redirect('main')
    else:
        return render(request,'main.html')

def login(request):
    if request.method == "POST":
        username = request.POST['lusername']
        password = request.POST['lpassword']

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username/password')
            return redirect('login')     
    else:
        return render(request,'main.html') 

def logout(request):
    auth.logout(request)
    return redirect('main')

@login_required(login_url='login')
def home(request):
    data_list = Blog.objects.get_queryset().order_by('id')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(data_list,2)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request,'home.html',{'data':data})
    

def add_blog(request):
    if request.method == 'GET':
        form = Blog_form()
        return render (request,'blogform.html',{'form':form})

    else:
        form = Blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

def register(request):
    if request.method == 'GET':
        form = Detail_form()

        return render (request,'registerform.html',{'form':form})

    else:
        form = Detail_form(request.POST)
        print(form)
        if form.is_valid():
            form.save()

            return redirect('registeration')

def showdata(request):
    data = Detail.objects.all()
    return render (request,'showdata.html',{'data':data})

def update(request,id):
    if request.method == "GET":
        s = Detail.objects.get(id=id)
        form = Detail_form(instance=s)
        return render(request,'updatedata.html',{'s':form})
    else:
        s = Detail.objects.get(id=id)
        form = Detail_form(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('showdata')

def delete(request,id):
    deletedata = Detail.objects.get(id=id)
    deletedata.delete()

    return redirect('showdata')

def search(request):
        searchinp = request.POST['search']
        data = Detail.objects.filter(name__contains=searchinp)
        return render(request,'showdata.html',{'data':data})


def TodoList(request):
    if request.method == 'POST':
        data = request.POST['todo']
        s = Todo(item=data)
        s.save()
        return redirect('Todo')

    else:
        tododata = Todo.objects.all()
        return render(request,'todolist.html',{'data':tododata})

def Deletetodo(request,id):
    tododata = Todo.objects.get(id=id)
    tododata.delete()
    return redirect('Todo')