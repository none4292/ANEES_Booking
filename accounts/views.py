from django.shortcuts import get_object_or_404, redirect, render
from .models import Proflie
from .forms import UserForm , ProfileForm , UserCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from roommseters.models import Roommset 
from django.contrib.auth.models import User
# Create your views here.
# view for user signup to get information from the django from and create the user 
def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})


# get the proflie data for user authenticate
def profile(request):
    profile = Proflie.objects.get(user = request.user)
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
            
        user_roomset = Roommset.objects.filter(seeker=user)
        print(user_roomset)
    else:
        return redirect('/')

    context = {
        'obj':profile,
        'user_roomset':user_roomset,
    }
    return render(request,'profile/profile.html', context)


# get the proflie data from the django form and edit the data and send it bacck by user 
def profile_edit(request):
    profile = Proflie.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })
