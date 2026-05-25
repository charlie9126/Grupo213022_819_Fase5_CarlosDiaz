# Grupo213022_819_Fase5_CarlosDiaz
Fase 5 Fundamentos de programacion Unad
# Fase 5 - Evaluación Final POA

## Curso
Fundamentos de Programación  
Código: 213022

## Estudiante
Carlos Diaz

## Problema Seleccionado
Problema 1 - Clasificación de compromiso de sesiones de clientes.

## Descripción
El programa desarrollado en Python permite analizar sesiones de clientes almacenadas en una matriz con la siguiente estructura:

- ID del cliente
- Duración de la sesión en segundos
- Cantidad de clics realizados

A partir de estos datos, el sistema clasifica el nivel de compromiso de cada sesión en:

- Alto
- Medio
- Bajo

## Lógica de Clasificación

- Alto:
  - Duración mayor a 180 segundos
  - y clics mayores a 8

- Bajo:
  - Duración menor a 60 segundos
  - o clics menores a 3

- Medio:
  - Todos los demás casos

## Tecnologías Utilizadas

- Python 3

## Estructuras Utilizadas

- Matrices (listas de listas)
- Funciones
- Condicionales (`if`, `elif`, `else`)
- Ciclos `for`

## Archivo Principal

```bash
problema1.py
