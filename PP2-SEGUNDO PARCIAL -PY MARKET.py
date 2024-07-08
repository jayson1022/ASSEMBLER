import csv
#JAYSON ROSARIO LOPEZ 
#MATRICULA 18-1597
def cargar_productos(ruta_archivo):
    productos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                productos.append({
                    'nombre': fila['nombre_producto'],
                    'precio': float(fila['precio']),
                    'descuento': float(fila['porcentaje_descuento'])
                })
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return productos

def calcular_precio_promedio(productos):
    if not productos:
        return 0
    total_precio = sum(producto['precio'] for producto in productos)
    return total_precio / len(productos)

def aplicar_descuentos(productos):
    for producto in productos:
        producto['precio_con_descuento'] = producto['precio'] * (1 - producto['descuento'] / 100)

def mostrar_productos(productos):
    for producto in productos:
        print(f"Producto: {producto['nombre']}, Precio Original: {producto['precio']}, "
              f"Descuento: {producto['descuento']}%, Precio con Descuento: {producto.get('precio_con_descuento', 'N/A')}")

ruta_archivo = 'productos.csv'
productos = cargar_productos(ruta_archivo)

precio_promedio = calcular_precio_promedio(productos)
print(f"Precio promedio de los productos: {precio_promedio:.2f}")

aplicar_descuentos(productos)

mostrar_productos(productos)
