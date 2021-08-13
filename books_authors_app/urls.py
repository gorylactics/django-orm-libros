from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('procesarLibro' , views.procesarLibro),
    path('book/<int:id>', views.book),
    path('authors', views.authors),
    path('author/<int:id>', views.author),
]
