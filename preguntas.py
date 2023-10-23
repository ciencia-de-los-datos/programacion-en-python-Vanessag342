"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import defaultdict
data_csv = open('data.csv', 'r')
csv_reader = csv.reader(data_csv, delimiter='\t')
data = list(csv_reader)

def pregunta_01():
    suma = 0
    for row in data:
        suma += int(row[1])
    return suma


def pregunta_02():
    contador_letras = defaultdict(int)
    for row in data:
        letra = row[0]
        contador_letras[letra] += 1
    return sorted(contador_letras.items())


def pregunta_03():
    suma_letras = defaultdict(int)
    for row in data:
        letra = row[0]
        valor = int(row[1])
        suma_letras[letra] += valor
    return sorted(suma_letras.items())


def pregunta_04():
    meses = defaultdict(int)
    for row in data:
        fecha = row[2]
        mes = fecha.split('-')[1]
        meses[mes] += 1
    return sorted(meses.items())


def pregunta_05():
    maximos_minimos = defaultdict(lambda: [float('inf'), float('-inf')])
    for row in data:
        letra = row[0]
        valor = int(row[1])
        maximos_minimos[letra][0] = min(maximos_minimos[letra][0], valor)
        maximos_minimos[letra][1] = max(maximos_minimos[letra][1], valor)
    return sorted([(letra, min_max[1], min_max[0]) for letra, min_max in maximos_minimos.items()])


import re

def pregunta_06():
    diccionario_valores = defaultdict(lambda: [float('inf'), float('-inf')])
    for row in data:
        claves_valores = re.findall(r'([a-z]+):(\d+)', row[4])
        for clave, valor_str in claves_valores:
            valor = int(valor_str)
            diccionario_valores[clave][0] = min(diccionario_valores[clave][0], valor)
            diccionario_valores[clave][1] = max(diccionario_valores[clave][1], valor)
    return sorted([(clave, min_max[0], min_max[1]) for clave, min_max in diccionario_valores.items()])


def pregunta_07():
    letras_valores = defaultdict(list)
    for row in data:
        valor = int(row[1])
        letra = row[0]
        letras_valores[valor].append(letra)
    return sorted([(valor, sorted(letras)) for valor, letras in letras_valores.items()])


def pregunta_08():
    valores_letras = defaultdict(set)
    for row in data:
        valor = int(row[1])
        letra = row[0]
        valores_letras[valor].add(letra)
    return sorted([(valor, sorted(letras)) for valor, letras in valores_letras.items()])


def pregunta_09():
    contador_claves = defaultdict(int)
    for row in data:
        claves_valores = row[4].split(',')
        for clave_valor in claves_valores:
            clave = clave_valor.split(':')[0]
            contador_claves[clave] += 1
    return dict(sorted(contador_claves.items()))


def pregunta_10():
    resultado = []
    for row in data:
        letra = row[0]
        columna_4 = len(row[3].split(','))
        columna_5 = len(row[4].split(','))
        resultado.append((letra, columna_4, columna_5))
    return resultado


def pregunta_11():
    suma_letras = defaultdict(int)
    for row in data:
        columna_2 = int(row[1])
        letras_columna_4 = row[3].split(',')
        for letra in letras_columna_4:
            suma_letras[letra] += columna_2
    return dict(sorted(suma_letras.items()))


def pregunta_12():
    suma_por_letra = defaultdict(int)
    for row in data:
        letra = row[0]
        claves_valores = row[4].split(',')
        for clave_valor in claves_valores:
            clave, valor = clave_valor.split(':')
            suma_por_letra[letra] += int(valor)
    return dict(sorted(suma_por_letra.items()))
