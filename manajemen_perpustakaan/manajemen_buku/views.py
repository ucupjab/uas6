from rest_framework import generics
from .models import Buku
from .serializers import BukuSerializer

class DaftarBuku(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
