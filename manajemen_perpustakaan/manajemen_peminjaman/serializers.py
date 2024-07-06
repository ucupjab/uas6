from rest_framework import serializers
from .models import Peminjaman
from manajemen_pengguna.models import Pengguna
from manajemen_buku.models import Buku

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ['id', 'username']  # Sesuaikan dengan field yang ingin Anda sertakan

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id', 'judul']  # Sesuaikan dengan field yang ingin Anda sertakan

class PeminjamanSerializer(serializers.ModelSerializer):
    pengguna = PenggunaSerializer()
    buku = BukuSerializer()

    class Meta:
        model = Peminjaman
        fields = ['id', 'pengguna', 'buku', 'tanggal_peminjaman', 'tanggal_pengembalian', 'status']

    def create(self, validated_data):
        pengguna_data = validated_data.pop('pengguna')
        buku_data = validated_data.pop('buku')

        pengguna = Pengguna.objects.get_or_create(**pengguna_data)[0]
        buku = Buku.objects.get_or_create(**buku_data)[0]

        peminjaman = Peminjaman.objects.create(
            pengguna=pengguna,
            buku=buku,
            **validated_data
        )
        return peminjaman

    def update(self, instance, validated_data):
        pengguna_data = validated_data.pop('pengguna')
        buku_data = validated_data.pop('buku')

        instance.pengguna.username = pengguna_data.get('username', instance.pengguna.username)
        instance.buku.judul = buku_data.get('judul', instance.buku.judul)
        instance.tanggal_peminjaman = validated_data.get('tanggal_peminjaman', instance.tanggal_peminjaman)
        instance.tanggal_pengembalian = validated_data.get('tanggal_pengembalian', instance.tanggal_pengembalian)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
