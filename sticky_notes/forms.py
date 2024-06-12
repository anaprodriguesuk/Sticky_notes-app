from django import forms  # type: ignore
from .models import StickyNotes


class StickyNotesForm(forms.ModelForm):
    class Meta:
        model = StickyNotes  # Specifies the model to use for the form
        fields = ['title', 'content']
        # Specifies the fields to include in the form
