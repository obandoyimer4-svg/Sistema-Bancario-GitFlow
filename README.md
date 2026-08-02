# Sistema-Bancario-GitFlow
# Sistema Bancario - GitFlow

## Descripción del proyecto

El presente proyecto consiste en el desarrollo de un **Sistema Bancario básico en Python**, creado como proyecto de formación para poner en práctica conocimientos de programación, manejo de archivos y control de versiones.

El sistema permite registrar clientes, crear cuentas bancarias y realizar diferentes operaciones como consultar saldo, consignar dinero, retirar dinero y transferir dinero.

Además, se implementaron operaciones **CRUD** para la administración de clientes y cuentas bancarias.

El proyecto fue desarrollado de manera colaborativa por los aprendices **Yimer** y **Samuel**, utilizando Git y GitHub para organizar el trabajo mediante ramas, commits e integración de funcionalidades.

Durante el desarrollo se utilizó una metodología basada en **GitFlow**, trabajando principalmente con las ramas `main`, `develop` y diferentes ramas de funcionalidades (`feature`).

---

# Objetivos

## Objetivo general

Desarrollar un sistema bancario básico en Python que permita gestionar clientes, cuentas bancarias y operaciones financieras, aplicando conceptos de programación y control de versiones mediante Git y GitHub.

## Objetivos específicos

- Registrar clientes dentro del sistema.
- Consultar información de clientes.
- Actualizar información de clientes.
- Eliminar clientes registrados.
- Crear cuentas bancarias.
- Consultar información de cuentas.
- Actualizar información de cuentas.
- Eliminar cuentas.
- Permitir el inicio de sesión de los clientes.
- Realizar consignaciones.
- Realizar retiros.
- Realizar transferencias.
- Consultar saldos.
- Almacenar la información utilizando archivos JSON.
- Aplicar el uso de ramas y commits.
- Trabajar colaborativamente mediante Git y GitHub.
- Integrar las funcionalidades desarrolladas en la rama `develop`.

---

# Tecnologías utilizadas

## Python

Python fue utilizado como lenguaje principal para desarrollar la lógica del sistema.

Durante el desarrollo se utilizaron conceptos como:

- Variables.
- Funciones.
- Condicionales.
- Ciclos.
- Listas.
- Diccionarios.
- Manejo de archivos.
- Validaciones.
- Operaciones matemáticas.
- Módulos.

Los principales módulos utilizados fueron:

```python
import json
import os
```

## JSON

Se utilizaron archivos JSON para almacenar la información del sistema.

Los principales archivos son:

```text
data/usuarios.json
data/cuentas.json
```

### usuarios.json

Almacena información relacionada con los clientes, como:

- Nombre.
- Documento.
- Teléfono.

### cuentas.json

Almacena información relacionada con las cuentas bancarias, como:

- Número de cuenta.
- Documento del titular.
- Nombre del titular.
- Tipo de cuenta.
- Saldo.

## Git

Git fue utilizado para controlar las versiones del proyecto y organizar el trabajo realizado por los dos aprendices.

## GitHub

GitHub fue utilizado como repositorio remoto para almacenar el proyecto y permitir el trabajo colaborativo.

## Visual Studio Code

Visual Studio Code fue utilizado como entorno de desarrollo para escribir, modificar y ejecutar el código Python.

---

# Funcionalidades del sistema

El sistema bancario cuenta con diferentes funcionalidades relacionadas con clientes, cuentas y operaciones financieras.

## 1. Registrar cliente

Permite registrar un nuevo cliente ingresando información como:

- Nombre.
- Documento.
- Teléfono.

La información se almacena en:

```text
data/usuarios.json
```

---

## 2. Buscar cliente

Permite consultar si un cliente se encuentra registrado mediante su número de documento.

El sistema busca la información dentro del archivo `usuarios.json`.

---

## 3. Actualizar cliente

Permite modificar información de un cliente que ya se encuentra registrado.

Se pueden actualizar datos como:

- Nombre.
- Teléfono.

Los cambios son guardados nuevamente en el archivo JSON.

---

## 4. Eliminar cliente

Permite eliminar un cliente registrado utilizando su número de documento.

