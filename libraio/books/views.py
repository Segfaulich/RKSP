from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from .forms import *
from .utils import *


class BookListView(DataMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, TemplateView):
    template_name = 'books/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class AddBookView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'books/add_book.html'

    success_url = reverse_lazy('list')
    login_url = reverse_lazy('list')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class DeleteReqView(LoginRequiredMixin, DataMixin, FormView):
    form_class = DeleteReqForm
    template_name = 'books/delete_request.html'

    success_url = reverse_lazy('list')
    login_url = reverse_lazy('list')
    raise_exception = True

    def form_valid(self, form):
        delete_request = form.save(commit=False)
        delete_request.user = self.request.user
        delete_request.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class ShowBookView(DataMixin, DetailView):
    model = Book
    template_name = 'books/book.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['book'])

        return dict(list(context.items()) + list(c_def.items()))


class BookGenreView(DataMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(genre__id=self.kwargs['genre_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO", genre_selected=context['books'][0].genre_id)

        return dict(list(context.items()) + list(c_def.items()))


class BookSearchView(DataMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Результаты поиска")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'books/auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'books/auth/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='books/exceptions/error_page.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена',
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='books/exceptions/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return redirect('login')
    # return render(request=request, template_name='books/exceptions/error_page.html', status=403, context={
    #     'title': 'Ошибка доступа: 403',
    #     'error_message': 'Доступ к этой странице ограничен',
    # })
