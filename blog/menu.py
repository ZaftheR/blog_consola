def mostrar_menu():

    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tags")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    try:
        opcion = input("Elige una opción (1-7): ").strip()
        int(opcion)
        return opcion

    except ValueError:
        return None