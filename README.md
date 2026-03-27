# 📝 Sticky Notes App

A personal sticky notes web application built with Django. Users can register, log in, and manage their own private collection of colorful notes.

---

## Features

- User registration and authentication (login/logout)
- Create, edit, and delete personal notes
- Color-coded note cards (like real sticky notes)
- Color picker with quick-select preset colors
- Search notes by title or content
- Each user only sees their own notes
- Responsive design using Bootstrap 5
- Character counter on note content field
- Django admin panel for data inspection

---

## Project Structure

```
sticky_project/
├── manage.py
├── db.sqlite3
├── README.md
├── sticky_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notes/
│   ├── models.py       # Note model
│   ├── views.py        # All views (list, create, edit, delete, register)
│   ├── forms.py        # NoteForm (ModelForm)
│   ├── urls.py         # Notes app URL patterns
│   ├── admin.py        # Admin panel registration
│   └── migrations/
└── templates/
    ├── base.html               # Base layout with navbar
    ├── note_list.html          # All notes grid view
    ├── note_form.html          # Create & Edit form (shared)
    ├── note_confirm_delete.html
    ├── register.html
    └── login.html
```

---

## Setup Instructions

### 1. Prerequisites

Make sure you have Python 3.8+ installed.

```bash
python3 --version
```

### 2. Clone / Extract the Project

```bash
# If from ZIP:
unzip sticky_notes.zip
cd sticky_notes

# If from GitHub:
git clone <repo-url>
cd sticky_notes
```

### 3. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows
```

### 4. Install Dependencies

```bash
pip install django
```

### 5. Run Migrations

```bash
python3 manage.py migrate
```

### 6. (Optional) Create a Superuser for Admin Panel

```bash
python3 manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python3 manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000/**

---

## Pages & URLs

| Page         | URL                    | Description                          |
|--------------|------------------------|--------------------------------------|
| Home/Notes   | `/notes/`              | Shows all notes for logged-in user   |
| Create Note  | `/notes/new/`          | Form to write a new sticky note      |
| Edit Note    | `/notes/<id>/edit/`    | Pre-filled form to update a note     |
| Delete Note  | `/notes/<id>/delete/`  | Confirmation page before deleting    |
| Register     | `/register/`           | New user sign-up form                |
| Login        | `/login/`              | Username & password login            |
| Logout       | `/logout/`             | Logs out and redirects to login      |
| Admin        | `/admin/`              | Django admin panel (superuser only)  |

---

## Usage

1. Go to `/register/` and create a new account
2. You'll be automatically logged in and redirected to `/notes/`
3. Click "New Note" to create your first sticky note
4. Pick a color using the color picker or quick-color buttons
5. Hover over any note card to see Edit and Delete buttons
6. Use the search bar to filter notes by title or content

---

## Notes on Security

- All note views are protected with `@login_required`
- Users can only view/edit/delete their own notes (enforced via `owner=request.user` filter)
- CSRF protection is enabled on all forms
- Django's built-in `UserCreationForm` handles secure password hashing

---

## Bonus Features Implemented

- Search bar to filter notes by title or content
- Color picker input on the form
- Quick-select preset color buttons
- Live card background preview when picking a color
- Character counter on the content field

---

## Submission Info

- Student: [Your Name]
- Roll Number: [Your Roll Number]
- Assignment: Sticky Notes Django App
