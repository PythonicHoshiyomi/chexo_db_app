from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.MemberListView.as_view(), name='list'),
    path('list/add/', views.ListCreate.as_view(), name='dojo-add'),
]