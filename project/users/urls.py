from django.urls import path, include

from users.views import Register
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
]

