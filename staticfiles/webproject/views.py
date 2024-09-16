from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from picproject.forms import Imageform,SignUpForm
from picproject.models import picproj
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def pic(request):
    if request.method == "POST":
        form=Imageform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    img=picproj.objects.all()
    return render(request,'uploadpic1.html',{'img':img ,'form':form})
#def pic(request):
   # a=''
    #if request.method == "POST":
        #pic=request.POST['pic']
       # imagedesc=request.POST['imagedesc']
       # userid=request.POST['userid']
       # data=picproj(pic_image=pic,user_id=userid,image_title=imagedesc)
       # data.save()
       # a='Image Successfully upload'
    #img=picproj.objects.all()
    #return render(request,'uploadpic1.html',{'img':img ,'a':a})

def login_page(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass']
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('/picproj/')
        else:
            messages.info(request,'Username or Password is Incorrect!!!')
            return redirect('/loginpage/')
    return render(request,'login1.html')

def delete_image(request,im):
    if request.method=="POST":
        img = picproj.objects.get(id=im)
        img.delete()
    return redirect('/picproj/')

def product(request,pk):
    prod = picproj.objects.get(id=pk)
    return render(request,'product.html',{'product': prod})


def logout_page(request):
    logout(request)
    return redirect('loginpage')

def register_page(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request,'Username already exists')
            return HttpResponseRedirect('/register/')

        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created Successfully')
        return HttpResponseRedirect('/register/')
    return render(request,'register1.html')

def homepage(request):
    return HttpResponse("Welcome to Haridwar")
def register1(request):
    return render(request,"register1.html")
def login1(request):
    return render(request,"login1.html")
def picupload(request):
    return render(request,"picupload.html")

def Aboutus(request):
    return render(request,"index.html")

def works(request):
    return render(request,"works.html")

def user(request):
    res=0
    data={}
    try:
        if request.method=="POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            res = n1+n2
            data={
                    'n1':n1,
                    'n2':n2,
                    'res':res
            }
            url="/thanku/?output={}".format(res)
            return HttpResponseRedirect(url)
    
    except: 
        pass   
        
    return render(request,"userform.html",data)

def thanku(request):
    if request.method=="GET":
        output=request.GET['output']
    return render(request,"Thankyou.html",{'output':output})