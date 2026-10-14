from blog.datos import estados_post

def validar_post(post):
    """
    Valida un post.
    Retorna (True, "") si es válido.
    Si hay error, retorna (False, "mensaje").
    Revisa: tipo dict, claves, título, contenido, autor dict con nombre, etiquetas lista, estado válido.
    """
    if not isinstance(post, dict):
        return False, "El post no es un diccionario."

    claves_necesarias = ["id", "titulo", "contenido", "autor", "etiquetas", "estado"]
    for clave in claves_necesarias:
        if clave not in post:
            return False, f"Falta la clave '{clave}'."

    titulo = post.get("titulo")
    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, "El título está vacío o no es texto."

    contenido = post.get("contenido")
    if not isinstance(contenido, str) or contenido.strip() == "":
        return False, "El contenido está vacío o no es texto."

    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, "El autor no es un diccionario."
    if "nombre" not in autor or not isinstance(autor.get("nombre"), str) or autor.get("nombre").strip() == "":
        return False, "El autor no tiene la clave 'nombre' o está vacía."

    etiquetas = post.get("etiquetas")
    if not isinstance(etiquetas, list):
        return False, "Las etiquetas no están en una lista."

    estado = post.get("estado")
    if estado not in estados_post:
        return False, f"El estado '{estado}' no es válido."

    return True, ""
