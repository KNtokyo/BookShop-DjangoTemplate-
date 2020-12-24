from django.db import models

CHOICES = (
    ('in stock', 'В наличии'),
    ('out of stock', 'Нет в наличии')
)

class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=80, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Genre(models.Model):
    slug = models.SlugField(primary_key=True, max_length=20)
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book', blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title} - {self.author}'

