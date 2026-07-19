from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),
    path('employees/edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('employees/delete/<int:id>/', views.employee_delete, name='employee_delete'),
]