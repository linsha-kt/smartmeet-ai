from django.urls import path
from . import views

urlpatterns = [

    path('', views.meeting_list, name='meeting_list'),

    path('add/', views.meeting_add, name='meeting_add'),

    path('<int:id>/', views.meeting_detail, name='meeting_detail'),

    path('edit/<int:id>/', views.meeting_edit, name='meeting_edit'),

    path('delete/<int:id>/', views.meeting_delete, name='meeting_delete'),

]