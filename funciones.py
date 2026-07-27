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


def iniciar_sesion():

    print("\n===== INICIAR SESIÓN =====")

    documento = input("Ingrese su documento: ")

    ruta = "data/usuarios.json"

    if not os.path.exists(ruta):

        print("\nNo hay clientes registrados.")
        return

    with open(ruta, "r", encoding="utf-8") as archivo:

        try:
            clientes = json.load(archivo)
        except:
            clientes = []

    for cliente in clientes:

        if cliente["documento"] == documento:

            print(f"\nBienvenido(a), {cliente['nombre']}")
            return

    print("\nCliente no encontrado.")

def buscar_cliente():

    print("\n===== BUSCAR CLIENTE =====")

    documento = input("Ingrese el documento a buscar: ")

    ruta = "data/usuarios.json"

    if not os.path.exists(ruta):
        print("\nNo hay clientes registrados.")
        return

    with open(ruta, "r", encoding="utf-8") as archivo:

        try:
            clientes = json.load(archivo)
        except:
            clientes = []

    for cliente in clientes:

        if cliente["documento"] == documento:

            print("\n===== CLIENTE ENCONTRADO =====")
            print("Nombre:", cliente["nombre"])
            print("Documento:", cliente["documento"])
            print("Teléfono:", cliente["telefono"])

            return

    print("\nCliente no encontrado.")

