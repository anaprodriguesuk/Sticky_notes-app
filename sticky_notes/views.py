# type: ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import StickyNotes
from .forms import StickyNotesForm

# View to list all sticky notes


def list_notes(request):
    notes = StickyNotes.objects.all()
    return render(request, "sticky_notes/list_notes.html", {'notes': notes})

# View to read details of a sticky note


def read_note(request, note_id):
    note = get_object_or_404(StickyNotes, pk=note_id)
    return render(request, "sticky_notes/view_notes.html", {'note': note})

# View to create a new sticky note


def create_note(request):
    if request.method == 'POST':
        form = StickyNotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_notes"))
        else:
            return render(request, "sticky_notes/create_notes.html",
                          {'form': form, 'error': 'All fields are required.'})
    else:
        form = StickyNotesForm()
        return render(request, "sticky_notes/create_notes.html",
                      {'form': form})

# View to update an existing sticky note


def update_note(request, note_id):
    note = get_object_or_404(StickyNotes, pk=note_id)
    if request.method == 'POST':
        form = StickyNotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse('read_note', args=[note_id]))
        else:
            return render(request, "sticky_notes/update_note.html",
                          {'form': form, 'note': note, 'error':
                              'All fields required.'})
    else:
        form = StickyNotesForm(instance=note)
        return render(request, "sticky_notes/update_note.html",
                      {'form': form, 'note': note})

# View to delete an existing sticky note


def delete_note(request, note_id):
    note = get_object_or_404(StickyNotes, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect(reverse('list_notes'))
    else:
        return render(request, "sticky_notes/delete_note.html", {'note': note})
