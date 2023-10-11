from django.contrib.auth import login, authenticate
from django.views import View
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm, CustomUserEditForm  # Импортируйте форму редактирования профиля
from .models import Region  # Импортируйте модель Region

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            selected_region = form.cleaned_data['region']
            user = form.save(commit=False)
            user.region = selected_region
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class EditProfile(View):
    template_name = 'registration/edit_profile.html'

    def get(self, request):
        form = CustomUserEditForm(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправьте пользователя на страницу профиля или другую страницу
        context = {'form': form}
        return render(request, self.template_name, context)
