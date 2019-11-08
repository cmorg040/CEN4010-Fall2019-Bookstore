from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address, CreditCard
from crispy_forms.helper import FormHelper
import datetime
import re
from django.forms import ModelForm, ChoiceField, CharField
from .calendar import MONTHS, YEARS

# User registration form
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        #self.fields['username'].label = False
        # Do not show fields for username and emails
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        #self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


# This form will be used to update first name and last name
class UserProfileForm(forms.ModelForm):
    # used for crispy form to auto generate first name and last name
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


# Form to update the users nickname at the profile page
class NicknameForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick_name']


# Form to update the user bio at the profile page
class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']


# Form to update username and email at the profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Do not show fields for username
        self.fields['username'].help_text = ''


# this form is to edit/add the address for the user
class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        # all fields that are used to get user address
        fields = ['name', 'address1', 'address2', 'city', 'state', 'zipcode', 'primaryAddress']

    def __init__(self, *args, **kwargs):
        super(EditAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        # these are the fields that are all required it will be marked with a * in order to be updated
        # address2 not required
        self.fields['address2'].required = False


class DeleteAddressForm(forms.Form):
    pass


class CreditCardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)

        self.fields['number'] = forms.CharField(widget=forms.TextInput(attrs={'id': 'creditcard-number'}))
        self.fields['expdate_month'] = ChoiceField(choices=MONTHS)
        self.fields['expdate_year'] = ChoiceField(choices=YEARS)

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'expdate_month', 'expdate_year', 'securitycode']

    def clean(self):
        # Get all error messages
        self.invalidErrors = []
        # Get card number
        number = self.cleaned_data['number']
        # Get card expiration month
        month = int(self.cleaned_data['expdate_month'])
        # Get card expiration year
        year = int(self.cleaned_data['expdate_year'])
        # Get card security code
        securityCode = self.cleaned_data['securitycode']

        # to determine credit card pattern
        # http://code.activestate.com/recipes/577815-determine-credit-card-type-by-number/

        """
        AMEX_CC_RE = re.compile(r"^3[47][0-9]{13}$")
        VISA_CC_RE = re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$")
        MASTERCARD_CC_RE = re.compile(r"^5[1-5][0-9]{14}$")
        DISCOVER_CC_RE = re.compile(r"^6(?:011|5[0-9]{2})[0-9]{12}$")

        CC_MAP = {"American Express": AMEX_CC_RE, "Visa": VISA_CC_RE,
                  "Mastercard": MASTERCARD_CC_RE, "Discover": DISCOVER_CC_RE}

        validation = ''
        for type, regexp in CC_MAP.items():
            if regexp.match(str(number)):
                validation = type
        """

        VISA_PAT = r'^4[0-9]{12}(?:[0-9]{3})?$'
        MASTERCARD_PAT = r"^5[1-5][0-9]{14}$"
        AMERICANEXP_PAT = r'^3[47][0-9]{13}$'
        DISCOVERY_PAT = r'^6(?:011|5[0-9]{2})[0-9]{12}$'

        cardTypeList = [DISCOVERY_PAT, VISA_PAT, MASTERCARD_PAT, ]

        credit_string = '|'.join(cardTypeList)

        # threeDigitCards has only 3 digit security code
        threeDigitCards = re.compile(credit_string)
        # fourDigitCards has only 4 digit security code
        fourDigitCards = re.compile(AMERICANEXP_PAT)

        if threeDigitCards.match(str(number)):
            creditCardValid = re.compile(r'^[0-9]{3}$')  # 3
        elif fourDigitCards.match(str(number)):
            creditCardValid = re.compile(r'^[0-9]{4}$')  # 4
        else:
            creditCardValid = None
            self.invalidErrors.append('Credit card number not valid')

        # check credit card expiration date
        if datetime.datetime(year, month, 1) < datetime.datetime.today():
            self.invalidErrors.append('Credit Card Expired')

        # verify security code if not match then get this error
        if not creditCardValid or not creditCardValid.match(str(securityCode)):
            self.invalidErrors.append('Invalid security code')

        if len(self.invalidErrors):
            raise forms.ValidationError(' , '.join(self.invalidErrors))

        return self.cleaned_data

