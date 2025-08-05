"""
Analisi dei dati su Star Wars - Dataquest Inspired

Autore: [Il tuo nome]
Descrizione: Analisi esplorativa dei risultati di un sondaggio sulla saga di Star Wars.

"""

import pandas as pd
import numpy as np
import os

# Caricamento del dataset
if os.path.exists("star_wars.csv"):
    star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
else:
    raise FileNotFoundError("Il file 'star_wars.csv' non è stato trovato.")

# Visualizzazione delle prime righe
print(star_wars.head())

# Pulizia iniziale delle colonne boolean
yes_no = {"Yes": True, "No": False}
for col in [
    "Have you seen any of the 6 films in the Star Wars franchise?",
    "Do you consider yourself to be a fan of the Star Wars film franchise?"
]:
    star_wars[col] = star_wars[col].map(yes_no)

# Mappatura dei film visti
movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    np.nan: False
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)

# Output per verifica
print(star_wars.head())
