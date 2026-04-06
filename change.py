def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto = float(input("ingresar gasto:"))
    #Al ponerle float te da resultado con coma, si le saco da lo que pongan.
    dinero_recibido = int(input("ingrese el dinero recibido:"))
    print("Ingresar Gasto:")
    print(gasto)
    print("Dinero recibido:")
    print(dinero_recibido) 
    #print("\n Vuelto \n")
    print("")
    print("Vuelto")
    print("")
          
    vuelto = dinero_recibido - gasto
    pesos_enteros = int(vuelto)
    centavos = int((vuelto - pesos_enteros) * 100) 
    print("Pesos:" , pesos_enteros)
    print("centavos:", centavos)
change()