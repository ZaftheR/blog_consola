# blog_consola

Sistema de blog por consola organizado en módulos.

## Qué hace
Permite listar posts, buscar por título, filtrar por etiqueta y validar la estructura de los posts.

## Cómo ejecutar
1. Colocar la carpeta `blog_consola` en tu equipo.
2. Abrir terminal en la carpeta raíz `blog_consola`.
3. Ejecutar:

## Estructura
- `main.py` : Orquesta la ejecución y muestra el menú.
- `blog/` : Paquete con módulos:
  - `datos.py` : Datos base (perfil_autor, estados_post, etiquetas_blog, posts).
  - `menu.py` : Función para mostrar el menú y leer la opción.
  - `operaciones.py` : Funciones listar_posts, buscar_por_titulo, filtrar_por_etiqueta.
  - `validaciones.py` : Función validar_post.

## Notas
- Un post en `datos.py` incluye errores intencionales para probar la validación.
- Las búsquedas y filtros usan `.lower()` para ignorar mayúsculas/minúsculas.

# Clonar o copiar el proyecto (si está en GitHub)
git clone <URL-del-repositorio>
cd blog_consola

# (Opcional) Crear y activar un entorno virtual
# Windows
python -m venv env
env\Scripts\activate

# macOS / Linux
python3 -m venv env
source env/bin/activate

# Instalar dependencias (si existe requirements.txt)
pip install -r requirements.txt

# Ejecutar el programa
python main.py

# Al terminar, salir del entorno virtual (si lo activaste)
deactivate

