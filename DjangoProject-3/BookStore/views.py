from django.shortcuts import render
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book
# Create your views here.
def index(request):
    book = Book.objects.all()
    context = {
        'book' : book
    }
    return render(request, "ex3/index.html", context)


def registerAuthor(request):

    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid:
            ftmp = form.save()
            ftmp.save
        context = {
            'form' : form,
            'submitted' : True

        }
        return render (request, "ex3/registerAuthor.html", context)

    
    elif request.method == "GET":
        form = AuthorForm()
        context = {
            'form' : form

        }
    return render (request, "ex3/registerAuthor.html", context)


def registerPublisher(request):

    if request.method == "POST":
        form = PublisherForm(request.POST)

        if form.is_valid:
            ftmp = form.save()
            ftmp.save
        context = {
            'form' : form,
            'submitted' : True

        }
        return render (request, "ex3/registerPublisher.html", context)

    elif request.method == "GET":
        form = PublisherForm()
        context = {
            'form' : form

        }
    return render (request, "ex3/registerPublisher.html", context)

def publishBook(request):

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            print("done")
            author = request.POST.get('author')
            publisher = request.POST.get('publisher')
            form.author = author
            form.publisher = publisher
            ftmp = form.save()
            ftmp.save
        else:
            print("not valid")

        context = {
            'form':form,
            'submitted' : True
        }
        return render (request, "ex3/publishBook.html", context)


    elif request.method == "GET":
        form = BookForm()
        context = {
            'form' : form
        }
    return render (request, "ex3/publishBook.html", context)

