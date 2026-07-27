import json
import os


def registrar_cliente():

    print("\n===== REGISTRO DE CLIENTE =====")

    nombre = input("Ingrese el nombre: ")
    documento = input("Ingrese el documento: ")
    telefono = input("Ingrese el teléfono: ")

    cliente = {
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono
    }

    ruta = "data/usuarios.json"

    if os.path.exists(ruta):

        with open(ruta, "r", encoding="utf-8") as archivo:

            try:
                clientes = json.load(archivo)
            except:
                clientes = []

    else:

        clientes = []

    clientes.append(cliente)

    with open(ruta, "w", encoding="utf-8") as archivo:

        json.dump(clientes, archivo, indent=4, ensure_ascii=False)

    print("\nCliente registrado correctamente.")
    print("Los datos fueron guardados en usuarios.json")


def menu_principal():

    saldo = 100000

    while True:

        print("\n==============================")
        print("     SISTEMA BANCARIO")
        print("==============================")
        print("1. Registrar cliente")
        print("2. Iniciar sesión")
        print("3. Crear cuenta bancaria")
        print("4. Consultar saldo")
        print("5. Consignar dinero")
        print("6. Transferencias")
        print("7. Retirar dinero")
        print("8. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            registrar_cliente()

        elif opcion == "2":

            print("\nFunción Iniciar Sesión en desarrollo.")

        elif opcion == "3":

            print("\nFunción Crear Cuenta Bancaria en desarrollo.")

        elif opcion == "4":

            print(f"\nSu saldo actual es: ${saldo}")

        elif opcion == "5":

            valor = float(input("\nIngrese el valor a consignar: "))

            if valor > 0:

                saldo += valor

                print("\nConsignación realizada correctamente.")
                print(f"Nuevo saldo: ${saldo}")

            else:

                print("\nEl valor debe ser mayor que cero.")

        elif opcion == "6":

            cuenta = input("\nIngrese el número de cuenta destino: ")
            valor = float(input("Ingrese el valor a transferir: "))

            if valor > 0 and valor <= saldo:

                saldo -= valor

                print("\nTransferencia realizada correctamente.")
                print(f"Cuenta destino: {cuenta}")
                print(f"Saldo restante: ${saldo}")

            elif valor > saldo:

                print("\nSaldo insuficiente.")

            else:

                print("\nEl valor debe ser mayor que cero.")

        elif opcion == "7":

            valor = float(input("\nIngrese el valor a retirar: "))

            if valor > 0 and valor <= saldo:

                saldo -= valor

                print("\nRetiro realizado correctamente.")
                print(f"Saldo restante: ${saldo}")

            elif valor > saldo:

                print("\nSaldo insuficiente para realizar el retiro.")

            else:

                print("\nEl valor debe ser mayor que cero.")

        elif opcion == "8":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción inválida.")