El sistema identifica al cliente correspondiente y lo elimina de la información almacenada.

---

## 5. Iniciar sesión

Permite que un cliente ingrese al sistema utilizando su número de documento.

Si el documento se encuentra registrado, el sistema muestra un mensaje de bienvenida con el nombre del cliente.

Si no se encuentra, el sistema informa que el cliente no está registrado.

---

## 6. Crear cuenta bancaria

Permite crear una cuenta bancaria para un cliente previamente registrado.

El usuario puede seleccionar entre:

- Cuenta de Ahorros.
- Cuenta Corriente.

El sistema asigna un número de cuenta y establece un saldo inicial.

La información se almacena en:

```text
data/cuentas.json
```

---

## 7. Consultar cuenta

Permite consultar los datos de una cuenta bancaria utilizando el número de cuenta.

Se puede consultar información como:

- Número de cuenta.
- Titular.
- Tipo de cuenta.
- Saldo.

---

## 8. Actualizar cuenta

Permite modificar información correspondiente a una cuenta bancaria existente.

---

## 9. Eliminar cuenta

Permite eliminar una cuenta bancaria registrada en el sistema.

---

## 10. Consignar dinero

Permite agregar dinero al saldo de una cuenta.

El sistema valida que el valor ingresado sea mayor que cero.

---

## 11. Retirar dinero

Permite retirar dinero de una cuenta.

Antes de realizar el retiro se valida que:

- El valor sea mayor que cero.
- Exista saldo suficiente.

Si el saldo no es suficiente, el sistema muestra un mensaje indicando que no se puede realizar la operación.

---

## 12. Transferir dinero

Permite transferir dinero indicando una cuenta de destino y un valor.

El sistema valida que el valor sea válido y que exista saldo suficiente para realizar la operación.

---

## 13. Consultar saldo

Permite consultar el saldo disponible de una cuenta.

---

# CRUD

Una de las partes importantes del proyecto fue la implementación del concepto **CRUD**.

CRUD corresponde a las operaciones:

- **Create:** Crear.
- **Read:** Consultar.
- **Update:** Actualizar.
- **Delete:** Eliminar.

Estas operaciones permiten administrar la información almacenada en el sistema.

## CRUD de clientes

| Operación | Funcionalidad |
|---|---|
| Create | Registrar cliente |
| Read | Buscar cliente |
| Update | Actualizar cliente |
| Delete | Eliminar cliente |

## CRUD de cuentas

| Operación | Funcionalidad |
|---|---|
| Create | Crear cuenta |
| Read | Consultar cuenta |
| Update | Actualizar cuenta |
| Delete | Eliminar cuenta |

La implementación del CRUD permite que la información pueda ser administrada durante todo su ciclo de vida y no solamente registrada.

---

# Estructura del proyecto

La estructura principal del proyecto es:

```text
Sistema-Bancario-GitFlow/
│
├── data/
│   ├── usuarios.json
│   └── cuentas.json
│
├── funciones.py
├── README.md
├── .gitignore
└── .git/
```

## funciones.py

Contiene las funciones y la lógica principal del sistema bancario.

## data/usuarios.json

Contiene la información de los clientes registrados.

## data/cuentas.json

Contiene la información de las cuentas bancarias.

## README.md

Contiene la documentación del proyecto, sus funcionalidades y las instrucciones de ejecución.

## .gitignore

Permite indicar archivos o carpetas que no deben ser incluidos en el repositorio.

Durante el proyecto se utilizó para evitar almacenar archivos generados automáticamente, como los relacionados con `__pycache__`.

---

# Requisitos para ejecutar el proyecto

Para ejecutar el proyecto se necesita:

- Python 3.
- Git.
- Visual Studio Code o un editor de código similar.
- Acceso al repositorio de GitHub.

No es necesario instalar librerías externas, debido a que se utilizan módulos incluidos en Python.

---

# Instalación y ejecución

## 1. Clonar el repositorio

Desde Git Bash se puede clonar el repositorio utilizando:

```bash
git clone URL_DEL_REPOSITORIO
```

Después se ingresa a la carpeta del proyecto:

