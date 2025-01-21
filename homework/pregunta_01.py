"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt") as file:
        lines = file.readlines()
    filtered_lines = [line.strip() for line in lines if "---" not in line]
    headers = re.split(r"\s{2,}", filtered_lines[0])
    headers[1] += " palabras clave"
    headers[2] += " palabras clave"
    records = []
    current_record = headers
    for line in filtered_lines[2:]:
        split_line = re.split(r"\s{2,}", line)
        if len(line) == 0: continue
        if split_line[0].isdigit(): 
            records.append(current_record)
            current_record = []
            current_record.append(int(split_line[0]))
            current_record.append(int(split_line[1]))
            current_record.append(float(split_line[2].split()[0].replace(',', '.')))
            percentage_index = line.find("%")
            normalized_keywords = re.sub(r'\s+', ' ', line[percentage_index + 1:].strip())
            current_record.append(normalized_keywords)
        else: 
            clean_keywords = re.sub(r'\s+', ' ', line.strip()).replace(".", "")
            current_record[-1] += " " + clean_keywords.strip()
    records.append(current_record) 
    records[0] = [header.lower().replace(" ", "_") for header in records[0]]
    dataframe = pd.DataFrame(data=records[1:], columns=records[0])
    return dataframe


pregunta_01()