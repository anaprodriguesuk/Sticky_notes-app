from django.test import TestCase  # type: ignore
from django.urls import reverse  # type: ignore
from sticky_notes.models import StickyNotes


class StickyNotesTests(TestCase):

    # Set up a test sticky note that can be used in the tests
    def setUp(self):
        self.note = StickyNotes.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    # Test the list view for sticky notes
    def test_list_notes(self):
        response = self.client.get(reverse('list_notes'))
        self.assertEqual(response.status_code, 200)  # Check response
        self.assertContains(response, 'Test Note')   # Check response title

    # Test the detail view for a specific sticky note
    def test_read_note(self):
        response = self.client.get(reverse('read_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)  # Check tresponse
        # Check note content
        self.assertContains(response, 'This is a test note.')

    # Test creating a new sticky note
    def test_create_note(self):
        response = self.client.post(reverse('create_note'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        # Check redirect after creation
        self.assertEqual(response.status_code, 302)
        # Check that the new note was created
        self.assertEqual(StickyNotes.objects.last().title, 'New Note')

    # Test updating an existing sticky note
    def test_update_note(self):
        response = self.client.post(reverse('update_note',
                                            args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'This is an updated test note.'
        })
        # Check redirect after updating
        self.assertEqual(response.status_code, 302)
        # Refresh the note object from the database
        self.note.refresh_from_db()
        # Check that the note title was updated
        self.assertEqual(self.note.title, 'Updated Note')

    # Test deleting a sticky note
    def test_delete_note(self):
        response = self.client.post(reverse('delete_note',
                                            args=[self.note.id]))
        # Check for a redirect after deletion
        self.assertEqual(response.status_code, 302)
        # Check that the note was deleted
        self.assertEqual(StickyNotes.objects.count(), 0)
