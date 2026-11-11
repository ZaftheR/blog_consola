# main.py

from blog.modelos import Blog, Autor, Post
from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.validaciones import validar_post


if __name__ == "__main__":

    blog = Blog()

    posts_cargados = cargar_posts()

    for post in posts_cargados:
        blog.agregar_post(post)

    while True:

        opcion = mostrar_menu()

        if opcion is None:
            print("Opción inválida")
            continue

        # Ver todos los posts
        if opcion == "1":

            blog.listar_posts()

        # Buscar por título
        elif opcion == "2":

            termino = input("Buscar por titulo: ").strip()

            resultados = blog.buscar_por_titulo(termino)

            if resultados:

                print("\nResultados encontrados:")

                for post in resultados:
                    print(
                        f"- {post.titulo} | "
                        f"Autor: {post.autor.nombre}"
                    )

            else:
                print("No se encontraron resultados.")

        # Filtrar por tag
        elif opcion == "3":

            tag = input("Ingresá un tag: ").strip()

            if tag == "":
                print("Debe ingresar un tag.")
                continue

            resultados = blog.filtrar_por_tag(tag)

            if resultados:

                print(f"\nPosts con el tag '{tag}':")

                for post in resultados:
                    print(
                        f"- {post.titulo} | "
                        f"Estado: {post.estado}"
                    )

            else:
                print("No se encontraron posts.")

        # Crear nuevo post
        elif opcion == "4":

            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()

            if titulo == "" or contenido == "":
                print("Los campos no pueden estar vacíos.")
                continue

            nombre = input("Nombre del autor: ").strip()

            if nombre == "":
                print("El nombre del autor no puede estar vacío.")
                continue

            bio = input("Bio: ").strip()
            especialidad = input("Especialidad: ").strip()

            redes_sociales = input(
                "Redes sociales separadas por coma: "
            )

            tags = input(
                "Tags separados por coma: "
            ).strip()

            if tags == "":
                print("Debe ingresar al menos un tag.")
                continue

            estado = input(
                "Estado (borrador/publicado/archivado): "
            ).strip()

            autor = Autor(
                nombre,
                bio,
                especialidad,
                redes_sociales.split(",")
            )

            nuevo_post = Post(
                len(blog.obtener_posts()) + 1,
                titulo,
                contenido,
                autor,
                tags.split(","),
                estado
            )

            blog.agregar_post(nuevo_post)

            print("Post creado correctamente.")

        # Validar posts
        elif opcion == "5":

            print("\nValidando posts...")

            for post in blog.obtener_posts():

                valido, mensaje = validar_post(post)

                if valido:
                    print(f"Post {post.id}: válido")
                else:
                    print(f"Post {post.id}: {mensaje}")

        # Guardar JSON
        elif opcion == "6":

            guardar_posts(
                blog.obtener_posts()
            )

        # Salir
        elif opcion == "7":

            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida")