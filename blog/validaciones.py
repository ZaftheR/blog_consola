estados_post = ("borrador", "publicado", "archivado")


def validar_post(post):

    if not post.titulo:
        return False, "El título está vacío."

    if not post.contenido:
        return False, "El contenido está vacío."

    if not post.autor:
        return False, "El post no tiene autor."

    if not post.autor.nombre:
        return False, "El autor no tiene nombre."

    if not isinstance(post.tags, list):
        return False, "Los tags deben estar en una lista."
    
    if len(post.tags) == 0:
        return False, "El post no tiene tags."

    if post.estado not in estados_post:
        return False, f"El estado '{post.estado}' no es válido."

    return True, ""
