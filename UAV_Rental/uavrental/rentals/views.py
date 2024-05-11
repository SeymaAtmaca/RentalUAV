from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UAV, Rental
from .forms import RentalForm

#Aşağıda her view' ın kulalnacağı model, uygulayacağı template, başarı durumlarında geri döneceği url' ler ( success) tanımlanmıştır.

class HomeView(ListView):
    # Anasayfada UAV listesi ve kiralama formunu içeren bir sayfa görüntülemek için kullanılır.
    model = UAV
    template_name = 'home.html'  

    def get_context_data(self, **kwargs):
        # Görünümün bağlam verilerini oluştururken, kiralama formunu ve oluşturma URL'sini ekler.
        context = super().get_context_data(**kwargs)
        context['rental_form'] = RentalForm()  
        context['rental_create_url'] = reverse_lazy('rental-create')
        return context

class UAVListView(ListView):
    # UAV listesini görüntülemek için kullanılır.
    model = UAV
    template_name = 'uav_list.html'

class UAVDetailView(DetailView):
    # Belirli bir UAV'nin ayrıntılarını görüntülemek için kullanılır.
    model = UAV
    template_name = 'uav_detail.html'

class UAVCreateView(CreateView):
    # Yeni bir UAV oluşturmak için kullanılır.
    model = UAV
    template_name = 'uav_form.html'
    fields = ['brand', 'model', 'weight', 'category']
    success_url = reverse_lazy('profile')

class UAVUpdateView(UpdateView):
    # Mevcut bir UAV'yi güncellemek için kullanılır.
    model = UAV
    template_name = 'uav_form.html'
    fields = ['brand', 'model', 'weight', 'category']
    success_url = reverse_lazy('profile')

class RentalListView(ListView):
    # Kiralama listesini görüntülemek için kullanılır.
    model = Rental
    template_name = 'rental_list.html'

class UAVDeleteView(DeleteView):
    # Bir UAV'yi silmek için kullanılır.
    model = UAV
    success_url = reverse_lazy('profile')
    template_name = 'uav_confirm_delete.html'

class RentalDetailView(DetailView):
    # Belirli bir kiralamanın ayrıntılarını görüntülemek için kullanılır.
    model = Rental
    template_name = 'rental_detail.html'

class RentalUpdateView(UpdateView):
    # Mevcut bir kiralama girişini güncellemek için kullanılır.
    model = Rental
    template_name = 'rental_form.html'
    form_class = RentalForm
    success_url = reverse_lazy('profile')

class RentalCreateView(CreateView):
    # Yeni bir kiralama girişi oluşturmak için kullanılır.
    model = Rental
    template_name = 'rental_form.html'
    form_class = RentalForm
    success_url = reverse_lazy('profile')

class RentalDeleteView(DeleteView):
    # Bir kiralama girişini silmek için kullanılır.
    model = Rental
    success_url = reverse_lazy('rental-list')
    template_name = 'rental_confirm_delete.html'
    success_url = reverse_lazy('profile')
