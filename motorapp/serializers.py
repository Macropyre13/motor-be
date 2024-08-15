from rest_framework import serializers
from . import models

class GejalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gejala
        fields = '__all__'

class KerusakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kerusakan
        fields = '__all__'

class BasisPengetahuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasisPengetahuan
        fields = '__all__'

class DataKasusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataKasus
        fields = '__all__'

class RiwayatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Riwayat
        fields = '__all__'
        