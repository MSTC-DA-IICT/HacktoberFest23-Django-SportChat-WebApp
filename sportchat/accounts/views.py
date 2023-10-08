from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Change 'login' to your login URL name
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'register.html', {'form': form})
