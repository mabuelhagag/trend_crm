from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(_("First Name"), blank=True, max_length=255)
    last_name = models.CharField(_("Last Name"), blank=True, max_length=255)
    company = models.CharField(_("Company"), blank=True, max_length=20)
    phone = models.CharField(_("Phone"), blank=True, max_length=255)
    email = models.CharField(_("Email"), blank=True, max_length=255)
    balance = models.DecimalField(_("Balance"), blank=True, decimal_places=2, max_digits=5)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def authorization(self):
        return "Unchecked"

    @property
    def reseller(self):
        return "Unchecked"

    @property
    def private(self):
        return "Unchecked"
