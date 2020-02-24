from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View functions for home page of site."""
    
    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #The all() in implied ny default.
    num_authors = Author.objects.count()

    # Number of visits to the view , as counted in the session variable
    num_visits = request.session.get('num_visists', 0)
    request.session['num_visists'] = num_visits + 1

    # genres and books that contain the word 'the'
    num_thes = Book.objects.filter(title__icontains='the').count()
    num_thes += Genre.objects.filter(name__icontains='the').count()


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_thes': num_thes,
        'num_visits': num_visits
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author