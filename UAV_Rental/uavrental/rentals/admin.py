from django.contrib import admin
from .models import UAV, Rental

# Rental modeli için Admin konfigürasyonu
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    # Admin panelinde görüntülenecek alanlar
    list_display = ['uav', 'date_start', 'date_end', 'renting_member']
    # Arama alanları
    search_fields = ['uav__brand', 'uav__model', 'renting_member__username']

# UAV modeli için Admin konfigürasyonu
@admin.register(UAV)
class UAVAdmin(admin.ModelAdmin):
    # Admin panelinde görüntülenecek alanlar
    list_display = ['brand', 'model', 'weight', 'category']
    # Arama alanları
    search_fields = ['brand', 'model']
