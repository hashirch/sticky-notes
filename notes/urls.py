from django.urls import path
from . import views

# Notes app ke saare URL patterns yahan hain
urlpatterns = [
    # Notes ki list - home page
    path('', views.note_list, name='note_list'),

    # Naya note banao
    path('new/', views.note_create, name='note_create'),

    # Existing note edit karo - pk se specific note dhundha jata hai
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),

    # Note delete karo - pehle confirm page aayega
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
