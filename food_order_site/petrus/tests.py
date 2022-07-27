from django.test import TestCase
from django.urls import resolve, reverse
from petrus.views import index

# Create your tests here.


class indexTest(TestCase):
    def test_reservation_form_resolve(self):
        url = reverse(index)
        self.assertEquals(resolve(url).func, index)
