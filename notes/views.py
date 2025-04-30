from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

@login_required
def dashboard_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/dashboard.html', {'notes': notes})

@login_required
def add_note_view(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect('dashboard')
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Add Note'})

@login_required
def edit_note_view(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Edit Note'})

@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('dashboard')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