```bash
cd Sistema-Bancario-GitFlow
```

---

## 2. Consultar las ramas

Para consultar las ramas disponibles:

```bash
git branch -a
```

---

## 3. Cambiar a la rama develop

La rama principal utilizada durante el desarrollo de las funcionalidades fue `develop`.

Para cambiar a ella:

```bash
git checkout develop
```

---

## 4. Actualizar el proyecto

Antes de ejecutar el sistema se recomienda obtener los últimos cambios:

```bash
git pull origin develop
```

---

## 5. Ejecutar el programa

Desde la carpeta principal del proyecto:

```bash
python funciones.py
```

En algunos equipos también se puede utilizar:

```bash
py funciones.py
```

---

# Menú principal

El sistema cuenta con opciones para administrar clientes, cuentas y operaciones bancarias.

El menú desarrollado incluye funcionalidades como:

```text
==============================
     SISTEMA BANCARIO
==============================

1. Registrar cliente
2. Buscar cliente
3. Actualizar cliente
4. Eliminar cliente
5. Crear cuenta
6. Consultar cuenta
7. Actualizar cuenta
8. Eliminar cuenta
9. Consignar dinero
10. Retirar dinero
11. Transferir dinero
12. Consultar saldo
13. Salir
```

El usuario selecciona la opción correspondiente y posteriormente sigue las instrucciones mostradas en pantalla.

---

# Metodología GitFlow

Para el desarrollo del proyecto se utilizó una metodología basada en **GitFlow**.

Se trabajó principalmente con:

```text
main
develop
feature-*
```

## Rama main

La rama `main` representa la rama principal del proyecto y contiene las versiones principales del sistema.

## Rama develop

La rama `develop` fue utilizada como rama de integración de las diferentes funcionalidades desarrolladas.

## Ramas feature

Las ramas `feature` fueron utilizadas para desarrollar funcionalidades específicas de forma independiente.

Después de finalizar cada funcionalidad, los cambios podían ser integrados a `develop`.

Este método permitió organizar mejor el trabajo y reducir los problemas al momento de integrar las modificaciones de los dos aprendices.

---

# Ramas utilizadas

Durante el desarrollo del proyecto se utilizaron las siguientes ramas:

```text
main
develop

feature-registro-clientes
feature-inicio-sesion
feature-creacion-cuentas
feature-consignaciones
feature-consulta-saldo
feature-retiros
feature-transferencias
feature-crud-clientes-cuentas
```

También se encuentran algunas ramas remotas relacionadas con versiones anteriores del desarrollo:

```text
origin/feature-registro-clientes
origin/feature-inicio-sesion
origin/feature-creacion-cuentas
origin/feature-consignaciones
origin/feature-consulta-saldo
origin/feature-retiros
origin/feature-transferencias
origin/feature-crud-clientes-cuentas
origin/main
origin/develop
```

---

# Flujo de trabajo utilizado

El flujo general utilizado durante el desarrollo fue:

```text
Crear rama feature
        ↓
Desarrollar funcionalidad
        ↓
Probar funcionalidad
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
Integrar cambios en develop
```

Este proceso permitió separar las funcionalidades y mantener un historial organizado.

---

# Comandos Git utilizados

## Consultar el estado del proyecto

```bash
git status
```

## Consultar ramas locales

```bash
git branch
```

## Consultar ramas locales y remotas

```bash
git branch -a
```

## Crear una rama

```bash
git checkout -b nombre-de-la-rama
```

## Cambiar de rama

```bash
git checkout nombre-de-la-rama
```

## Obtener información de las ramas remotas

```bash
git fetch origin
```

## Actualizar una rama

```bash
git pull origin develop
```

## Preparar cambios

```bash
git add .
```

## Crear un commit

```bash
git commit -m "Descripción del cambio"
```

## Subir una rama al repositorio remoto

```bash
git push -u origin nombre-de-la-rama
```

## Integrar una rama

```bash
git merge origin/nombre-de-la-rama
```

## Consultar el historial

```bash
git log --all --oneline --graph --decorate
```

## Consultar el historial mostrando autores

```bash
git log --all --format="%h | %an | %s" --graph
```

---

