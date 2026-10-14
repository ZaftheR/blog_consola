def listar_posts(lista):
    """
    Muestra título, autor y estado de cada post.
    Usa .get() para evitar KeyError.
    """
    if not lista:
        print("No hay posts para mostrar.")
        return

    print("\nPosts disponibles:")
    for post in lista:
        titulo = post.get("titulo", "<sin titulo>")
        autor = post.get("autor")
        nombre_autor = autor.get("nombre") if isinstance(autor, dict) else "<autor inválido>"
        estado = post.get("estado", "<sin estado>")
        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    """
    Retorna lista de posts cuyo título contiene 'termino' (case-insensitive).
    """
    if termino is None or termino.strip() == "":
        return []
    termino = termino.lower()
    resultados = []
    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)
    return resultados


def filtrar_por_etiqueta(lista, etiqueta):
    """
    Retorna lista de posts que contienen 'etiqueta' en su lista de etiquetas (case-insensitive).
    """
    if etiqueta is None or etiqueta.strip() == "":
        return []
    etiqueta = etiqueta.lower()
    filtrados = []
    for post in lista:
        etiquetas = post.get("etiquetas")
        if isinstance(etiquetas, list):
            for e in etiquetas:
                if isinstance(e, str) and e.lower() == etiqueta:
                    filtrados.append(post)
                    break
    return filtrados
