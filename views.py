from django.shortcuts import render, HttpResponse
#from core.models import Pessoa
# Create your views here.

def hello(requests,name="world",age=3500000000):
    return HttpResponse(f"<h1>Hello, {name}!</h1><h2>I'm aware that you are {age} years old. </h2><h3>Watch out... 👀🐱‍👤 </h3>")


# class PessoaAdmin(admin.modelAdmin):
#     list_display = ('name','idade')
#     list_filter = ('name')
#
# admin.site.register(Pessoa)