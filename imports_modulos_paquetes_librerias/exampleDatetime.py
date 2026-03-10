from datetime import datetime
import os

ahora = datetime.now()

os.system('clear' if os.name != 'nt' else 'cls')

print("\n"*2)
print("-"*20)
print("Fecha actual:", ahora)
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("-"*20)
print("\n"*2)