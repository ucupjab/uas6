# Generated by Django 5.0.6 on 2024-07-05 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('penulis', models.CharField(max_length=255)),
                ('penerbit', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('status', models.CharField(default='tersedia', max_length=50)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buku', to='manajemen_buku.kategori')),
            ],
        ),
    ]