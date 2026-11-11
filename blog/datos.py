import json
from blog.modelos import Post

ARCHIVO_POSTS = "posts.json"


# Cargar posts desde el archivo JSON
def cargar_posts():
    try:
        with open(ARCHIVO_POSTS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        posts = []

        for item in datos:
            post = Post.desde_diccionario(item)
            posts.append(post)
        return posts

    except FileNotFoundError:
        print("No se encontró el archivo posts.json")
        return []

    except json.JSONDecodeError:
        print("El archivo posts.json está vacío o tiene errores")
        return []

    except Exception as error:
        print(f"Error al cargar los posts: {error}")
        return []


# Guardar posts en el archivo JSON
def guardar_posts(posts):
    try:
        datos = []

        for post in posts:
            datos.append(post.a_diccionario())

        with open(ARCHIVO_POSTS, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Posts guardados correctamente")

    except Exception as error:
        print(f"Error al guardar los posts: {error}")
