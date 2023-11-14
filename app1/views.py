from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register,Blog

# Create your views here.
def display(request):
    return render(request,'register.html')


def display2(request):
    return render(request,'login.html')


def backtoregister(request):
    return redirect(display)
def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            data = Register.objects.create(username=username, email=email, password=password)
            data.save()
            return render(request, "login.html")
        except Exception:
            return render(request, 'register.html', {'note': "username already exists!"})
    else:
        return redirect(backtoregister)

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            data1 = Register.objects.get(email=email)
            if data1.password == password:
                request.session['id'] = data1.id
                return redirect(home)
            else:
                return render(request, 'login.html', {'msg': "password error"})
        except Exception:
            return render(request, 'login.html', {'msg1': "email error"})
    else:
        return render(request,'login.html')
def home(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
        data2 = Blog.objects.all()
        return render(request, 'home.html', {'data': data, 'data2': data2})
    else:
        return redirect(display2)

def profile(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            return render(request,'profile.html',{'data':data})
    else:
        return redirect(display2)


def update_profile(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method == "POST":
            newuser = request.POST['newuser']
            newemail = request.POST['newemail']
            newpass = request.POST['newpassword']
            try:
                data = Register.objects.get(id=username)
                data.username = newuser
                data.email = newemail
                data.password = newpass
                data.save()
                return HttpResponse("Information updated succesfully")
            except Exception:
                return HttpResponse("Some error has occurred")
    else:
        return redirect(display2)

def blog(request):
    if 'id' in request.session:
        return render(request,'blog.html')
    else:
        return redirect(display2)


def save_blog(request):
    if 'id' in request.session:
        username=request.session['id']
        try:
            title = request.POST['title']
            content = request.POST['content']
            user=Register.objects.get(id=username)
            data = Blog.objects.create(username=user, title=title, content=content)
            data.save()
            return redirect(home)
        except Exception:
            return HttpResponse("Error occurred")
    else:
        return redirect(display2)


