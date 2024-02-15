import pandas as pd
import json
from datetime import datetime
import os.path


def salarioEdad(salary, age):
    salario = float(salary.replace('$', '').replace(',', ''))
    if age < 30:
        salario = salario * 1.1
    return '{:.2f}€'.format(salario)


fechaActual = datetime.now().strftime('%B-%Y')
nombreArchivo = f"pagos-empleados-{fechaActual}.xlsx"

if os.path.isfile(nombreArchivo):
    print(f"El archivo '{nombreArchivo}' ya existe, borrelo antes de seguir")
else:
    with open('employees.json', 'r') as employees_json:
        employees_data = json.load(employees_json)

    df = pd.DataFrame(employees_data)

    filtro = df[df['proyect'] != 'GRONK'].copy()

    filtro['salary'] = filtro.apply(lambda row: salarioEdad(row['salary'], row['age']), axis=1)

    filtro.to_excel(nombreArchivo, index=True)

    df_from_excel = pd.read_excel(nombreArchivo)
    print(df_from_excel)
