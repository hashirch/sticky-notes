from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from notes import views as note_views

# Poore project ke URL patterns
urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # Notes app ke URLs - /notes/ prefix ke saath
    path('notes/', include('notes.urls')),

    # Registration page - apna custom view
    path('register/', note_views.register_view, name='register'),

    # Login - Django ka built-in LoginView, apna template use karega
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout - Django ka built-in LogoutView, login pe redirect karega
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Root URL pe /notes/ pe redirect karo
    path('', RedirectView.as_view(url='/notes/', permanent=False)),
]
