from django.shortcuts import render, HttpResponse
# Create your views here.

# In case the user doesn't know an specific address, he/she is greeted
def hello(requests,name="world",age=3500000000):
    return HttpResponse(f"<h1>Hello, {name}!</h1><h2>I'm aware that you are {age} years old. </h2><h3>Watch out... 👀🐱‍👤 </h3>")
