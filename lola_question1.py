import pandas as pd
import matplotlib.pyplot as plt

file_path = r"climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path)

df_global = df.groupby("Year").agg({
    "Sea Level Rise (mm)": "mean",
    "Rainfall (mm)": "mean"
}).reset_index()
fig, ax1 = plt.subplots(figsize=(15, 10))

ax1.plot(df_global["Year"], df_global["Sea Level Rise (mm)"], color="tab:blue", marker="o", label="Sea Level Rise(mm) ")
ax1.set_xlabel("Year")
ax1.set_ylabel("Sea Level Rise(mm))", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.plot(df_global["Year"], df_global["Rainfall (mm)"], color="tab:green", marker="s", linestyle="solid", label="Average Rainfall(mm)")
ax2.set_ylabel("Average Sea Level(mm)", color="tab:green")
ax2.tick_params(axis="y", labelcolor="tab:green")

plt.title("The correlation between the sea level and rainfall over the years")
fig.tight_layout()
plt.grid()

plt.show()
