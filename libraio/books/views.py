from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView, DeleteView, UpdateView
from django.views.generic.base import View

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
    form_class = AddBookForm
    template_name = 'books/add_book.html'

    success_url = reverse_lazy('list')
    login_url = reverse_lazy('list')
    raise_exception = True

    def form_valid(self, form):
        add_book_request = form.save(commit=False)
        add_book_request.user = self.request.user
        add_book_request.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('list')
    raise_exception = True

    def test_func(self):
        book = self.get_object()
        return self.request.user.is_authenticated and (self.request.user.is_superuser or book.user == self.request.user)

    def get_object(self, queryset=None):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        return book


class DeleteListView(DataMixin, ListView):
    model = DeleteRequest
    template_name = 'books/delete_list.html'
    context_object_name = 'delete_requests'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="LibraIO")

        return dict(list(context.items()) + list(c_def.items()))


class DeleteRejectView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DeleteRequest
    success_url = reverse_lazy('delete_list')
    raise_exception = True

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get_object(self, queryset=None):
        delete_req_id = self.kwargs.get('delete_req_id')
        delete_req = get_object_or_404(DeleteRequest, id=delete_req_id)
        return delete_req


class DeleteApproveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DeleteRequest
    success_url = reverse_lazy('delete_list')
    raise_exception = True

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def form_valid(self, form):
        book = self.get_object().book  # Get the associated book
        book.delete()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        delete_req_id = self.kwargs.get('delete_req_id')
        delete_req = get_object_or_404(DeleteRequest, id=delete_req_id)
        return delete_req


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


class RegisterUserView(DataMixin, UserPassesTestMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'books/auth/register.html'

    def test_func(self):
        return not self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUserView(DataMixin, UserPassesTestMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'books/auth/login.html'

    def test_func(self):
        return not self.request.user.is_authenticated

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
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, '
                         'отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    if request.user.is_authenticated:
        return redirect('main')
    else:
        return redirect('login')
    # return render(request=request, template_name='books/exceptions/error_page.html', status=403, context={
    #     'title': 'Ошибка доступа: 403',
    #     'error_message': 'Доступ к этой странице ограничен',
    # })
