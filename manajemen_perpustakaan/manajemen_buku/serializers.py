from rest_framework import serializers
from .models import Buku, Kategori

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class BukuSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = (
        ('tersedia', 'Tersedia'),
        ('tidak tersedia', 'Tidak Tersedia'),
    )

    kategori = KategoriSerializer()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Buku
        fields = ['id', 'judul', 'penulis', 'penerbit', 'isbn', 'kategori', 'status']

    def create(self, validated_data):
        kategori_data = validated_data.pop('kategori')
        kategori = Kategori.objects.create(**kategori_data)
        buku = Buku.objects.create(kategori=kategori, **validated_data)
        return buku