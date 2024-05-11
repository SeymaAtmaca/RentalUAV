
from django.contrib import admin
from django.urls import path
from rentals.views import HomeView, RentalCreateView
from rentals import views
from django.urls import path, include
from accounts import urls
from django.contrib import admin
from django.urls import path, include
from rentals.views import HomeView, RentalCreateView
from accounts import urls as accounts_urls
from django.contrib.auth.views import LoginView
from accounts import views as v

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Ana sayfa için
    path('admin/', admin.site.urls),  # Admin paneli için
    path('accounts/', include(accounts_urls)),  # Kullanıcı hesapları için
    path('login/', LoginView.as_view(), name='login'),  # Giriş yapma sayfası için
    path('accounts/profile/', v.profile_view, name='profile'),  # Kullanıcı profili için
    path('uav/', views.UAVListView.as_view(), name='uav-list'),  # UAV listesi için
    path('uav/<int:pk>/', views.UAVDetailView.as_view(), name='uav-detail'),  # Belirli bir UAV detayı için
    path('uav/create/', views.UAVCreateView.as_view(), name='uav-create'),  # UAV oluşturma için
    path('uav/<int:pk>/update/', views.UAVUpdateView.as_view(), name='uav-update'),  # Belirli bir UAV güncelleme için
    path('uav/<int:pk>/delete/', views.UAVDeleteView.as_view(), name='uav-delete'),  # Belirli bir UAV silme için
    path('rental/', views.RentalListView.as_view(), name='rental-list'),  # Kiralama listesi için
    path('rental/<int:pk>/', views.RentalDetailView.as_view(), name='rental-detail'),  # Belirli bir kiralama detayı için
    path('rental/create/', RentalCreateView.as_view(), name='rental-create'),  # Kiralama oluşturma için
    path('rental/<int:pk>/update/', views.RentalUpdateView.as_view(), name='rental-update'),  # Belirli bir kiralama güncelleme için
    path('rental/<int:pk>/delete/', views.RentalDeleteView.as_view(), name='rental-delete'),  # Belirli bir kiralama silme için

]
