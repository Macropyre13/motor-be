from django.db import models

class Gejala(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Kerusakan(models.Model):
    nama        = models.CharField(max_length=255)
    deskripsi    = models.TextField()
    solusi      = models.TextField()
    gambar      = models.ImageField(upload_to='kerusakan/', null=True)

    def __str__(self):
        return self.nama
    
class BasisPengetahuan(models.Model):
    kode_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    kode_kerusakan = models.ForeignKey(Kerusakan, on_delete=models.CASCADE)
    bobot = models.FloatField()

    def __str__(self):
        return f"{self.kode_gejala} -> {self.kode_kerusakan} = {self.bobot}"

class DataKasus(models.Model):
    kerusakan = models.ForeignKey(Kerusakan, on_delete=models.CASCADE)
    list_gejala = models.TextField()
    hasil = models.FloatField()

    def __str__(self):
        return f'{self.kerusakan}'


class Riwayat(models.Model):
    nama = models.CharField(max_length=255)
    tgl = models.DateTimeField()
    result = models.TextField()

    def __str__(self):
        return self.nama

class UserModel(models.Model):
    username    = models.CharField(max_length=200)
    email       = models.EmailField()
    password1   = models.CharField(max_length=255)
    password2   = models.CharField(max_length=255)

    def __str__(self):
        return self.username