juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    
}


inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}


def leer_opcion():
    print("Solicita la opción del menu, valida que sea un entero entre 1 y 6")
    try:
        opcion_str = print (input("Ingrese opcion: "))
        opcion = int(opcion_str)
        if 1 <= opcion <= 6:
            return opcion
        else:
            return -1  
    except ValueError:
        return -1  


def stock_plataforma(plataforma, juegos, inventario):
    print("Muestra el total de stock disponible para una plataforma dada")
    plataforma_buscar = plataforma.strip().lower()
    total_stock = 0
    for codigo, datos in juegos.items():
        if datos[1].lower() == plataforma_buscar:
            if codigo in inventario:
                total_stock += inventario[codigo][1]    

    print(f"El total de stock disponibles es: {total_stock}")



def busqueda_precio(p_min, p_max, juegos, inventario):
    print("Busca juegos por rango de precio y stock disponible, ordenados alfabeticamente")
    resultados = []
    for codigo, datos_inv in inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]
        if p_min <= precio <= p_max and stock > 0:
            if codigo in juegos:
                titulo = juegos[codigo][0]
                resultados.append(f"{titulo} {codigo}")
              
    if resultados:
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios")  

    

 