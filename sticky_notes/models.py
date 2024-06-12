from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore

# Define the StickyNotes model


class StickyNotes(models.Model):
    '''A CharField for the title of the sticky note with
    a maximum length of 200 characters'''
    title = models.CharField(max_length=200)
    # A TextField for the content of the sticky note (no maximum length)
    content = models.TextField()
    '''A DateTimeField for the creation date, automatically set
    to the current date and time when the note is created'''
    date_created = models.DateTimeField(default=timezone.now)
    '''A DateTimeField for the last updated date, automatically set t
    o the current date and time whenever the note is saved'''
    date_updated = models.DateTimeField(auto_now=True)

    # A string representation method that returns the title of the sticky note
    def __str__(self):
        return self.title
