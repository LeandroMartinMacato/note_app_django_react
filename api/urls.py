from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name="notes"),
    path('note/<str:pk>/update', views.updateNote, name="update-note"),
    path('note/<str:pk>/delete', views.deleteNote, name="delete-note"),
    path('note/<str:pk>', views.getNote, name="note"),
]
