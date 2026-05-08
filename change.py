def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input())
    dinero_recibido = int(input())
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("")
    print("Vuelto")
    print("")

    vuelto = dinero_recibido - gasto
    pesos_enteros = int(vuelto)
    centavos = round((vuelto - pesos_enteros) * 100)
    print("Pesos:")
    print(pesos_enteros)
    print("Centavos:")
    print(centavos)

if __name__ == "__main__":
    change()