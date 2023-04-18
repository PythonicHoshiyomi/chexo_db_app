from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('dojos/', views.getDojos, name='dojo-list'),
    path('dojos/<int:dojo_id>/', views.getDojo),
    path('dojos/add/', views.createDojo, name='dojo-add'),
    path('dojos/<int:pk>/update', views.updateDojo, name='dojo-update'),
    path('dojos/<int:dojo_id>/delete', views.deleteDojo, name='dojo-delete'),
    path('dojos/<int:dojo_id>/members/', views.getDojoMembers, name="dojo-members"),
    path('dojos/members/<int:id>', views.getMember),
    path('dojos/<int:dojo_id>/add/', views.addMember, name='member-add'),
    path('dojos/<int:dojo_id>/members/<int:pk>/delete', views.deleteMember, name='member-delete'),
    path('dojos/<int:dojo_id>/members/<int:pk>/', views.updateMember, name='member-update')
]