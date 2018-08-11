from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import UserForm, ProfileForm
from .models import User

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    username = request.user.username
                    return HttpResponseRedirect(
                        reverse('accounts:profile', kwargs={'username': username})
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            username = request.user.username
            return HttpResponseRedirect(reverse('accounts:profile', kwargs={'username': username}))
    return render(request, 'accounts/sign_up.html', {'form': form})

@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))

@login_required
def edit_profile(request, username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                "Great! Additions to your profile have been saved."
            )
            return HttpResponseRedirect(reverse('accounts:profile', kwargs={'username': request.user.username}))
    else:
        user = User.objects.get(username=username)
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def view_profile(request, username):
    user = User.objects.get(username=username)

    return render(request, 'accounts/profile.html', {
        'user': user,
    })

@login_required
def change_password(request, username):
    user = User.objects.get(username=username)

    return render(request, 'accounts/change_password.html', {
        'user': user,
    })

