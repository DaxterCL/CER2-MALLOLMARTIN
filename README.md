# Fundación Patrimonio Vivo – Catálogo digital de lugares patrimoniales

Certamen N°2 – Explotación de Base de Datos (EIN082B Taller Lenguaje de Programación).
Aplicación web hecha con **Python** y **Django** que centraliza los lugares patrimoniales
de la fundación. Cualquier visitante puede consultar el catálogo; el área de gestión
requiere iniciar sesión y, para agregar o modificar lugares, tener permisos.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación y ejecución

Desde la carpeta del proyecto (la que contiene `manage.py`):

### 1. Crear y activar un entorno virtual

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Si PowerShell bloquea la activación, ejecutar antes: `Set-ExecutionPolicy -Scope Process Bypass`

Linux / macOS:

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar las dependencias

```
pip install -r requirements.txt
```

### 3. Configurar la base de datos

El proyecto usa SQLite, por lo que no hay que instalar nada adicional. Se crean las tablas con:

```
python manage.py makemigrations catalogo
python manage.py migrate
```

### 4. Cargar los datos iniciales

```
python manage.py loaddata datos_iniciales
```

Carga las categorías y los lugares de ejemplo incluidos en `catalogo/fixtures/datos_iniciales.json`.

### 5. Crear un usuario administrador

```
python manage.py createsuperuser
```

Pide un nombre de usuario, un correo (opcional) y una contraseña. Al escribir la
contraseña no se muestra nada en pantalla, es normal.

### 6. Ejecutar la aplicación

```
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Configuración de usuarios

Para probar los distintos niveles de acceso, entrar a http://127.0.0.1:8000/admin/
con el superusuario y, en **Usuarios**, crear:

1. Un usuario sin permisos: puede iniciar sesión y ver Gestión, pero no agregar ni
   modificar lugares.
2. Otro usuario con permisos: en "Permisos de usuario", asignarle *Can add lugar
   patrimonial* y *Can change lugar patrimonial*. Puede agregar y modificar lugares.

Las contraseñas de los usuarios creados desde Admin deben tener al menos 8 caracteres
y no ser solo números.

| Tipo de usuario          | Qué puede hacer                                    |
|--------------------------|----------------------------------------------------|
| Anónimo                  | Ver inicio, catálogo, detalle, categorías y filtro |
| Autenticado sin permisos | Lo anterior + entrar a Gestión (solo consulta)     |
| Con permisos             | Lo anterior + agregar y modificar lugares          |
| Superusuario             | Todo, incluido Django Admin en `/admin/`           |

## Rutas principales

| Ruta                           | Acceso                             |
|--------------------------------|------------------------------------|
| `/`                            | Público                            |
| `/catalogo/`                   | Público                            |
| `/lugar/<id>/`                 | Público                            |
| `/categorias/`                 | Público                            |
| `/categorias/<id>/`            | Público                            |
| `/login/` y `/logout/`         | Público                            |
| `/gestion/`                    | Usuario autenticado                |
| `/gestion/lugar/nuevo/`        | Autenticado + permiso de agregar   |
| `/gestion/lugar/<id>/editar/`  | Autenticado + permiso de modificar |
| `/admin/`                      | Administrador                      |

## Cómo se cubren los requisitos funcionales

| Código | Dónde está                                                                                  |
|--------|---------------------------------------------------------------------------------------------|
| RF01   | `inicio` (vista) y `templates/inicio.html`                                                  |
| RF02   | `catalogo` (vista), consulta con ORM a `LugarPatrimonial`                                   |
| RF03   | `detalle_lugar` (vista) y `templates/detalle_lugar.html`                                    |
| RF04   | Modelo `Categoria` y vista `lista_categorias`                                               |
| RF05   | `lugares_por_categoria` (vista), filtra con `filter(categoria=...)`                         |
| RF06   | `catalogo/admin.py` (ambos modelos registrados en Django Admin)                             |
| RF07   | `templates/base.html`, `_tarjeta_lugar.html` y `static/css/estilos.css`                     |
| RF08   | `LoginView` en `patrimonio_vivo/urls.py` y `templates/login.html`                           |
| RF09   | `LogoutView` en `patrimonio_vivo/urls.py` (botón en la barra de navegación)                 |
| RF10   | Decorador `@login_required` en la vista `gestion`                                           |
| RF11   | Permisos `add_lugarpatrimonial` y `change_lugarpatrimonial` (asignados desde Django Admin)  |
| RF12   | `@permission_required(..., raise_exception=True)` responde 403 aunque se use la URL directa |

## Estructura del proyecto

```
manage.py
requirements.txt
patrimonio_vivo/        Configuración del proyecto (settings, urls)
catalogo/               Aplicación principal
    models.py           Categoria y LugarPatrimonial (relacionados por ForeignKey)
    views.py            Vistas públicas y de gestión
    urls.py             Rutas de la aplicación
    forms.py            Formulario para agregar/editar lugares
    admin.py            Registro de modelos en Django Admin
    fixtures/           Datos iniciales (categorías y lugares) en formato JSON
templates/              Plantillas HTML (base.html, páginas y 403.html)
static/css/estilos.css  Hoja de estilos
```

## Notas

- Las imágenes se manejan con una **URL** (campo `imagen`), sin subir archivos.
- Si se agregan o modifican lugares y se quiere actualizar el archivo de datos iniciales:
  `python manage.py dumpdata catalogo --indent 2 --output catalogo/fixtures/datos_iniciales.json`