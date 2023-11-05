
menu = {
    "Hamburguesa": 5.99,
    "Pizza": 7.99,
    "Papas Fritas": 2.99,
    "Refresco": 1.99,
}

def mostrar_menu():
    print("Menú:")
    for item, precio in menu.items():
        print(f"{item}: ${precio}")

def tomar_pedido():
    pedido = {}
    while True:
        item = input("¿Qué te gustaría pedir? (Escribe 'fin' para terminar): ")
        if item.lower() == "fin":
            break
        if item in menu:
            cantidad = int(input(f"Cantidad de {item}: "))
            if item in pedido:
                pedido[item] += cantidad
            else:
                pedido[item] = cantidad
        else:
            print("¡Lo siento, ese artículo no está en el menú!")

    return pedido

def calcular_total(pedido):
    total = 0
    for item, cantidad in pedido.items():
        total += menu[item] * cantidad
    return total

def main():
    print("¡Bienvenido al restaurante de comida rápida!")
    mostrar_menu()
    pedido = tomar_pedido()

    if not pedido:
        print("No se realizó ningún pedido.")
    else:
        print("Pedido:")
        for item, cantidad in pedido.items():
            print(f"{item}: {cantidad}")
        total = calcular_total(pedido)
        print(f"Total a pagar: ${total:.2f}")
        print("¡Gracias por su compra!")

if __name__ == "__main__":
    main()
