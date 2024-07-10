# Escuela Técnica Industrial Pedro Zaraza - Sistema de Gestión Académica 💻📚
By [Servicio Comunitario Desarrollo Web UE Pedro Zaraza 2024-1 AIS UNERG]

## Descripción 📝
Este proyecto es un sistema de gestión académica desarrollado para la Escuela Técnica Industrial Pedro Zaraza. El sistema permite la gestión de periodos académicos, materias, secciones y estudiantes, y automatiza la generación de reportes y formatos necesarios para el control de estudio.


## Estado del proyecto 🚀
En desarrollo.


## Características ✨
- 📅 Gestión de periodos académicos.
- 📘 Administración de materias y secciones.
- 👩‍🎓 Registro y gestión de información de estudiantes.
- 📄 Generación de boletas de calificaciones y otros reportes.
- 📑 Automatización de formatos de control de estudio (Registro de títulos, Materias pendientes, Finales y Revisión).


## Requisitos de Software y Hardware 💻📋
-  Windows 10 o superior
-  Python 3.8+
-  Django 4.2+
-  SQLite (para base de datos de desarrollo)
-  Node.js (para gestión de dependencias front-end)
-  Otros requisitos especificados en `requirements.txt`


## Proceso de Instalación 🔧
### Clonar el Repositorio 🗂️
	bash
>git clone https://github.com/DanielEsc0911/ETPZ
>cd ETPZ


### Configurar el Entorno Virtual 🌐
	bash
>py -m venv env
>env\Scripts\activate.bat


### Instalar Dependencias 📦
	bash
>pip install -r requirements.txt


### Configurar el Archivo de Entorno 📄
Crear un archivo `.env` en el directorio raíz del proyecto y agregar las siguientes variables:
	env
SECRET_KEY= ”tu_clave_secreta_aqui”
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3


### Migrar la Base de Datos 💾
	bash
>python manage.py migrate


### Ejecutar el Servidor de Desarrollo 🌐
	bash
>py manage.py runserver 9090


## Uso 🚀
### Iniciar el Sistema
Para iniciar la página, abre la terminal y ejecuta los siguientes comandos:
	bash
>env\Scripts\activate.bat
>py manage.py runserver 9090


### Creación de Superusuario
Si el sistema no reconoce tu usuario y contraseña, habilita/crea en el entorno virtual:
	bash
>env\Scripts\activate.bat

Luego, escribe este comando:
	bash
>python manage.py createsuperuser


## Migraciones y Actualización del Repositorio en GitHub 📂
Para realizar migraciones o actualizar el repositorio en GitHub, usa los siguientes comandos:
	bash
>python manage.py makemigrations
>python manage.py migrate



## Estructura del Proyecto 📂
ETPZ
│
├── apps
│   ├── _psycache_                 # Archivos de caché de Python
│   ├── authentication             # Módulo de autenticación de usuarios
│   ├── home                       # Módulo principal del sistema
│   │   ├── _psycache_             # Archivos de caché de Python
│   │   ├── migrations             # Archivos de migraciones de la base de datos
│   │   ├── templatetags           # Tags personalizados para plantillas Django
│   │       ├── __init__.py        # Archivo de inicialización del módulo
│   │       ├── admin.py           # Configuración del panel de administración
│   │       ├── config.py          # Archivo de configuración del módulo
│   │       ├── forms.py           # Definición de formularios del módulo
│   │       ├── models.py          # Definición de modelos de datos
│   │       ├── tests.py           # Pruebas unitarias del módulo
│   │       ├── urls.py            # Definición de rutas del módulo
│   │       ├── utils.py           # Utilidades y funciones auxiliares
│   │       ├── views.py           # Definición de vistas del módulo
│
├── static                         # Archivos estáticos (CSS, JavaScript, imágenes)
├── templates                      # Plantillas HTML del proyecto
│   ├── _init_.py                  # Archivo de inicialización de plantillas
│   ├── config.py                  # Configuración de plantillas
│   ├── context_processors.py      # Procesadores de contexto para plantillas
│
├── core                           # Configuración central del proyecto
├── env                            # Entorno virtual del proyecto
├── staticfiles                    # Archivos estáticos recopilados para despliegue
│
├── .gitignore                     # Archivos y directorios ignorados por Git
├── autorun.bat                    # Script para ejecutar automáticamente el proyecto
├── db.sqlite3                     # Base de datos SQLite
├── gunicorn-cfg.py                # Configuración de Gunicorn para despliegue
├── LICENSE.md                     # Licencia del proyecto
├── log.json                       # Archivos de registro en formato JSON
├── manage.py                      # Comando de gestión de Django
├── readme.txt                     # Archivo README del proyecto
├── requirements.txt               # Dependencias del proyecto
├── server.py                      # Configuración del servidor de desarrollo

apps/
Contiene los módulos de la aplicación, como autenticación y la funcionalidad principal (home).

home/
_psycache_: Archivos de caché de Python para mejorar el rendimiento.
migrations/: Archivos que registran los cambios en los modelos de datos.
templatetags/: Tags personalizados para plantillas Django.
__init__.py: Archivo de inicialización.
admin.py: Configuración del panel de administración.
config.py: Archivo de configuración del módulo.
forms.py: Definición de formularios.
models.py: Definición de modelos de datos.
tests.py: Pruebas unitarias.
urls.py: Definición de rutas.
utils.py: Utilidades y funciones auxiliares.
views.py: Definición de vistas.
static/
Archivos estáticos como CSS, JavaScript e imágenes.

templates/
Plantillas HTML utilizadas en el proyecto.

core/
Configuración central del proyecto.

env/
Entorno virtual del proyecto.

staticfiles/
Archivos estáticos recopilados para despliegue.

Archivos raíz
.gitignore: Lista de archivos y directorios que Git debe ignorar.
autorun.bat: Script para ejecutar automáticamente el proyecto.
db.sqlite3: Base de datos SQLite utilizada en desarrollo.
gunicorn-cfg.py: Configuración de Gunicorn para despliegue.
LICENSE.md: Licencia del proyecto.
log.json: Archivos de registro en formato JSON.
manage.py: Herramienta de línea de comandos de Django.
readme.txt: Archivo README del proyecto.
requirements.txt: Lista de dependencias del proyecto.
server.py: Configuración del servidor de desarrollo.



## Contribución 🤝
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1.  Haz un fork del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-característica).
3.  Haz tus cambios y haz commit (`git commit -am 'Añadir nueva característica').
4.  Sube tus cambios (`git push origin feature/nueva-característica).
5.  Abre un Pull Request.


## Licencia 📄
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.


## Autores ✍️
Daniel Escalona -[GitHub] (https://github.com/DanielEsc0911)


## Colaboradores 🖥️👾
- Sergio Hurtado - [GitHub] (https://github.com/HSerch19)
- Daniel De Freitas - [GitHub] (https://github.com/)
- Georgelys Herrera - [GitHub] (https://github.com/georgbztt)
- Douglas Montoya - [GitHub] (https://github.com/DouglasMontoya)


