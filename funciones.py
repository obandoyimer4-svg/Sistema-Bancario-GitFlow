import os

def menu_principal():

    while True:

        print("\n==============================")
        print("     SISTEMA BANCARIO")
        print("==============================")
        print("1. Registrar cliente")
        print("2. Iniciar sesión")
        print("3. Crear cuenta bancaria")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            print("\nFunción Registrar Cliente en desarrollo.")

        elif opcion == "2":

            print("\nFunción Iniciar Sesión en desarrollo.")

        elif opcion == "3":

            print("\nFunción Crear Cuenta Bancaria en desarrollo.")

        elif opcion == "4":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción inválida.")