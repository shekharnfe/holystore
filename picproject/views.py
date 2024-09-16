from django.shortcuts import render,redirect
from django import forms
from .models import Product,Category,Profile,contactus
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm,UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.db.models import Q
import json
from cart.cart import Cart


# Create your views here.
#@login_required(login_url='login')
def home(request):
    products=Product.objects.all()
    return render(request, "home.html",{'products':products})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # Query the Products DB Model
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        # Test for null
        if not searched:
           messages.success(request, "That Product Does not exist...Please try Again...") 
           return render(request, "search.html",{})
        else:
            return render(request, "search.html",{'searched':searched}) 
    else:
        return render(request, "search.html",{})

def update_info(request):
    if request.user.is_authenticated:
        # Get current user
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get current user shipping info
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None , instance=current_user)
        # Get user shipping form
        shipping_form = ShippingForm(request.POST or None , instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            # save shipping form
            shipping_form.save()
            messages.success(request, "Your info has been Updated !!!")
            return redirect('home')
        return render(request, "update_info.html",{'form':form,'shipping_form':shipping_form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated, Please login again...")
                login(request, current_user)
                #return redirect('update_password')
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('update_password')

        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html",{'form':form})
    else:
         messages.success(request, "You must be logged in to view that page !!!")
         return redirect('home')   

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None , instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request, "User has been Updated !!!")
            return redirect('home')
        return render(request, "update_user.html",{'user_form':user_form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')


    

def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html",{'categories':categories})

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,"products.html",{'product':product})

def category(request,var):
    var = var.replace('-',' ')
    try:
        category = Category.objects.get(name=var)
        products = Product.objects.filter(category=category)
        return render(request, "category.html",{'products':products,'category':category})
    except:
        messages.info(request,'That Category Does not Exist')
        return redirect('home')

def about(request):
    return render(request, "about.html",{})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            # shopping cart stuff
            current_user = Profile.objects.get(user__id=request.user.id)
            #get their saved cart from database
            saved_cart = current_user.old_cart
            # convert database string to python dictionary
            if saved_cart:
                # convert to dict using json
                converted_cart = json.loads(saved_cart)
                # add the loaded cart dict to our session
                # Get the cart
                cart = Cart(request)
                # loop thru the cart and add the items from the database
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)


            #messages.success(request,("You have been logged in!!"))
            return redirect('home')
        else:
            messages.info(request,'Username or Password is Incorrect!!!')
            return redirect('login')
    else:
        return render(request, "login.html",{})


def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.info(request,'Username created - Please fill out your information')
            return redirect('update_info')
        else:
            messages.info(request,'Whoops! There is an error in Registering , Please try again!')
            return redirect('register')
    else:    
        return render(request, "register.html",{'form':form})
    
def index(request):
    return render(request,'index.html',{})

def contact(request):
    if request.method == 'POST':
        if request.POST['full_name'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
            saverec = contactus()
            saverec.full_name = request.POST['full_name']
            saverec.email = request.POST['email']
            saverec.subject = request.POST['subject']
            saverec.message = request.POST['message']
            saverec.save()
            messages.success(request,'Your message has been sent successfully !')
            return redirect('contact')
            
    else:    
            return render(request,'contact.html',{})

def contactinfo(request):
    cinfo = contactus.objects.all()
    return render(request,'contactinfo.html',{'cinfo': cinfo})        