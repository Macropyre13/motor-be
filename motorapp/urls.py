from django.urls import path
from . import views

urlpatterns = [
    path('gejala/', views.gejala_list),
    path('gejala/<int:id>', views.detail_gejala),
    path('kerusakan/', views.kerusakan_list),
    path('kerusakan/<int:id>', views.detail_kerusakan),
    path('basis-pengetahuan/', views.basispengetahuan_list),
    path('basis-pengetahuan/<int:id>', views.detail_bp),
    path('data-kasus/', views.kasus_list),
    path('data-kasus/<int:id>', views.detail_kasus),
    path('riwayat/', views.riwayat_list),
    path('riwayat/<int:id>', views.detail_riwayat)
]