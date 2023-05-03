from .models import *

menu = [
    {'title': "Список книг", 'url_name': 'list'},
    {'title': "Добавить книгу", 'url_name': 'add_book'},
    {'title': "Удаление книги", 'url_name': 'delete_req'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['genres'] = genres

        if 'genre_selected' not in context:
            context['genre_selected'] = 0

        return context
