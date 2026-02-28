from django.urls import path
from . import views
from django.urls import path, include
from .import views 
from views import PatientViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'patients', PatientViewSet)

app_name = 'patient'

urlpatterns = [
    path('', views.search_patient, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('search/', views.search_patient, name='search_patient'),
    path('delete/<str:phone>/', views.delete_patient, name='delete_patient'),
    path('api/', include(router.urls)),
]
