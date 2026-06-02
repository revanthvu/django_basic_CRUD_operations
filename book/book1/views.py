

# Create your views here.
import json
from http import HTTPStatus
from multiprocessing import context

from django.http import JsonResponse
from django.http.response import  HttpResponse
from django.views.decorators.csrf import csrf_exempt

from.models import *

@csrf_exempt
def add_book(request):
    if request.method=='POST':
        data= json.loads(request.body)
        book_data=book.objects.create(
            id=data['id'],
            title=data['title'],
            author=data['author'],
            price=data['price'],
        )
        return JsonResponse({
            "name":book_data.name,
            "status": HTTPStatus.OK
        })

from django.shortcuts import render

def netflix_home(request):
    return render(request, 'index.html')
def home_view(request):
    return render(request, 'home.html')

def programming_view(request):
    return render(request, 'programming.html' , context={"role": "admin"})

def academic_view(request):
    return render(request, 'academic.html')
def portfolio_view(request):
    return render(request, 'portfolio.html')
def contact(request):
    return render(request, 'contact.html')
def grade(request,marks):
    return render(request, 'grade.html', context={"grade":marks})
def table(request):
    return render(request, 'tableforloop.html',context={
                   "user_data":
                       [
                           {"name": "Pavan" , "email":"pavan@email.com"},
                           {"name": "Sai", "email":"sai@email.com"},
                           {"name": "Ganesh" , "email":"ganesh@email.com"}
                       ]
                   })
def add_user(request):
    # here we are receiving the data from browser and storing it int the db
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        data=UserMode.objects.create(
            name=name,
            email=email
        )
        return HttpResponse("success, User added")
    return render(request, "user_form.html")
def view_books(request):

    books = Book.objects.all()

    output = ""

    for book in books:
        output += f"""
        Name : {book.title}<br>
        Author : {book.author}<br>
        Price : {book.price}<br><br>
        """

    return HttpResponse(output)