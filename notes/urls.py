from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add_note_view, name='add_note'),
    path('edit/<int:pk>/', views.edit_note_view, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note_view, name='delete_note'),
]