# Manejo de conflictos

Durante el desarrollo se presentaron conflictos al momento de integrar diferentes ramas.

Uno de los principales conflictos ocurrió al integrar:

```text
origin/feature-creacion-cuentas
```

en la rama `develop`.

Los archivos que presentaron conflictos fueron:

```text
data/cuentas.json
funciones.py
```

El conflicto se produjo porque diferentes ramas habían realizado cambios sobre los mismos archivos.

Para solucionar el conflicto se revisaron los cambios y se conservaron las funcionalidades necesarias del proyecto.

En `data/cuentas.json` se seleccionó la información correcta de las cuentas existentes.

En `funciones.py` se integraron las funcionalidades de:

- Registro de clientes.
- Inicio de sesión.
- Creación de cuentas.
- Consulta de saldo.
- Consignaciones.
- Transferencias.
- Retiros.
- CRUD.

Después de resolver los conflictos se utilizaron comandos como:

```bash
git add .
```

y:

```bash
git commit -m "Se resolvió el conflicto de feature-creacion-cuentas"
```

Finalmente se actualizaron los cambios en el repositorio remoto.

Este proceso permitió practicar el manejo de conflictos de Git y comprender cómo combinar el trabajo realizado en diferentes ramas.

---

# Historial de ramas y commits

El historial del repositorio se consultó mediante:

```bash
git log --all --format="%h | %an | %s" --graph
```

Este comando permitió visualizar los commits, autores y la relación entre las diferentes ramas.

El historial demuestra la participación de los dos aprendices durante el desarrollo.

---

# Participación de Yimer

De acuerdo con el historial de Git, Yimer participó en diferentes etapas del desarrollo.

Entre sus principales commits se encuentran:

```text
073475f | Yimer | Se creó la estructura inicial del sistema bancario

0520b28 | Yimer | Se eliminó la carpeta __pycache__ del repositorio

bf70ac3 | Yimer | Se eliminó la carpeta __pycache__ del repositorio

001c61f | Yimer | Se agregó la funcionalidad de consignaciones

7481955 | Yimer | Registro de clientes guarda datos en JSON

2fcf45a | Yimer | Se integró la rama feature-retiros en develop

4aef0eb | Yimer | Se implementó la funcionalidad de inicio de sesión

37d0a83 | Yimer | Se integró la rama feature-creacion-cuentas en develop

cdfaab6 | Yimer | Se resolvió el conflicto de feature-creacion-cuentas
```

Entre las actividades realizadas por Yimer se encuentran:

- Creación de la estructura inicial del sistema.
- Registro de clientes.
- Almacenamiento de información en JSON.
- Funcionalidad de consignaciones.
- Funcionalidad de inicio de sesión.
- Integración de la funcionalidad de retiros.
- Integración de la creación de cuentas.
- Resolución de conflictos.
- Mantenimiento y organización del repositorio.

---

# Participación de Samuel

De acuerdo con el historial de Git, Samuel también participó en diferentes etapas del desarrollo.

Entre sus principales commits se encuentran:

```text
90dff6b | Samuel | Se agregó la consulta de saldo

48f3a6c | Samuel | Se agregó la funcionalidad de transferencias

20b7f22 | Samuel | Se agregó la funcionalidad de retiros

1827513 | Samuel | Se implementó la creación de cuentas bancarias

8a77ae9 | Samuel | Se agregó la opción crear cuenta bancaria al menú

f238b96 | Samuel | Se agregó CRUD de clientes y cuentas
```

Entre las actividades realizadas por Samuel se encuentran:

- Consulta de saldo.
- Transferencias.
- Retiros.
- Creación de cuentas bancarias.
- Integración de la opción de creación de cuentas al menú.
- Implementación del CRUD de clientes y cuentas.

---

# Evidencia de trabajo colaborativo

El historial de Git demuestra que el proyecto fue desarrollado de manera colaborativa.

Los commits muestran la participación de:

```text
Yimer
Samuel
```

Además, el uso de ramas independientes permitió dividir el trabajo y posteriormente integrar las funcionalidades en `develop`.

Algunas de las funcionalidades desarrolladas fueron:

