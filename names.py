def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input()
    apellido = input()
    
    print(nombre.title)
    print(nombre.lower)
    print(nombre.upper)
    print("\t" + nombre)
names()