from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('dojos/', views.getDojos, name='dojo-list'),
    path('dojo/<int:dojo_id>/', views.getDojo),
    path('dojo/add/', views.createDojo, name='dojo-add'),
    path('dojo/<int:dojo_id>/members/', views.getDojoMembers, name="dojo-members"),
    path('dojo/member/<int:id>', views.getMember),
    path('dojo/<int:dojo_id>/add/', views.addMember)
]