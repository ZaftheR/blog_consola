from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_etiqueta
from blog.validaciones import validar_post

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            print("Opción inválida, intenta de nuevo")
            continue

        if opcion == "1":
            listar_posts(posts)

        elif opcion == "2":
            termino = input("Buscar por titulo: ").strip()
            if termino == "":
                print("Búsqueda vacía. Ingresá un término válido.")
                continue
            resultados = buscar_por_titulo(posts, termino)
            if resultados:
                print("\nResultados de la búsqueda:")
                for p in resultados:
                    autor = p.get("autor")
                    nombre_autor = autor.get("nombre") if isinstance(autor, dict) else "<autor inválido>"
                    print(f"- {p.get('titulo')} | Autor: {nombre_autor} | Estado: {p.get('estado')}")
            else:
                print("No se encontraron posts con ese término.")

        elif opcion == "3":
            etiqueta = input("Ingresá una etiqueta para filtrar: ").strip()
            if etiqueta == "":
                print("Etiqueta vacía. Ingresá una etiqueta válida.")
                continue
            filtrados = filtrar_por_etiqueta(posts, etiqueta)
            if filtrados:
                print(f"\nPosts con la etiqueta '{etiqueta}':")
                for p in filtrados:
                    print(f"- {p.get('titulo')} | Estado: {p.get('estado')}")
            else:
                print("No hay posts con esa etiqueta.")

        elif opcion == "4":
            print("\nValidando posts...")
            for p in posts:
                valido, mensaje = validar_post(p)
                pid = p.get("id", "<sin id>")
                if valido:
                    print(f"Post {pid}: válido")
                else:
                    print(f"Post {pid}: error - {mensaje}")

        elif opcion == "5":
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")
