from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import Note
from .forms import NoteForm


# ===================== NOTE VIEWS =====================

@login_required  # Sirf logged-in user access kar sakta hai
def note_list(request):
    """Logged-in user ke saare notes dikhata hai, search bhi support karta hai"""
    # Search query URL se lena - ?q=kuch_bhi
    query = request.GET.get('q', '')

    # Sirf is user ke notes fetch karo
    notes = Note.objects.filter(owner=request.user)

    # Agar search query hai to title ya content mein dhundho
    if query:
        notes = notes.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, 'note_list.html', {
        'notes': notes,
        'query': query,  # Search box mein wapas dikhane ke liye
    })


@login_required
def note_create(request):
    """Naya note banane ka view - GET pe form dikhao, POST pe save karo"""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Note save karo lekin pehle owner set karo
            note = form.save(commit=False)
            note.owner = request.user  # Current logged-in user owner hai
            note.save()
            return redirect('note_list')
    else:
        # Pehli baar form khali dikhao
        form = NoteForm()

    return render(request, 'note_form.html', {
        'form': form,
        'action': 'Create',  # Template mein heading ke liye
    })


@login_required
def note_edit(request, pk):
    """Existing note edit karne ka view - sirf owner edit kar sakta hai"""
    # Note dhundho - agar owner match nahi karta to 404 do
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        # Existing note ko naye data se update karo
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        # Form mein purana data pehle se bhara hua dikhao
        form = NoteForm(instance=note)

    return render(request, 'note_form.html', {
        'form': form,
        'action': 'Edit',  # Template mein heading ke liye
        'note': note,
    })


@login_required
def note_delete(request, pk):
    """Note delete karne ka view - pehle confirm karo, phir delete karo"""
    # Sirf is user ka note delete ho sakta hai
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        # User ne confirm kar diya - note delete karo
        note.delete()
        return redirect('note_list')

    # GET request pe confirmation page dikhao
    return render(request, 'note_confirm_delete.html', {'note': note})


# ===================== AUTH VIEWS =====================

def register_view(request):
    """Naye user ka registration - Django ka built-in UserCreationForm use kar rahe hain"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # User save karo aur seedha login kar do
            user = form.save()
            login(request, user)  # Register ke baad automatically login
            return redirect('note_list')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
