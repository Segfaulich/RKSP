from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Book(models.Model):

    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(blank=True, verbose_name="Описание")
    cover = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Обложка")

    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, verbose_name="Жанр")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-publication_date', 'title']


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Жанр")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['id']


class DeleteRequest(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='delete_requests', verbose_name='Книга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    reason = models.TextField(blank=True, verbose_name='Причина удаления')
    req_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'

    class Meta:
        verbose_name = 'Запрос на удаление книги'
        verbose_name_plural = 'Запросы на удаление книги'
        ordering = ['-req_date']