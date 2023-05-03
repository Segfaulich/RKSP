from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'modified_date', 'cover')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('publication_date',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


class DeleteReqAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'reason', 'req_date')
    list_display_links = ('book',)
    search_fields = ('book', )


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(DeleteRequest, DeleteReqAdmin)
