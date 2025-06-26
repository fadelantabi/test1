from django.urls import path
from . import views

urlpatterns = [
    path('color/',view=views.color),
    path('color/<uuid:id>/',views.color),
    path('color/create/',view=views.color),
    path('color/<uuid:id>/update',views.color),
    path('color/<uuid:id>/delete',views.color),
    path('model/',view=views.model),
    path('model/<uuid:id>/',views.model),
    path('model/create/',view=views.model),
    path('model/<uuid:id>/update',views.model),
    path('model/<uuid:id>/delete',views.model),
    path('product/',view=views.product),
    path('product/<uuid:id>/',views.product),
    path('product/create/',view=views.product),
    path('product/<uuid:id>/update',views.product),
    path('product/<uuid:id>/delete',views.product),
    path('product/filter/',views.filterApi)


]