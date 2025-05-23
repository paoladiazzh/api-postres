from django.db import models

#Para referencia
class Postre:
    def __init__(self, id, nombre, sabor, tamanio):
        self.id = id
        self.nombre = nombre
        self.sabor = sabor
        self.tamanio = tamanio
