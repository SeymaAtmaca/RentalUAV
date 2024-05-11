from django.db import models
from django.contrib.auth.models import User

# UAV 
class UAV(models.Model):
    # Marka
    brand = models.CharField(max_length=100)
    # Model
    model = models.CharField(max_length=100)
    # Ağırlık
    weight = models.FloatField()
    # Kategori
    category = models.CharField(max_length=100)

    # Nesneyi dize olarak temsil ederken kullanılacak metot
    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        # Veritabanındaki uygulama adı
        app_label = 'rentals'


# Kiralama modeli
class Rental(models.Model):
    # Kiralanacak UAV (Unmanned Aerial Vehicle - İnsansız Hava Aracı)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    # Kiralamanın başlangıç tarihi
    date_start = models.DateTimeField()
    # Kiralamanın bitiş tarihi
    date_end = models.DateTimeField()
    # Kiralayan üye
    renting_member = models.ForeignKey(User, on_delete=models.CASCADE)

    # Nesneyi dize olarak temsil ederken kullanılacak metot
    def __str__(self):
        return f"Rental #{self.pk} - {self.uav.brand} {self.uav.model} - {self.renting_member.username}"

    class Meta:
        # Veritabanındaki uygulama adı
        app_label = 'rentals'
