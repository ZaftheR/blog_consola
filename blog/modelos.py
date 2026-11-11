# Clase para representar un autor
class Autor:

    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

    # Convertir autor a diccionario
    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    # Crear autor desde un diccionario
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos.get("nombre", ""),
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )


# Clase para representar un post
class Post:

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    # Convertir post a diccionario
    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    # Crear post desde un diccionario
    @classmethod
    def desde_diccionario(cls, datos):

        autor = Autor.desde_diccionario(
            datos.get("autor", {})
        )

        return cls(
            datos.get("id", 0),
            datos.get("titulo", ""),
            datos.get("contenido", ""),
            autor,
            datos.get("tags", []),
            datos.get("estado", "")
        )


# Clase principal del blog
class Blog:

    def __init__(self):
        self.posts = []

    # Agregar un post
    def agregar_post(self, post):
        self.posts.append(post)

    # Mostrar todos los posts
    def listar_posts(self):

        if not self.posts:
            print("No hay posts disponibles.")
            return

        print("\nPosts disponibles:")

        for post in self.posts:
            print(
                f"- {post.titulo} | "
                f"Autor: {post.autor.nombre} | "
                f"Estado: {post.estado}"
            )

    # Buscar por título
    def buscar_por_titulo(self, termino):

        resultados = []

        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)

        return resultados

    # Filtrar por tag
    def filtrar_por_tag(self, tag):

        resultados = []

        for post in self.posts:

            for item in post.tags:

                if item.lower() == tag.lower():
                    resultados.append(post)
                    break

        return resultados

    # Obtener todos los posts
    def obtener_posts(self):
        return self.posts