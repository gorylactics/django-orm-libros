from django.shortcuts import render , redirect
from .models import *

def index(request):
    if request.method == 'GET':
        contexto = {'libros' : Book.objects.all()}
        return render(request, 'books_authors_app/index.html', contexto)

def procesarLibro(request):
    if request.method == 'POST':
        print(request.POST)
        libro = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['description']
        )
        return redirect('/')

def book(request, id):
    libro = Book.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
                'libro' : libro,
                'autores': Author.objects.all(),
                'autorizados' : Book.objects.all()
            }
        return render(request , 'books_authors_app/book.html', contexto)
    if request.method == 'POST':
        autor = Author.objects.get(id = request.POST['opcion'])
        libro.authors.add(autor)
        return redirect(f'/book/{id}')

def authors(request):
    if request.method == 'GET':
        contexto = {
            'autores' : Author.objects.all()
        }
        return render(request, 'books_authors_app/authors.html', contexto)
    if request.method == 'POST':
        print(request.POST)
        autorNuevo = Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notas = request.POST['notas'],
        )
        return redirect('/authors')

def author(request, id):
    
    autor = Author.objects.get(id = id)
    libro = Book.objects.all
    
    if request.method == 'GET':
        contexto = {
            'autor' : autor,
            'libro' : libro
            }
        return render(request, 'books_authors_app/author.html', contexto)
    
    if request.method == 'POST':
        libro = Book.objects.get(id = request.POST['opcion'])
        autor.books.add(libro)
        return redirect(f'/author/{id}')


