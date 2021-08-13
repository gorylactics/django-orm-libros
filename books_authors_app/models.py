from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f'{self.title} {self.desc}'
    def __str__(self):
        return f'{self.title} {self.desc}'

class Author(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    notas = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name='authors')
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

