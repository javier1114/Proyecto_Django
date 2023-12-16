from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetConfirmView

from .forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm, CustomSetPasswordForm
from cuentas.models import User

def crear_manager():
    if not User.objects.filter(email="admin@correo.com").first():
        user = User.objects.create_user(
            "admin@correo.com", 'Administrador' ,'admin1234'
        )
        # le damos permisos de administrador y gerente
        user.is_manager = True
        user.is_admin = True
        user.save()


def manager_login(request):
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None and user.is_manager:
                login(request, user)
                return redirect('dashboard:products')
            else:
                messages.error(
                    request, 'Usuario o contraseña incorrectos!', 'danger'
                )
                return redirect('cuentas:manager_login')
    else:
        form = ManagerLoginForm()
    context = {'form': form}
    return render(request, 'manager_login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.crear_usuario(
                data['email'], data['nombre_completo'], data['contraseña']
            )
            return redirect('cuentas:user_login')
    else:
        form = UserRegistrationForm()
    context = {'titulo':'Signup', 'form':form}
    return render(request, 'register.html', context)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'password_reset_confirm.html'  # La plantilla para mostrar el formulario de cambio de contraseña


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['contraseña']
            )
            if user is not None:
                login(request, user)
                return redirect('tienda:pagina_inicio')
            else:
                messages.error(
                    request, 'Usuario o contraseña incorrectos!', 'danger'
                )
                return redirect('cuentas:user_login')
    else:
        form = UserLoginForm()
    context = {'titulo':'Login', 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('cuentas:user_login')


def edit_profile(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tu perfil ha sido actualizado!', 'success')
        return redirect('cuentas:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'titulo':'Edit Profile', 'form':form}
    return render(request, 'edit_profile.html', context)