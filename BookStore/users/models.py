from django.db import models, transaction
from django.contrib.auth.models import User
from localflavor.us.models import USStateField  # To shows list of US states on address form
from django.urls import reverse # to return url when clicking on address
from .calendar import MONTHS, YEARS, JAN, CURRENT_YEAR

# https://docs.djangoproject.com/en/2.1/ref/models/instances/#get-absolute-url

# All data is linked to this profile. If data gets deleted then the user should be deleted as well
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick name', max_length=30, blank=True, default='')
    bio = models.TextField(max_length=450, blank=True)

    def __str__(self):
        # get the profile not just the object
        return self.user.username


# All information for the address should be linked to this
class Address(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField("Address Lines 1", max_length=100)
    address2 = models.CharField("Address Lines 2", max_length=100, blank=True)
    city = models.CharField("City", max_length=50)
    state = USStateField("State", default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)
    slug = models.SlugField(max_length=150, db_index=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    primaryAddress = models.BooleanField()

    def __str__(self):
        return self.name

    @transaction.atomic
    # if primary address is checked
    def save(self, *args, **kwargs):
        if self.primaryAddress:
            Address.objects.filter(
                primaryAddress=True).update(primaryAddress=False)
        super(Address, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('settings:edit-address', args=[self.id])

# all credit card information should be linked to this
class CreditCard(models.Model):
    name = models.CharField(max_length=50, blank=False)
    number = models.CharField(max_length=16, blank=False, unique=True)
    expdate_month = models.IntegerField(choices=MONTHS, default=JAN)
    expdate_year = models.IntegerField(choices=YEARS, default=CURRENT_YEAR)
    securitycode = models.IntegerField(blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('settings:edit-creditcard', args=[self.id])
