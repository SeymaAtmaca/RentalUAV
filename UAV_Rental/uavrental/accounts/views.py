from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from rentals.models import UAV, Rental
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    # Kullanıcı kayıt formu için CreateView sınıfını kullanır
    form_class = UserCreationForm
    # Kayıt başarılı olduktan sonra yönlendirme yapılacak URL
    success_url = reverse_lazy('login')
    # Kayıt sayfasının kullanacağı şablon
    template_name = 'signup.html'

class LoginView(LoginView):
    # Kullanıcı zaten giriş yapmışsa yönlendirme yapılacak URL
    redirect_authenticated_user = True
    # Giriş sayfasının kullanacağı şablon
    template_name = 'login.html'

@login_required
def profile_view(request):
    # Tüm UAV'leri getir
    uavs = UAV.objects.all()  
    # Kullanıcının yaptığı kiralamaları getir
    user_rentals = Rental.objects.filter(renting_member=request.user)  
    # profile.html şablonunu kullanarak profili render et
    return render(request, 'profile.html', {'uavs': uavs, 'user_rentals': user_rentals})
