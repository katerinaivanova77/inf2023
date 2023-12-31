import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris_data = pd.read_csv("iris_data.csv")

species_counts = iris_data["Species"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(species_counts, labels=species_counts.index, autopct="%1.1f%%")
plt.title("Доля видов ирисов в датасете")
plt.show()

petal_length_bins = pd.cut(iris_data["PetalLengthCm"], bins=[0, 1.2, 1.5, np.inf], labels=["<= 1.2", "> 1.2 and <= 1.5", "> 1.5"])
petal_length_counts = petal_length_bins.value_counts()
plt.figure(figsize=(6, 6))
plt.pie(petal_length_counts, labels=petal_length_counts.index, autopct="%1.1f%%")
plt.title("Доли ирисов по длине лепестка")
plt.show()