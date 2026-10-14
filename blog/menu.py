def mostrar_menu():
    """
    Muestra el menú y devuelve la opción elegida como string.
    Usa try/except para evitar que texto rompa el programa.
    """
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por etiqueta")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = input("Elige una opción (1-5): ").strip()
        int(opcion)  # valida que sea numérico
        return opcion
    except ValueError:
        return None
