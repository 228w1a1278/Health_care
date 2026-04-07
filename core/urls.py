from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_router, name='home'),
    path('receptionist/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('status/<int:pk>/<str:new_status>/', views.update_status, name='update_status'),
    path('consultation/<int:pk>/', views.write_prescription, name='write_prescription'),
    path('print/<int:pk>/', views.view_prescription, name='view_prescription'),
]
