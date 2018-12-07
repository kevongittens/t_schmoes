from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for %s' % username)
            return redirect('blog-home')
        else:
            messages.success(request, 'Accont details not valid')
    else:
        form = UserRegisterForm()
        messages.success(request, 'Accont details not valid')
    return render(request, 'users/register.html', {'form': form})
