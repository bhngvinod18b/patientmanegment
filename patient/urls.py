
from django.urls import path, include
from .import views 
from .views import PatientViewSet, AppointmentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
app_name = 'patient'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_patient, name='add_patient'),
    path('search/', views.search_patient, name='search_patient'),
    path('delete/<str:phone>/', views.delete_patient, name='delete_patient'),
    path('api/', include(router.urls)),
    path('list/', views.patient_list, name='patient_list'),
    path('appointment/', views.add_appointments, name='add_appointments'),
    path('view/', views.view_appointment, name='view_appointment'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
