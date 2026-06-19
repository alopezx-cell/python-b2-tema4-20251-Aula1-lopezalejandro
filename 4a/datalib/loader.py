import csv


def load_csv(filepath):
    # leemos el csv y lo convertimos en lista de diccionarios
    lista = []
    with open(filepath, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            lista.append(dict(fila))
    return lista
