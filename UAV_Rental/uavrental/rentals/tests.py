from django.test import TestCase
from django.urls import reverse
from .models import UAV, Rental
from django.contrib.auth.models import User
from .forms import RentalForm

class UAVModelTest(TestCase):
    # UAV modelinin doğru bir şekilde oluşturulup oluşturulmadığını test eder.
    def test_uav_model(self):
        uav = UAV.objects.create(
            brand='Test Brand',
            model='Test Model',
            weight=10.5,
            category='Test Category'
        )
        self.assertEqual(uav.brand, 'Test Brand')
        self.assertEqual(uav.model, 'Test Model')
        self.assertEqual(uav.weight, 10.5)
        self.assertEqual(uav.category, 'Test Category')


class RentalFormTest(TestCase):
    # Kiralama formunun doğru bir şekilde oluşturulup oluşturulmadığını test eder.
    def test_rental_form(self):
        user = User.objects.create(username='testuser')
        uav = UAV.objects.create(
            brand='Test Brand',
            model='Test Model',
            weight=10.5,
            category='Test Category'
        )
        data = {
            'uav': uav.pk,
            'date_start': '2024-05-01',
            'date_end': '2024-05-05',
            'renting_member': user.pk
        }
        form = RentalForm(data=data)
        self.assertTrue(form.is_valid())

class RentalModelTest(TestCase):
    # Kiralama modelinin doğru bir şekilde oluşturulup oluşturulmadığını test eder.
    def test_rental_model(self):
        user = User.objects.create(username='testuser')
        uav = UAV.objects.create(
            brand='Test Brand',
            model='Test Model',
            weight=10.5,
            category='Test Category'
        )
        rental = Rental.objects.create(
            uav=uav,
            date_start='2024-05-01',
            date_end='2024-05-05',
            renting_member=user
        )
        self.assertEqual(rental.uav, uav)
        self.assertEqual(rental.date_start, '2024-05-01')
        self.assertEqual(rental.date_end, '2024-05-05')
        self.assertEqual(rental.renting_member, user)
