perfil_autor = {
    "nombre": "Lucía Gómez",
    "bio": "Escribo sobre tecnología y comparto soluciones prácticas.",
    "especialidad": "Desarrollo web y Python básico",
    "redes_sociales": ["@lucia.codes", "@lucia_tech"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Web", "Backend", "Tutorial"}

posts = [
    {
        "id": 1,
        "titulo": "Aprendiendo Python paso a paso",
        "contenido": "Conceptos básicos para arrancar con Python.",
        "autor": perfil_autor,
        "etiquetas": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Mi primera app con Flask",
        "contenido": "Ejemplo sencillo para crear una app web con Flask.",
        "autor": perfil_autor,
        "etiquetas": ["Python", "Web", "Flask"],
        "estado": "borrador"
    },
    # Post intencionalmente con errores para validar
    {
        "id": 3,
        "titulo": "",                 # título vacío
        # "contenido" falta intencionalmente
        "autor": "Lucía Gómez",       # autor no es diccionario
        "etiquetas": "Python",        # etiquetas no es lista
        "estado": "publicado_invalido" # estado inválido
    }
]
