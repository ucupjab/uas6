from django.urls import path
from .views import DaftarPeminjaman

urlpatterns = [
    path('peminjaman/', DaftarPeminjaman.as_view(), name='daftar_peminjaman'),
]