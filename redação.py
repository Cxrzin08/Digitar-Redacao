import keyboard
import time

print("Aguarde 5 segundos e clique no campo onde deseja digitar...")
time.sleep(5)

#cole seu texto na linha que esta vazia entre as aspas
texto = """

"""

for char in texto:
    keyboard.write(char)
    time.sleep(0.05)

print("Texto digitado com sucesso!")
