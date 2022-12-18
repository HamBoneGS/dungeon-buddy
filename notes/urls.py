from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes, name='new_note'),
    path('<int:id>', views.notes, name='edit_note'),
    path('save/', views.save_note, name="save_note"),
    path('<int:id>/update/', views.update_note, name="update_note"),
    path('characters', views.characters, name='characters_home'),
    path('characters/<int:id>', views.character_full, name="character_full")
]