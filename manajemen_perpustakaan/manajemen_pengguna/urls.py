from django.urls import path
from .views import DaftarPengguna

urlpatterns = [
    path('pengguna/', DaftarPengguna.as_view(), name='daftar_pengguna'),
]
