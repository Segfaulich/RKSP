from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutView.as_view(), name='main'),
    path('list/', BookListView.as_view(), name='list'),
    path('add_book/', AddBookView.as_view(), name='add_book'),

    path('delete_req/', DeleteReqView.as_view(), name='delete_req'),
    path('delete_list/', DeleteListView.as_view(), name='delete_list'),
    path('delete_list/<int:delete_req_id>/reject/', DeleteRejectView.as_view(), name='delete_req_reject'),
    path('delete_list/<int:delete_req_id>/approve/', DeleteApproveView.as_view(), name='delete_req_approve'),

    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),

    path('list/book/<int:book_id>/', ShowBookView.as_view(), name='book'),
    path('list/book/<int:book_id>/delete', BookDeleteView.as_view(), name='book_delete'),

    path('list/genre/<int:genre_id>/', BookGenreView.as_view(), name='genre'),
    path('list/search/', BookSearchView.as_view(), name='search')
]
