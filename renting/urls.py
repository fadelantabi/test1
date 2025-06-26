from django.urls import path
from . import views

urlpatterns = [
    path('renting/',view=views.renting),
    path('renting/<uuid:id>/',views.renting),
    path('renting/create/',view=views.renting),
    path('renting/<uuid:id>/update',views.renting),
    path('renting/<uuid:id>/delete',views.renting),
]