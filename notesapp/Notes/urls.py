from django.urls import path
from . import views

urlpatterns = [
    path('Notes/',views.NotesListView.as_view(), name="Notes.list"),
    path('Notes/<int:pk>',views.NotesDetailView.as_view(),name="notes.detail"),  
    path('Notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name="notes.update"), 
    path('Notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name="notes.delete"),     
    path('Notes/new',views.NotesCreateView.as_view(),name="notes.new"),

]