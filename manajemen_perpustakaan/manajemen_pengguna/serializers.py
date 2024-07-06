from rest_framework import serializers
from .models import Pengguna

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ['id', 'username', 'nama_lengkap', 'email', 'is_admin']