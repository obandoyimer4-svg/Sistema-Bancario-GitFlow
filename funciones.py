import os

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
        print("5. Transferencias")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            print("\nFunción Registrar Cliente en desarrollo.")

        elif opcion == "2":

            print("\nFunción Iniciar Sesión en desarrollo.")

        elif opcion == "3":

            print("\nFunción Crear Cuenta Bancaria en desarrollo.")

        elif opcion == "4":

            print(f"\nSu saldo actual es: ${saldo}")

        elif opcion == "5":

            cuenta = input("Ingrese el número de cuenta destino: ")
            valor = float(input("Ingrese el valor a transferir: "))

            if valor <= saldo:

                saldo -= valor

                print("\nTransferencia realizada correctamente.")
                print(f"Cuenta destino: {cuenta}")
                print(f"Saldo restante: ${saldo}")

            else:

                print("\nSaldo insuficiente.")

        elif opcion == "6":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción inválida.")