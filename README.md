# blog_consola

Sistema de gestión de blog por consola desarrollado en Python.

## Descripción

Esta versión del proyecto incorpora Programación Orientada a Objetos (POO) y persistencia mediante archivos JSON.

El sistema permite gestionar publicaciones de un blog desde consola, realizando búsquedas, filtrados, validaciones y guardado de datos.

## Clases principales

### Autor

Representa al autor de una publicación.

Atributos:

- nombre
- bio
- especialidad
- redes_sociales

### Post

Representa una publicación del blog.

Atributos:

- id
- titulo
- contenido
- autor
- tags
- estado

Cada post contiene una instancia de la clase Autor.

### Blog

Centraliza la lógica principal del sistema.

Permite:

- listar posts
- buscar por título
- filtrar por tag
- agregar nuevos posts
- obtener todos los posts

## Persistencia JSON

Los datos se almacenan en el archivo:

```text
posts.json
```

Al iniciar el programa:

- se cargan los datos desde `posts.json`
- los diccionarios se convierten en objetos

Al guardar:

- los objetos se convierten nuevamente en diccionarios
- los datos se almacenan en `posts.json`

## Estructura del proyecto

```text
blog_consola/
│
├── main.py
├── README.md
├── posts.json
├── .gitignore
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Funcionalidades

1. Ver todos los posts.
2. Buscar por título.
3. Filtrar por tag.
4. Crear nuevo post.
5. Validar posts.
6. Guardar posts en JSON.
7. Salir.

## Cómo ejecutar el proyecto

Desde la carpeta raíz:

```bash
python main.py
```

## Instalación en otro equipo

Clonar el repositorio:

```bash
git clone https://github.com/ZaftheR/blog_consola.git
cd blog_consola
```

Opcionalmente crear un entorno virtual:

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

Ejecutar el programa:

```bash
python main.py
```

Salir del entorno virtual:

```bash
deactivate
```

## Cambios respecto a la versión anterior

- Se incorporó Programación Orientada a Objetos.
- Se agregaron las clases Autor, Post y Blog.
- Se incorporó persistencia mediante JSON.
- Los posts se cargan desde `posts.json`.
- Los posts pueden guardarse en `posts.json`.
- La lógica principal se centralizó en la clase Blog.
- Se mantuvo la estructura modular del proyecto.
