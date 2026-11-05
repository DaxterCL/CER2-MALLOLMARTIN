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



## Notas

- Las imágenes se manejan con una **URL** (campo `imagen`), sin subir archivos.
- Si se agregan o modifican lugares y se quiere actualizar el archivo de datos iniciales:
  `python manage.py dumpdata catalogo --indent 2 --output catalogo/fixtures/datos_iniciales.json`