```text
Registro de clientes
Inicio de sesión
Creación de cuentas
Consulta de saldo
Consignaciones
Retiros
Transferencias
CRUD de clientes
CRUD de cuentas
```

La existencia de diferentes ramas `feature` permite demostrar que el desarrollo se realizó por funcionalidades y que posteriormente fueron integradas al proyecto.

---

# Integración final

Después de desarrollar las diferentes funcionalidades, los cambios fueron integrados en `develop`.

Uno de los ejemplos fue la integración de:

```text
feature-retiros
        ↓
develop
```

También se integró:

```text
feature-creacion-cuentas
        ↓
develop
```

Posteriormente se agregó:

```text
feature-crud-clientes-cuentas
        ↓
develop
```

De esta manera se fue construyendo progresivamente la versión integrada del sistema.

---

# Aprendizajes obtenidos

Durante el desarrollo del proyecto se fortalecieron diferentes conocimientos relacionados con programación y herramientas de desarrollo.

Entre los principales aprendizajes se encuentran:

- Uso de funciones en Python.
- Uso de condicionales.
- Uso de ciclos.
- Manejo de listas y diccionarios.
- Lectura y escritura de archivos JSON.
- Validación de datos.
- Implementación de operaciones CRUD.
- Manejo de ramas en Git.
- Creación de commits.
- Uso de repositorios remotos.
- Integración de ramas.
- Resolución de conflictos.
- Trabajo colaborativo mediante GitHub.
- Organización del código por funcionalidades.

---

# Posibles mejoras futuras

El sistema puede continuar ampliándose en futuras versiones.

Algunas posibles mejoras son:

- Implementar una base de datos real como MySQL o PostgreSQL.
- Crear una interfaz gráfica.
- Implementar usuarios y contraseñas para el inicio de sesión.
- Agregar mayor seguridad a la información.
- Mejorar las validaciones de datos.
- Implementar un sistema de autenticación más completo.
- Agregar historial de movimientos.
- Permitir consultar movimientos de cada cuenta.
- Implementar diferentes permisos según el tipo de usuario.
- Agregar comprobantes de las operaciones bancarias.

---

# Conclusión

El desarrollo del Sistema Bancario permitió aplicar conocimientos de programación y control de versiones mediante un proyecto práctico.

Durante la construcción del sistema se implementaron funcionalidades para registrar y administrar clientes, crear y administrar cuentas bancarias y realizar diferentes operaciones financieras.

La implementación del CRUD permitió comprender el ciclo básico de administración de información mediante las operaciones de crear, consultar, actualizar y eliminar.

El uso de archivos JSON permitió almacenar los datos de clientes y cuentas de una manera sencilla y adecuada para el alcance inicial del proyecto.

Por otra parte, el uso de Git y GitHub permitió desarrollar el proyecto de manera colaborativa utilizando ramas independientes para las diferentes funcionalidades.

La metodología basada en GitFlow permitió trabajar principalmente con las ramas `main`, `develop` y diferentes ramas `feature`, facilitando la organización del proyecto y la integración de los cambios.

El historial de commits demuestra la participación de los aprendices **Yimer y Samuel**, evidenciando los aportes realizados por cada uno durante las diferentes etapas del desarrollo.

Finalmente, el proyecto permitió fortalecer conocimientos de Python, JSON, Git, GitHub, trabajo colaborativo, manejo de ramas, commits, integración de funcionalidades y resolución de conflictos.

---

# Autores

**Yimer**

Participación en:

- Estructura inicial.
- Registro de clientes.
- Almacenamiento JSON.
- Inicio de sesión.
- Consignaciones.
- Integración de funcionalidades.
- Resolución de conflictos.
- Organización del repositorio.

**Samuel**

Participación en:

- Creación de cuentas bancarias.
- Consulta de saldo.
- Retiros.
- Transferencias.
- CRUD de clientes.
- CRUD de cuentas.
- Integración de funcionalidades.

---

# Estado del proyecto

**Proyecto académico desarrollado durante la formación del SENA.**

El sistema se encuentra en desarrollo y puede continuar ampliándose con nuevas funcionalidades y mejoras en futuras versiones.