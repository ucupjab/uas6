from django.urls import path
from .views import DaftarBuku

urlpatterns = [
    path('buku/', DaftarBuku.as_view(), name='daftar_buku'),
]
