from django.shortcuts import HttpResponse


# Create your views here.

# In case the user doesn't know an specific address, he/she is greeted
def hello_generic(requests, name="world", age=3500000000):
    return HttpResponse(
        f"<h1>Hello, person (whose name I don't know, yet),</h1><h2>On this page you can type some info to show in "
        f"the URL. Like in the example below:</h2><h3>Hello, {name}!</h3><h3>I'm aware that you are {age} years old.</h3>"
        f"<h3>Watch out... 👀🐱‍👤 </h3><h2>To produce the result you saw, type the original URL, adding the "
        f"following: \"/hello/your_name/your_age\"</h2><h4>Otherwise, if you are staff, type '/admin'</h4>")


def hello_custom(requests, name="world", age=3500000000):
    return HttpResponse(
        f"<h1>Hello, {name}!</h1><h2>I'm aware that you are {age} years old. </h2><h3>Watch out... 👀🐱‍👤 </h3>")
