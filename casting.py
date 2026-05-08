def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())
    
    
    precioDescuento = precio - descuento
    total = precioDescuento * cantidad
    
    print(f"precio: {precio} ")
    print(f"Descuento: {descuento}")
    print(f"Precio Con descuento: {precioDescuento}")
    print(f"total: {total}")
    
#casting()
     