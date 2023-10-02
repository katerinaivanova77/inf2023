import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris_data = pd.read_csv("iris_data.csv")

species_counts = iris_data["Species"].value_counts()
plt.figure(figsize=(10, 10))
plt.pie(species_counts, labels=species_counts.index)
plt.title("Виды ирисов в датасете")
plt.show()

plc = pd.cut(iris_data["PetalLengthCm"], bins=[0, 1.2, 1.5, np.inf], labels=["<= 1.2", "> 1.2 and <= 1.5", "> 1.5"])
plc = plc.value_counts()
plt.figure(figsize=(10, 10))
plt.pie(plc, labels=plc.index)
plt.title("По длине лепестка")
plt.show()


