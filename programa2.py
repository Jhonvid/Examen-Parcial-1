def obtener_datos_productos(tamaño):
    nombres=[]
    precios=[]
    for i in range(tamaño):
        nombre=input(f"ingrese el nombre del producto [{i+1}]: ")
        precio=float(input(f"ingrese el precio del producto [{i+1}]: "))
        nombres.append(nombre)
        precios.append(precio)
        
    return nombres, precios

def crear_arreglo_final(nombres, precios):
    productos_precios=[]
    for i in range(len(nombres)):
        productos_precios.append(f"{nombres[i]}: ${precios[i]}")
    return productos_precios

def mostrar_productos_precios(productos_precios):
    print("\nlista de productos y precios:")
    for producto in productos_precios:
        print(producto)

def main():
    tamaño=int(input("ingrese la cantidad de productos: "))
    nombres, precios=obtener_datos_productos(tamaño)
    productos_precios=crear_arreglo_final(nombres, precios)
    mostrar_productos_precios(productos_precios)

main()
