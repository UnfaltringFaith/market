from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import UserForm
# Create your views here.

def test(request):
    langs = ["rus", "eng", "bel", "pol"]
    return render(request, "index.html", context={"n": 6, "body": "<h1>SEX</h1>", "langs": langs})

def index(request: HttpRequest):
    if(request.method == "POST"):
        name = request.POST.get("name")
        age = request.POST.get("age")
        isStudent = request.POST.get("student")
        return HttpResponse(f"<h2>name: {name}, age: {age}, Stident:{isStudent} {"Student" if isStudent == True else "Free"} </h2>")
    else:
        userForm = UserForm()
        return render(request, "index.html", {"form": userForm})
            
def postuser(request: HttpRequest):
    name = request.POST.get("name","None")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist('languagues', ["python"])
    return HttpResponse(f"<h2>name: {name}, age: {age}, languagues: {langs}</h2>")