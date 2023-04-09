from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path(
       'list/<int:list_id>/', 
       views.MemberListView.as_view(), 
       name='list'),
    #create a dojo
    path(
        'list/add/', 
        views.ListCreate.as_view(), 
        name='dojo-add'),
    #update a dojo
    path(
        'list/<int:pk>/update/', 
        views.DojoUpdate.as_view(), 
        name='dojo-update'),
    #delete a dojo
    path(
        'list/<int:pk>/delete/', 
        views.DojoDelete.as_view(), 
        name='dojo-delete'),
    #create a member to a dojo
    path(
        'list/<int:list_id>/add/', 
        views.MemberCreate.as_view(), 
        name='member-add'),
    #edit a member
    path(
        'list/<int:list_id>/member/<int:pk>/', 
        views.MemberUpdate.as_view(), 
        name='member-update'),
    #delete a member from a dojo
    path(
        'list/<int:list_id>/member/<int:pk>/delete/', 
        views.MemberDelete.as_view(), 
        name='member-delete')
]