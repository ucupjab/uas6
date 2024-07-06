from rest_framework import generics
from .models import Peminjaman
from .serializers import PeminjamanSerializer

class DaftarPeminjaman(generics.ListCreateAPIView):
    queryset = Peminjaman.objects.all()
    serializer_class = PeminjamanSerializer
