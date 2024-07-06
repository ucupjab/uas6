from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    kategori = models.ForeignKey(Kategori, related_name='buku', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='tersedia')

    def __str__(self):
        return self.judul
