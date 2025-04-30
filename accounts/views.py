# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import RegisterForm
# from django.contrib import messages

# def register_view(request):
#     form = RegisterForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             messages.success(request, "Registration successful")
#             return redirect('login')
#     return render(request, 'accounts/register.html', {'form': form})

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Invalid credentials")
#     return render(request, 'accounts/login.html')

# @login_required
# def dashboard_view(request):
#     return render(request, 'accounts/dashboard.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')


# ====================================================================================


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful")
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # This points to the view in the notes app
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'accounts/login.html')

# ⛔️ REMOVE or COMMENT OUT this old dashboard view, it's now handled by the notes app
# @login_required
# def dashboard_view(request):
#     return render(request, 'accounts/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
