from django import forms
from .models import Note

# Note banane aur edit karne ka form - ModelForm se inherit kar rahe hain
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # Sirf yeh teen fields user ko dikhani hain - owner aur timestamps nahi
        fields = ['title', 'content', 'color']
        widgets = {
            # Title ke liye simple text input with placeholder
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note ka title likhein...'
            }),
            # Content ke liye textarea - 5 rows
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Yahan apna note likhein...',
                'id': 'note-content'  # JavaScript character counter ke liye
            }),
            # Color picker input - user apni marzi ka color chunega
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control form-control-color',
                'title': 'Note ka color chunein'
            }),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'color': 'Note Color',
        }
