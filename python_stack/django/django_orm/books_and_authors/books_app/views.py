from django.shortcuts import render , redirect
from .models import Book , Author

# Create your views here.
def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "Book/index.html" , context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc']
        )   
    return redirect('/') 


def book_details(request,book_id):
    current_book = Book.objects.get(id = book_id)
    context = {
        'book': current_book,
        'available_authors': Author.objects.exclude(books=current_book)
    }
    return render(request , 'Book/book_detail.html' , context)

def add_author_to_book(request , book_id):
    if request.method == 'POST':
        book = Book.objects.get(id = book_id)
        author = Author.objects.get(id = request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}')


def authors_index(request):
    context = {
        'authors': Author.objects.all()
    }  
    return render(request , "Author/authors.html" , context)  

def add_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes']
        )

    return redirect('/authors') 

def author_details(request , author_id):
    current_author = Author.objects.get(id = author_id)
    context = {
        'author': current_author,
        'availabel_books': Book.objects.exclude(authors = current_author)
    }
    return render(request, 'Author/author_detail.html',context)

def add_book_to_author(request,author_id):
    if request.method == 'POST':
        author = Author.objects.get(id = author_id)
        book = Book.objects.get(id = request.POST['book_id'])  
        author.books.add(book)
    return redirect(f'/authors/{author_id}')      
        

