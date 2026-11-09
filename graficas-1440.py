
# importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# marco morquecho NC 1440

# listas de cryptos
btc = ['Bitcoin', 'BTC', True, 2009]
eth = ['Ethereum', 'ETH', True, 2015]
sol = ['Solana', 'SOL', True, 2020]
ada = ['Cardano', 'ADA', True, 2017]
xrp = ['Ripple', 'XRP', False, 2012]

# crear tabla
lista_cryptos = [btc, eth, sol, ada, xrp]

df_cryptos = pd.DataFrame(lista_cryptos,
columns=["Nombre", "Simbolo", "Codigo_Abierto", "Año"])

print(df_cryptos)

# GRAFICA 1: LINEAS
plt.plot(df_cryptos["Nombre"], df_cryptos["Año"],
         marker="o", color="blue")
plt.title("Cryptos 1440")
plt.xlabel("Criptomonedas")
plt.ylabel("Año de creacion")
plt.show()

# GRAFICA 2: PUNTOS
plt.scatter(df_cryptos["Nombre"], df_cryptos["Año"],
            color="red", marker="o")
plt.title("Puntos Cryptos 1440")
plt.xlabel("Criptomonedas")
plt.ylabel("Año de creacion")
plt.show()

# GRAFICA 3: BARRAS
plt.bar(df_cryptos["Nombre"], df_cryptos["Año"] - 2000)
plt.title("Año de creacion Cryptos 1440")
plt.xlabel("Criptomonedas")
plt.ylabel("Años desde 2000")
plt.show()

# GRAFICA 4: BARRAS ORDENADAS
df_ordenar = df_cryptos.sort_values("Año", ascending=False)

plt.barh(df_ordenar["Nombre"], df_ordenar["Año"] - 2000,
         color="green")
plt.title("Cryptos ordenadas 1440")
plt.xlabel("Años desde 2000")
plt.ylabel("Criptomonedas")
plt.show()

# GRAFICA 5: CODIGO ABIERTO
plt.bar(df_cryptos["Nombre"],
        df_cryptos["Codigo_Abierto"].astype(int),
        color=["green", "green", "green", "green", "red"])
plt.title("Codigo abierto Cryptos 1440")
plt.xlabel("Criptomonedas")
plt.ylabel("Codigo abierto")
plt.yticks([0, 1], ["No", "Si"])
plt.show()


# Grafica de pastel

plt.pie(df_cryptos["Año"],
        labels=df_cryptos["Nombre"],
        autopct="%1.1f%%")

plt.title("Cryptos 1440")
plt.show()

