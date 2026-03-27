from django.contrib import admin
from .models import Note

# Note model ko admin panel mein register karo - data inspect karne ke liye useful
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Admin list mein yeh columns dikhao
    list_display = ('title', 'owner', 'color', 'created_at', 'updated_at')
    # Owner aur date se filter kar sako
    list_filter = ('owner', 'created_at')
    # Title aur content mein search kar sako
    search_fields = ('title', 'content')
