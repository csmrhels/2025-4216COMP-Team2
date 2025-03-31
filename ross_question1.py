import matplotlib.pyplot as plt
import pandas as pd


file_path = "climate_change_dataset_rounded.csv" 
df = pd.read_csv(file_path, encoding="latin1")

#groups data by year and calculates average for temp and co2
df_global = df.groupby("Year").agg({
    "Avg Temperature (°C)": "mean",
    "CO2 Emissions (Tons/Capita)": "mean"
}).reset_index()

#creates line plot
fig, ax1 = plt.subplots(figsize=(10, 5))

#creates x and y axis and plots avg temp
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temperature (°C)", color="tab:red")
ax1.plot(df_global["Year"], df_global["Avg Temperature (°C)"], color="tab:red", marker="o", label="Avg Temperature")
ax1.tick_params(axis="y", labelcolor="tab:red")

#creates second y-axis and plots co2
ax2 = ax1.twinx()
ax2.set_ylabel("CO2 Emissions (Tons/Capita)", color="tab:blue")
ax2.plot(df_global["Year"], df_global["CO2 Emissions (Tons/Capita)"], color="tab:blue", marker="s", linestyle="dashed", label="CO2 Emissions")
ax2.tick_params(axis="y", labelcolor="tab:blue")

#creates graph title and layout
plt.title("Correlation Between CO2 Emissions and Temperature Over Time")
fig.tight_layout()
plt.grid()

plt.show()