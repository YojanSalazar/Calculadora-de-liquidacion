# Calculadora-de-liquidaci-n-


## Colaboradores
- Sebastian Aristizabal Aristizabal

- Cesar Luis Velasquez Botero

---

## Descripción

Este proyecto implementa un sistema en Python para calcular la **liquidación laboral** de un empleado en Colombia.

Permite calcular:

* Cesantías
* Intereses sobre cesantías
* Prima de servicios
* Vacaciones
* Pago total (liquidación)

El sistema se compone de:

* Un módulo de lógica (`logicaLiquidacion.py`)
* Pruebas automatizadas (`test_pruebasCalculos.py`)
* Una interfaz por consola (`interfazLiquidacion.py`)

La aplicación valida datos de entrada como:

* Salario (debe ser numérico y mayor a 0)
* Fechas (formato correcto y coherencia entre ingreso/retiro)

---

## Ejecución

- Prerrequisitos: Clonar el repositorio en un ambiente establecido
- Ejecución:
    -  Ubicados en la carpeta raiz del proyecto, ejecute:
    -  ```py src/view/interfazLiquidacion.py``` 

### 3. Ejecutar pruebas

Desde la raíz del proyecto, ejecuta:

``py test/test_pruebasCalculos.py``

---

## Arquitectura

El proyecto está dividido en tres componentes principales:

---

### 1. Lógica (`logicaLiquidacion.py`)

Contiene todos los cálculos:

* `validar_salario`
* `calcular_tiempo_trabajado_dias`
* `calcular_cesantias`
* `calcular_interes_cesantias`
* `calcular_vacaciones`
* `calcular_prima_servicios`
* `calcular_pago_neto`

También define excepciones personalizadas:

* `ErrorSalario`
* `ErrorFecha`

---

### 2. Interfaz (`interfazLiquidacion.py`)

Permite interacción por consola con el usuario:

Funciones:

* `ingreso_fechas()`

  * Solicita fechas y calcula días trabajados

* `ingreso_salario()`

  * Solicita salario y lo valida

Incluye un ciclo `while` que mantiene el programa en ejecución.

---

### 3. Pruebas (`test_pruebasCalculos.py`)

Incluye pruebas con `unittest` para:

* Cálculos correctos
* Casos límite
* Manejo de errores
* Validación de datos

## Estructura

```
project/
│
├── src/
│   └── model/
│   │   └── logicaLiquidacion.py
│   │
│   └── view/
│       └── interfazLiquidacion.py
│
├── test/
│   └── test_pruebasCalculos.py
│
└── README.md

```

---
