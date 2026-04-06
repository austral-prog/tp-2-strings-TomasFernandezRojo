def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre = input("Nombre:")
    email = input("Email:")
    notas1 = int(input("Nota1: "))
    notas2 = int(input("Nota2: "))
    notas3 = int(input("Nota3: "))
    nombreT = nombre.strip().title()
    Suma = int(notas1 + notas2 + notas3)
    promedio = (Suma / 3)
    
    
    
    encabezado = """================
FICHA DEL ALUMNO
================"""
    

    print(encabezado)
    print(f"Nombre: {nombreT}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombreT)}")
    print("Iniciales:", f"{nombreT[0]}{nombreT[nombreT.find(" ")+1]}", )
    print("Usuario:", f"{(nombreT[nombreT.find(" ")+1:]).lower()}.{(nombreT[0:nombreT.find(" ")]).lower()}")
    print("Email Valido:", str("@" in email))
    print(f"dominio: {email[email.find("@")+1:]}") # de @ al final
    print(f"Nombre para archivo: {nombreT.replace(" ", "_")}") # Espacio por _
    print(f"Cantidad de a: {nombreT.count("a")}") # Cantidad de A
    print(f"Codigo Secreto: {nombreT[::-1].upper()}") #Nombre dado vuelta
    print("Nota 1:" + str(notas1))
    print("Nota 2:" + str(notas2))
    print("Nota 3:" + str(notas3))
    print("Sumas:" + str(Suma))
    print(f"Promedio: {str(promedio)}" ) 
    print(f"Promedio Entero: {int(promedio)}")
    print("========================")
ficha()