def actualizar_cliente():

    documento = input("\nIngrese el documento del cliente: ")

    with open("data/usuarios.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)

    for cliente in clientes:

        if cliente["documento"] == documento:

            cliente["nombre"] = input("Nuevo nombre: ")
            cliente["telefono"] = input("Nuevo teléfono: ")

            with open("data/usuarios.json", "w", encoding="utf-8") as archivo:
                json.dump(clientes, archivo, indent=4, ensure_ascii=False)

            print("\nCliente actualizado correctamente.")
            return

    print("\nCliente no encontrado.")

def eliminar_cliente():

    documento = input("\nIngrese el documento del cliente a eliminar: ")

    with open("data/usuarios.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)

    nuevos_clientes = []

    eliminado = False

    for cliente in clientes:

        if cliente["documento"] != documento:
            nuevos_clientes.append(cliente)
        else:
            eliminado = True

    with open("data/usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(nuevos_clientes, archivo, indent=4, ensure_ascii=False)

    if eliminado:
        print("\nCliente eliminado correctamente.")
    else:
        print("\nCliente no encontrado.")

def consultar_cuenta():

    numero = int(input("\nIngrese el número de cuenta: "))

    ruta = "data/cuentas.json"

    if not os.path.exists(ruta):
        print("\nNo existen cuentas registradas.")
        return

    with open(ruta, "r", encoding="utf-8") as archivo:
        cuentas = json.load(archivo)

    for cuenta in cuentas:

        if cuenta["numero_cuenta"] == numero:

            print("\n===== DATOS DE LA CUENTA =====")
            print("Titular:", cuenta["titular"])
            print("Número:", cuenta["numero_cuenta"])
            print("Tipo:", cuenta["tipo_cuenta"])
            print("Saldo:", cuenta["saldo"])
            return

    print("\nCuenta no encontrada.")

def actualizar_cuenta():

    numero = int(input("\nIngrese el número de cuenta: "))

    with open("data/cuentas.json", "r", encoding="utf-8") as archivo:
        cuentas = json.load(archivo)

    for cuenta in cuentas:

        if cuenta["numero_cuenta"] == numero:

            print("\n1. Cuenta de Ahorros")
            print("2. Cuenta Corriente")

            opcion = input("Seleccione el nuevo tipo: ")

            if opcion == "1":
                cuenta["tipo_cuenta"] = "Ahorros"

            elif opcion == "2":
                cuenta["tipo_cuenta"] = "Corriente"

            else:
                print("\nOpción inválida.")
                return

            with open("data/cuentas.json", "w", encoding="utf-8") as archivo:
                json.dump(cuentas, archivo, indent=4, ensure_ascii=False)

            print("\nCuenta actualizada correctamente.")
            return

    print("\nCuenta no encontrada.")

def eliminar_cuenta():

    numero = int(input("\nIngrese el número de cuenta: "))

    with open("data/cuentas.json", "r", encoding="utf-8") as archivo:
        cuentas = json.load(archivo)

    nuevas_cuentas = []

    eliminada = False

    for cuenta in cuentas:

        if cuenta["numero_cuenta"] != numero:
            nuevas_cuentas.append(cuenta)
        else:
            eliminada = True

    with open("data/cuentas.json", "w", encoding="utf-8") as archivo:
        json.dump(nuevas_cuentas, archivo, indent=4, ensure_ascii=False)

    if eliminada:
        print("\nCuenta eliminada correctamente.")
    else:
        print("\nCuenta no encontrada.")



def crear_cuenta():

    print("\n===== CREAR CUENTA BANCARIA =====")

    documento = input("Ingrese el documento del cliente: ")

    ruta_clientes = "data/usuarios.json"

    with open(ruta_clientes, "r", encoding="utf-8") as archivo:

        try:
            clientes = json.load(archivo)
        except:
            clientes = []

    cliente_encontrado = None

    for cliente in clientes:

        if cliente["documento"] == documento:

            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:

        print("\nCliente no encontrado.")
        return

    print("\nSeleccione el tipo de cuenta:")
    print("1. Cuenta de Ahorros")
    print("2. Cuenta Corriente")

    opcion = input("Opción: ")

    if opcion == "1":

        tipo_cuenta = "Ahorros"

    elif opcion == "2":

        tipo_cuenta = "Corriente"

    else:

        print("\nOpción inválida.")
        return

    ruta_cuentas = "data/cuentas.json"

    if os.path.exists(ruta_cuentas):

        with open(ruta_cuentas, "r", encoding="utf-8") as archivo:

            try:
                cuentas = json.load(archivo)
            except:
                cuentas = []

    else:

        cuentas = []

    numero_cuenta = 1001 + len(cuentas)

    nueva_cuenta = {
        "numero_cuenta": numero_cuenta,
        "documento": documento,
        "titular": cliente_encontrado["nombre"],
        "tipo_cuenta": tipo_cuenta,
        "saldo": 0
    }

    cuentas.append(nueva_cuenta)

    with open(ruta_cuentas, "w", encoding="utf-8") as archivo:

        json.dump(cuentas, archivo, indent=4, ensure_ascii=False)

    print("\nCuenta creada exitosamente.")
    print(f"Titular: {cliente_encontrado['nombre']}")
    print(f"Número de cuenta: {numero_cuenta}")
    print(f"Tipo de cuenta: {tipo_cuenta}")

def menu_principal():

    saldo = 100000

    while True:

        print("\n==============================")
        print("     SISTEMA BANCARIO")
        print("==============================")
        print("1. Registrar cliente")
        print("2. Buscar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Crear cuenta bancaria")
        print("6. Consultar cuenta")
        print("7. Actualizar cuenta")
        print("8. Eliminar cuenta")
        print("9. Iniciar sesión")
        print("10. Consultar saldo")
        print("11. Consignar dinero")
        print("12. Transferencias")
        print("13. Retirar dinero")
        print("14. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

         registrar_cliente()

        elif opcion == "2":

         buscar_cliente()

        elif opcion == "3":

         actualizar_cliente()

        elif opcion == "4":

         eliminar_cliente()

        elif opcion == "5":

         crear_cuenta()

        elif opcion == "6":

         consultar_cuenta()

        elif opcion == "7":

         actualizar_cuenta()

        elif opcion == "8":

         eliminar_cuenta()

        elif opcion == "9":

         iniciar_sesion()

        elif opcion == "10":

         print(f"\nSu saldo actual es: ${saldo}")

        elif opcion == "11":

          valor = float(input("\nIngrese el valor a consignar: "))

          if valor > 0:

            saldo += valor

            print("\nConsignación realizada correctamente.")
            print(f"Nuevo saldo: ${saldo}")

          else:

           print("\nEl valor debe ser mayor que cero.")

        elif opcion == "12":

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


        elif opcion == "12":

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

        elif opcion == "13":

            valor = float(input("\nIngrese el valor a retirar: "))

            if valor > 0 and valor <= saldo:

               saldo -= valor

               print("\nRetiro realizado correctamente.")
               print(f"Saldo restante: ${saldo}")

            elif valor > saldo:

             print("\nSaldo insuficiente.")

            else:

             print("\nEl valor debe ser mayor que cero.")

        elif opcion == "14":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción inválida.")