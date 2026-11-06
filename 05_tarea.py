#sobre casas. csv, pedir presupusto y el programa te ha de mostrar las opciones disponbles

import pandas as pd

# Leer archivo CSV
df = pd.read_csv("casas.csv")

# Solicitar presupuesto al usuario
presupuesto = float(input("Introduce tu presupuesto máximo: "))

# Filtrar casas según el presupuesto
casas_disponibles = df[df["price"] <= presupuesto]

# Mostrar resultados
if len(casas_disponibles) > 0:
    print("\nCasas disponibles dentro de tu presupuesto:")
    print(casas_disponibles.to_string(index=False))
    
    print(f"\nNúmero de casas disponibles: {len(casas_disponibles)}")
else:
    print("\nNo hay casas disponibles para ese presupuesto.")
