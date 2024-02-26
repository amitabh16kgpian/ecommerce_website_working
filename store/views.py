from django.shortcuts import render, redirect
from .models import Product, Catergory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {"products": products})

def about(request):
    return render(request, 'about.html',{})

def login_user(request):
    if( request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)  
        if user is not None:
            login(request, user)
            messages.success(request, "You successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Enter your credentials correctly!")
            return redirect('login')
    else:    
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.....")
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username= username, password = password)
            login(request, user)
            messages.success(request, ("You Have Registered Successfully"))
            return redirect('home')
        else:
            messages.success(request, ("Oops!, Register with proper user name and password"))
            return redirect('register')
    else:  
        return render(request, 'register.html' , {'form':form})

def view_product(request, pk):
    product = Product.objects.get(id = pk)
    return render(request, 'view_product.html',{"product":product })

def view_by_categories(request, catg):
    category = Catergory.objects.get(name = catg)
    # here category is an object
    catg = catg.replace('-',' ')
    products = Product.objects.filter(category = category.id)
    return render(request,'view_by_categories.html',{'products': products, 'category': catg})