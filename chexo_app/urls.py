from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.MemberListView.as_view(), name='list'),
    path('list/add/', views.ListCreate.as_view(), name='dojo-add'),
    path('list/dojo/<int:pk>', views.DojoUpdate.as_view(), name='dojo-update'),
    path('list/<int:list_id>/add/', views.MemberCreate.as_view(), name='member-add'),
    path('list/<int:list_id>/member/<int:pk>', views.MemberUpdate.as_view(), name='member-update')
]