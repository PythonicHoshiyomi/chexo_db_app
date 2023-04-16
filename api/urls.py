from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('dojos/', views.getDojos, name='dojo-list'),
    path('dojo/<int:dojo_id>/', views.getDojo),
    path('dojo/add/', views.createDojo, name='dojo-add'),
    path('dojo/<int:pk>/update', views.updateDojo, name='dojo-update'),
    path('dojo/<int:dojo_id>/delete', views.deleteDojo, name='dojo-delete'),
    path('dojo/<int:dojo_id>/members/', views.getDojoMembers, name="dojo-members"),
    path('dojo/member/<int:id>', views.getMember),
    path('dojo/<int:dojo_id>/add/', views.addMember, name='member-add'),
    path('dojo/<int:dojo_id>/member/<int:pk>/delete', views.deleteMember, name='member-delete'),
    path('dojo/<int:dojo_id>/member/<int:pk>/', views.updateMember, name='member-update')
]