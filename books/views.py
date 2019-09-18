from django.shortcuts import render,redirect
from .models import Books
# Create your views here.

from rest_framework import viewsets

from .meraform import BookForm,BookAPIForm
from accounts.models import Signup
def all_books(request):
    books = Books.objects.all()
    mydata ={
        'books':books
    }
    return render(request,'books/home.html',mydata)


def details(request,id=None):
    book=Books.objects.get(id=id)
    # print(books)
    mydic={
        'book':book
    }
    return render(request,'books/bdetails.html',mydic)

def add_post(request,id=None):
    if not request.session.get('email'):
        return redirect('login')

    l_u_email =request.session.get('email')
    l_user =Signup.objects.get(email=l_u_email)
    print(l_user)

    form =BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book_name =form.cleaned_data.get('book_name')
        book_price =form.cleaned_data.get('book_price')
        book_desc =form.cleaned_data.get('book_desc')
        book_image =form.cleaned_data.get('book_image')
        bookCot =form.cleaned_data.get('bookCot')
        location =form.cleaned_data.get('location')
        b =Books()
        b.book_name=book_name
        b.book_user=l_user
        b.book_price=book_price
        b.book_desc=book_desc
        b.book_image=book_image
        b.bookCot=bookCot
        b.location=location
        b.save()
        print('dddd')






    mydic={
        'form':form
    }
    return render(request,'books/add_book.html',mydic)




class PostApi(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookAPIForm