from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserSignUpForm, UserUpdateForm, UserProfileForm, BioForm, NicknameForm, EditAddressForm, DeleteAddressForm, CreditCardForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from .models import Address, CreditCard

# https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.htmls

# User registration page
def signup(request):
    # If the request is a post, then proceed w/ the form
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        # To validate the form if the form is valid
        if form.is_valid():
            # save the form
            form.save()
            # obtain the username
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for { username }.')
            # redirect to the store home page which is bookdetails page
            return redirect ('store-home-page')
    # if the request is not a post, then show a blank form
    else:
        # to use the form at signup we create an instance of the form we imported on top:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})

# When the user clicks on the profile menu, he/she will be redirected here
@login_required
def settingsHome(request):
    return redirect('settings:profile-settings')

#  This is to update the profile page, so users can add name, bio and nickname
@login_required
def profile(request):
    if request.method == 'POST':
        # Get first name and last name from User Profile Form
        userProfileForm = UserProfileForm(request.POST, instance=request.user)
        # Get Bio information from users
        userBioForm = BioForm(request.POST, instance=request.user.profile)
        # Get Nickname Information from users
        userNicknameForm = NicknameForm(request.POST, instance=request.user.profile)

        # if everything inputed is valid then update form
        if userProfileForm.is_valid() and userBioForm.is_valid() and userNicknameForm.is_valid():
            # save the profile form
            userProfileForm.save()
            # save the bio form
            userBioForm.save()
            # save the nickname form
            userNicknameForm.save()
            messages.success(request, f'Your profile updated successfully!')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, f'There were errors updating you profile.')

    else:
        # just get user information
        userProfileForm = UserProfileForm(instance=request.user)
        userBioForm = BioForm(instance=request.user.profile)
        userNicknameForm = NicknameForm(instance=request.user.profile)

    context = {
        'userProfileForm': userProfileForm,
        'userBioForm': userBioForm,
        'userNicknameForm': userNicknameForm
    }

    # return to profile page
    return render(request, 'users/profile.html', context)


# This form is to update the username and email
@login_required
def accountSettings(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)

        # get form validation
        if userForm.is_valid():
            # save the form
            userForm.save()
            # print success message
            messages.success(request, f'Account updated successfully!')
            return HttpResponseRedirect(request.path_info)
        # else incorrect inputs
        else:
            messages.warning(request, f'ERROR!')

    else:
        userForm = UserUpdateForm(instance=request.user)

    context = {
        'userForm': userForm
    }
    return render(request, 'users/account.html', context)

# This part involves everything for billing such ass address and credit card
# *****************************************************************************************************
# Billing page (credit card and billing address)
@login_required
def billingSettings(request):

    primaryAddressCheck = False
    # Get user address list
    userAddressList = Address.objects.all().filter(user__user__username=request.user)
    userCreditCards = CreditCard.objects.all().filter(user__user__username=request.user)

    for address in userAddressList:
        if address.primaryAddress == True:
            primaryAddressCheck = True

    context = {
        'userAddressList': userAddressList,
        'primaryAddressCheck': primaryAddressCheck,
        'userCreditCards': userCreditCards,
    }

    return render(request, 'users/billing.html', context)

# This is to add a new address to the users, it can either be primary or not
@login_required
def addAddress(request):

    if request.method == 'POST':
        userAddressForm = EditAddressForm(request.POST)

        # if new address meets all required fields
        if userAddressForm.is_valid():
            # store the new address as new address
            newUserAddress = userAddressForm.save(commit=False)
            newUserAddress.user_id = request.user.profile.id
            newUserAddress.save()
            # if message saved then
            messages.success(request, f'New Address has Been Added')
            return redirect('settings:billing-settings')
        else:
            messages.warning(
                request, f'ERROR! Please check all Fields!')

    else:
        userAddressForm = EditAddressForm()

    context = {
        'userAddressForm': userAddressForm
    }

    return render(request, 'users/addAddress.html', context)


# This is to update the current address
@login_required
def addressChange(request, address_slug):

    # Gets all the fields of the current address based on id
    currentAddress = Address.objects.all().get(pk=address_slug)

    if request.method == 'POST':
        userAddressForm = EditAddressForm(request.POST, instance=currentAddress)

        # check to see if all fields are valid
        if userAddressForm.is_valid():
            userAddressForm.save()
            messages.success(request, f'Your Address Updated successfully')
            # stay in the same directory after updating
            return HttpResponseRedirect(request.path_info)
        # this is to delete the current address
        elif DeleteAddressForm():
            Address.objects.filter(id=address_slug).delete()
            return redirect('settings:billing-settings')
        else:
            messages.warning(request, f'There errors updating you profile. Please check all Fields!')

    else:
        userAddressForm = EditAddressForm(instance=currentAddress)

    context = {
        'address_slug': address_slug,
        'userAddressForm': userAddressForm,
    }
    return render(request, 'users/addressChange.html', context)

# this is to add a new credit card
@login_required
def addCreditCard(request):

    if request.method == 'POST':
        userCreditCardForm = CreditCardForm(request.POST)

        # check if form is valid
        if userCreditCardForm.is_valid():
            # save the current inputs from the user
            newCreditCard = userCreditCardForm.save(commit=False)
            newCreditCard.user_id = request.user.profile.id
            newCreditCard.save()
            # if credit card added successfully then redirect to billing page
            messages.success(request, f'Your Credit Card has been Added!')
            return redirect('settings:billing-settings')
        else:
            messages.warning(
                request, f'Error in Adding your Credit Card!')
    else:
        userCreditCardForm = CreditCardForm()

    context = {
        'userCreditCardForm': userCreditCardForm
    }
    # render the page to add a credit card
    return render(request, 'users/addCreditCard.html', context)

# to update/edit your current credit card
@login_required
def creditCardChange(request, creditcard_slug):

    # Gets the current credit card you want to edit based on ID
    currentCreditCard = CreditCard.objects.all().get(pk=creditcard_slug)

    if request.method == 'POST':
        # save the current changes to this credit card
        userCreditCardForm = CreditCardForm(request.POST, instance=currentCreditCard)

        # check if the form is valid
        if userCreditCardForm.is_valid():
            # save the current changes
            userCreditCardForm.save()
            messages.success(request, f'Credit Card has Been Updated!')
            # do not redirect to new page, stay in same page
            return HttpResponseRedirect(request.path_info)

        # if you want to delete this credit card
        elif 'delete' in request.POST:
            currentCreditCard.delete()
            # redirect to billing page after deleting
            return redirect('settings:billing-settings')

        else:
            messages.warning(request, f'Error in Updating Credit Card.')
    else:
        userCreditCardForm = CreditCardForm(instance=currentCreditCard)

    context = {
        'creditcard_slug': creditcard_slug,
        'userCreditCardForm': userCreditCardForm,
    }
    return render(request, 'users/creditCardChange.html', context)


#*****************************************************************************************************

# To update users password
@login_required
def securitySettings(request):
    if request.method == 'POST':
        passform = PasswordChangeForm(request.user, request.POST)

        # if the passwords match then update it
        if passform.is_valid():
            passform.save()
            # update users password with new password
            update_session_auth_hash(request, passform.user)
            messages.success(request, f'Password Updated Successfully')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, f'ERROR! Check Incorrect Password Inputs')

    else:
        passform = PasswordChangeForm(request.user)

    context = {
        'passform': passform
    }
    return render(request, 'users/security.html', context)

