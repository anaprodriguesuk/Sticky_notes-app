from django.urls import path # type: ignore
from . import views


urlpatterns = [
    # URL pattern for listing all notes
    path('', views.list_notes, name='list_notes'),
    # URL pattern for reading a specific note
    path('note/<int:note_id>/', views.read_note, name='read_note'),
    # URL pattern for creating a new note
    path('note/create/', views.create_note, name='create_note'),
    # URL pattern for updating a specific note
    path('note/<int:note_id>/update/', views.update_note, name='update_note'),
    # URL pattern for deleting a specific note
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
   
]
