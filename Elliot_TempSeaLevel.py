#Question: What is the correlation between a countries temperatutre and its sea level rise?

import csv
import matplotlib.pyplot as plt
import pandas as pd


#---Load CSV File into the code---
path = "climate_change_dataset_rounded.csv"
df = pd.read_csv(path)

#Find the correlation of the sea level compared to temperature and store it in a variable
correlation = df["Avg Temperature (°C)"].corr(df["Sea Level Rise (mm)"])


#---Create scatter diagram---
plt.figure(figsize=(10, 6))

#Plot data on the graph
plt.scatter(df["Avg Temperature (°C)"], df["Sea Level Rise (mm)"], alpha=0.6, color='blue')

plt.xlabel("Average Temperature (°C)")
plt.ylabel("Sea Level Rise (mm)")
plt.title(f"Correlation between a countries temperatutre and its sea level rise. \nCorrelation: {correlation:.2f}")
plt.grid(True)
plt.show()
