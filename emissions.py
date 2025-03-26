import matplotlib.pyplot as plt
import pandas as pd


file_path = r"M:\UniServerZ\www\matplotlib\4216Team2\climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path)

df_global = df.groupby("Year").agg({
    "Avg Temperature (°C)": "mean",
    "CO2 Emissions (Tons/Capita)": "mean"
}).reset_index()

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temperature (°C)", color="tab:red")
ax1.plot(df_global["Year"], df_global["Avg Temperature (°C)"], color="tab:red", marker="o", label="Avg Temperature")
ax1.tick_params(axis="y", labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.set_ylabel("CO2 Emissions (Tons/Capita)", color="tab:blue")
ax2.plot(df_global["Year"], df_global["CO2 Emissions (Tons/Capita)"], color="tab:blue", marker="s", linestyle="dashed", label="CO2 Emissions")
ax2.tick_params(axis="y", labelcolor="tab:blue")

plt.title("Correlation Between CO2 Emissions and Temperature Over Timea")
fig.tight_layout()
plt.grid()

plt.show()