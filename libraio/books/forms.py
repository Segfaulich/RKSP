from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Жанр не выбран"

    class Meta:
        model = Book
        fields = '__all__'  # ['title', 'author', 'cover', 'description', 'genre']
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-textarea'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'cover': forms.FileInput(attrs={'accept': '.jpeg,.jpg,.png'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        if Book.objects.filter(title__iregex=title).exists():
            raise forms.ValidationError('Запись с таким названием уже существует')

        return title

    def clean_cover(self):
        cover = self.cleaned_data['cover']
        if cover:
            allowed_formats = ['jpeg', 'jpg', 'png']
            file_extension = cover.name.split('.')[-1].lower()
            if file_extension not in allowed_formats:
                raise ValidationError('Формат файла должен быть JPEG, JPG или PNG')
        return cover


class DeleteReqForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].empty_label = "Книга не выбрана"

    class Meta:
        model = DeleteRequest
        fields = ['book', 'reason']
        widgets = {
            'reason': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))