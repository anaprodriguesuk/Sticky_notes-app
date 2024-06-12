from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sticky_notes.urls')),  # Include your app's URLs here
]




