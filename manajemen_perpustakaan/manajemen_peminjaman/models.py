from django.db import models
from manajemen_pengguna.models import Pengguna
from manajemen_buku.models import Buku

class Peminjaman(models.Model):
    pengguna = models.ForeignKey(Pengguna, related_name='peminjaman', on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, related_name='peminjaman', on_delete=models.CASCADE)
    tanggal_peminjaman = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='dipinjam')

    def __str__(self):
        return f"{self.pengguna.username} meminjam {self.buku.judul}"
