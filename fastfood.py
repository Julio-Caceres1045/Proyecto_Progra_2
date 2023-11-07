from datetime import datetime
from collections import deque


menu = {
    'hamburguesa': 5.99,
    'papas fritas': 2.49,
    'refresco': 1.99,
    'hot dog': 3.99,
    'ensalada': 4.49,
    'nuggets de pollo': 4.99,
    'helado': 2.99,
    # Agrega más elementos al menú aquí
}
inventario = {
    'hamburguesa': 100,
    'papas fritas': 200,
    'refresco': 150,
    'hot dog': 100,
    'ensalada': 50,
    'nuggets de pollo': 80,
    'helado': 60,
    
}

carrito = []
cola_pedidos = deque()

ESTADO_PENDIENTE = "pendiente"
ESTADO_PREPARACION = "en preparación"
ESTADO_LISTO = "listo para servir"

clientes = {}

def menu_principal():
    while True:
        print("Menú Principal:")
        print("1. Gestión de Pedidos")
        print("2. Preparar Pedidos")
        print("3. Facturación y Pagos")
        print("4. Administración de Clientes")
        print("5. Mostrar Inventario")
        print("6. Editar Inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            menu_gestion_pedidos()
        elif opcion == '2':
            menu_preparar_pedidos()
        elif opcion == '3':
            menu_facturacion_pagos()
        elif opcion == '4':
            menu_administracion_clientes()
        elif opcion == '5':
            mostrar_inventario()
        elif opcion == '6':
            editar_inventario()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
