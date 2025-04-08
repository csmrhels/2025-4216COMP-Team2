import pandas as pd
import matplotlib.pyplot as plt

file_path = r"climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path, encoding="latin1")


df_global = df.groupby("Year").agg({
    "Avg Temperature (°C)": "mean",
    "Forest Area (%)": "mean"
}).reset_index()
fig, ax1 = plt.subplots(figsize=(15, 10))

ax1.plot(df_global["Year"], df_global["Avg Temperature (°C)"], color="tab:red", marker="o", label="Avg Temperature (°C)")
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temperature (°C))", color="tab:red")
ax1.tick_params(axis="y", labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.plot(df_global["Year"], df_global["Forest Area (%)"], color="tab:green", marker="s", linestyle="solid", label="Forest Area (%)")
ax2.set_ylabel("Forest Area (%)", color="tab:green")
ax2.tick_params(axis="y", labelcolor="tab:green")

plt.title("Does an increase in temperature correlate with the increase of % of forest area?")
fig.tight_layout()
plt.grid()

plt.show()





