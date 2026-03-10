import my_module_operaciones as operations
import os

resultado1 = operations.sum(5, 3)
resultado2 = operations.product(4, 6)

os.system('clear' if os.name != 'nt' else 'cls')

print("\n"*2)
print("-"*20)
print("Suma:", resultado1)
print("Multiplicación:", resultado2)
print("-"*20)
print("\n"*2)