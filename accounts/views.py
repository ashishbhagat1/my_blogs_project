from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate, logout  # add login check
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # logincheck
from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm

from .models import Profile
# Create your views here.


def register(request):
    #import pdb;pdb.set_trace() # Don't use this it break each line so install pdb

    if request.method == "POST":
        try:
            form = UserRegistrationForm(request.POST)
        except:
            pass
        if form.is_valid():
            user = form.save()
            # # return redirect("login")
            login(request, user)
            # username = form.cleaned_data.get('username','User')
            messages.success(request, f"Registration successful.{user.username}")
            return redirect("blog-home")
        else:
            messages.error(request, "Sorry ! Account Not Created. ")
            return redirect("blog-home")
    else:
        try:
            form = UserRegistrationForm()
        except:
            pass
        # messages.success(request, f'Account created for !')
        messages.info(request, "Welcome To Registration")
        contexts = {"form": form, "title": "Register User"}
    return render(request, template_name="register.html", context=contexts)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        profile= Profile.objects.get(user = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        #profile = Profile.objects.get(user=request.user)
        print("Profile is : => ",request.user.profile)
        p_form = ProfileUpdateForm(instance=request.user) #instance=profile

    context = {
        "u_form": u_form,
        "p_form": p_form,
        "title": "User Profile",
    }
    return render(request, template_name="profile.html", context=context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # return redirect("main:homepage")
                return redirect("blog-home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):  # this not use because predefined function we used that as auth_views

    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("blog-home")


# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')
