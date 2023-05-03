from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from libraio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'books.views.tr_handler403'
handler404 = 'books.views.tr_handler404'
handler500 = 'books.views.tr_handler500'
