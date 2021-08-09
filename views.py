from django.shortcuts import render, HttpResponse, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/schedule')
        else:
            messages.error(request,"Invalid user or password")
    return redirect('/login')

@login_required(login_url='/login/')
def events_list(request):
    user = request.user
    event = Event.objects.filter(users=user)
    response = {'events': event}
    return render(request, 'schedule.html', response)


# In case the user doesn't know an specific address, he/she is greeted
def hello_generic(requests, name="world", age=3500000000):
    return HttpResponse(
        "<title>Welcome 🖐🏽 </title>"
        f"<h1>Hello, person (whose name I don't know, yet),</h1><h1>On this page you can do the following:</h1><h2> "
        f"1) Type some info in the URL to customize the page. Like in the example below:</h2> "
        f"</h2><h3>'Hello, {name}!</h3><h3>I'm aware that you are {age} years old.</h3>"
        f"<h3>Watch out...' 👀🐱‍👤 </h3><h3>*To produce the result you saw, type the original URL, adding the "
        f"following: \"/hello/your_name/your_age\"</h3>"
        f"<h2>  2) Visit the ADMIN page of the company, if you are staff.</h2>"
        f"<h3>You can do that by replacing: '/hello' with '/admin' in the URL</h3>"
        f"<h2>  3) To check your schedule, if you are staff and connected.</h2>"
        f"<h3>You need to replace: '/hello' with '/schedule' in the URL</h3>"
    )


def hello_custom(requests, name="world", age=3500000000):
    return HttpResponse(
        f"<h1>Hello, {name}!</h1><h2>I'm aware that you are {age} years old. </h2><h3>Watch out... 👀🐱‍👤 </h3>")
