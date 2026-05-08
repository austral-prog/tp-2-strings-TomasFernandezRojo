def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())
    
    
    precioDescuento = precio - descuento
    total = precioDescuento * cantidad
    
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precioDescuento}")
    print(f"Total: {total}")
    
#casting()
     