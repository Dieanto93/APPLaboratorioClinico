from django.urls import path
from . import views
from .views import registrar_paciente, editar_paciente, eliminar_paciente

urlpatterns = [
    path('', views.login_view, name='login'),
    path('administrative/dashboard/', views.administrative_dashboard, name='administrative_dashboard'),
    path('technician/dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('unknown_role/', views.unknown_role_dashboard, name='unknown_role_dashboard'),
    path('registrar-paciente/', registrar_paciente, name='registrar_paciente'),
    path('editar_paciente/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar-paciente/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),
    path('agregar-examenes-paciente/<int:paciente_id>/', views.agregar_examenes_paciente, name='agregar_examenes_paciente'),
    path('mostrar-resultados-examenes/', views.mostrar_resultados_examenes, name='mostrar_resultados_examenes'),
    path('ver-pedidos-pendientes/', views.ver_pedidos_pendientes, name='ver_pedidos_pendientes'),
    path('agregar-resultados-examenes/', views.agregar_resultados_examenes, name='agregar_resultados_examenes'),
    path('ingresar-resultados-examenes/', views.ingresar_resultados_examenes, name='ingresar_resultados_examenes'),
]