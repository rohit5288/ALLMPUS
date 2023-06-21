from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisteration


def register(request):
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            raw_password = form.cleaned_data.get('password1')
    else:
        form = UserRegisteration()
    return render(request, 'users/register.html', {'form': form})


