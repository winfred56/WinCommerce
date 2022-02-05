from django.shortcuts import render, redirect
from .forms import Registration


def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Registration()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
