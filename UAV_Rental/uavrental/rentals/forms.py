from django import forms
from .models import Rental
from django.utils import timezone

# Kiralama Formu
class RentalForm(forms.ModelForm):
    class Meta:
        # Formun hangi model üzerinden oluşturulacağını belirtir
        model = Rental
        # Formda hangi alanların yer alacağını belirtir
        fields = ['uav', 'date_start', 'date_end', 'renting_member']
        # Widget'ların tanımlanması, bu durumda datetime alanlarının tipinin belirlenmesi
        widgets = {
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # Temizleme metodu, formda kullanıcı tarafından girilen verileri doğrular
    def clean(self):
        cleaned_data = super().clean()
        date_start = cleaned_data.get("date_start")
        date_end = cleaned_data.get("date_end")
        # Başlangıç ve bitiş tarihlerinin geçerliliğini kontrol eder
        if date_start and date_end:
            if date_start < timezone.now():
                raise forms.ValidationError("Başlangıç tarihi geçmiş bir tarih olamaz.")
            if date_end < date_start:
                raise forms.ValidationError("Bitiş tarihi başlangıç tarihinden önce olamaz.")
        return cleaned_data
