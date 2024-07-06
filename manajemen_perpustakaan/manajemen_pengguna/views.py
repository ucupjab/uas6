from rest_framework import generics
from .models import Pengguna
from .serializers import PenggunaSerializer

class DaftarPengguna(generics.ListCreateAPIView):
    queryset = Pengguna.objects.all()
    serializer_class = PenggunaSerializer
