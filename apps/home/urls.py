from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.profesores, name='home'),
    
    path('planillas', views.planillas, name='planilla'),
    path('planillas/registro-titulos',views.registroTitulos, name='registro_titulos'),
    path('planillas/materia-pendientes',views.materiaPendientes, name='materia_pendientes'),
    path('planillas/finales',views.finales, name='finales'),
    path('planillas/revision',views.revision, name='revision'),

    path('profesores', views.profesores, name='profesores'),
    path('profesores/crear', views.crearProfesores, name='crear_profesores'),
    path('profesores/<int:id>/editar', views.editarProfesores, name='editar_profesores'),
    path('profesores/<int:pk>/agregar_materia', views.agergar_materia_profesor, name='agregar_materia_profesor'),
    path('profesores/<str:pk>/eliminar-materia', views.eliminar_materia_profesor, name='eliminar_materia_profesor'),
    
    path('materias', views.materias, name='materia'),
    path('materias/crear', views.materiaCrear, name='materia_crear'),
    path('materias/<str:pk>/editar', views.materiaEditar, name='materia_editar'),
    path('materias/<str:pk>/eliminar', views.materiaEliminar, name='materia_eliminar'),
    path('materias/obtener', views.obtener_materias, name='obtener_materias'),

    path('cargas/crear', views.cargaCrear, name='carga_crear'),
    path('cargas/<str:pk>/editar', views.cargaEditar, name='carga_editar'),
    path('cargas/<str:pk>/eliminar', views.cargaEliminar, name='carga_eliminar'),

    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.estudianteCrear, name='estudiantes_crear'),
    path('estudiantes/<int:id>/editar', views.estudianteEditar, name='estudiantes_editar'),
    path('estudiantes/<str:pk>/inasistencias', views.estudianteInasistencias, name='estudiante_inasistencias'),
    path('estudiantes/<str:pk>/<str:dir>/<str:periodo_sel>', views.estudianteVer, name='estudiante_ver'),
    path('estudiantes/<str:pk>/agregar-materia', views.agregar_materia_pendiente, name='agregar_materias_pendientes'),
    path('estudiantes/<str:pk>/eliminar-materia', views.eliminar_materia_pendiente, name='eliminar_materia_pendiente'),

    path('notas', views.notas, name='notas'),
    path('notas/cargar', views.Cargar_Notas, name='cargar_notas'),

    path('notas/<str:pk>/editar', views.editarNotas, name='editar_notas'),
    path('notas/<str:pd>/carga', views.carga_notas, name='carga_notas'),
    path('notas/<str:pk>/<str:dir>/<str:periodo_sel>', views.estudianteVer, name='imprimir_notas'),

    path('periodos', views.periodos, name='periodo'),
    path('periodos/crear', views.periodoCrear, name='periodo_crear'),
    path('periodos/<str:pk>/editar', views.periodoEditar, name='periodo_editar'),
    path('periodos/<str:pk>/eliminar', views.periodoEliminar, name='periodo_eliminar'),
    path('periodos/cambiar/<str:periodo_actual>', views.cambiar_periodo, name='cambiar_periodo'),

    path('configuracion', views.configuracion, name='configuracion'),
    path('configuracion/secciones', views.secciones, name='secciones'),
    path('configuracion/secciones/crear', views.crear_seccion, name='crear_seccion'),
    path('configuracion/secciones/<str:pk>/editar', views.editar_seccion, name='editar_seccion'),
    path('configuracion/periodos-academicos', views.crearPeriodoAcademico, name='crear_periodo'),
    path('configuracion/periodos-academicos/<str:pk>/editar', views.periodoAcademico_editar, name='editar_periodo'),
    path('configuracion/años', views.crearAnios, name='crear_anios'),
    path('configuracion/años/<str:pk>/editar', views.anio_editar, name='editar_anios'),
    path('configuracion/menciones', views.crearMenciones, name='crear_menciones'),
    path('configuracion/menciones/<str:pk>/editar', views.mencion_editar, name='editar_menciones'),
    
    path('notas', views.notas, name='notas'),
    path('notas/cargar', views.Cargar_Notas, name='Cargar_Notas'),
    path('notas/actualizar/<str:pk>', views.actualizar_notas, name='actualizar_notas'),
    path('notas/procesar', views.procesar, name='procesar'),

    path('boletas', views.boletas, name='boletas'),
    path('boletas/lista', views.boletas_lista_estudiantes, name='lista_boletas'),
    path('boletas/<str:pk>/ver', views.generar_boleta, name='generar_boletas'),

    path('inasistencias/actualizar/<str:pk>', views.actualizar_inasistencias, name='actualizar_insistencias'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
