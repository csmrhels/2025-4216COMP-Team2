import pandas as pd
import matplotlib.pyplot as plt

file_path = "climate_change_dataset_rounded.csv" 
df = pd.read_csv(file_path, encoding="latin1")

#group data by year and calculate averages for temp and sea level
yearly_avg = df.groupby("Year")[["Avg Temperature (°C)", "Sea Level Rise (mm)"]].mean().reset_index()

#creates line plot
fig, ax1 = plt.subplots(figsize=(10, 6))

#plots avg temp
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temperature (°C)", color="tab:blue")
ax1.plot(yearly_avg["Year"], yearly_avg["Avg Temperature (°C)"], color="tab:blue", label="Avg Temperature")
ax1.tick_params(axis='y', labelcolor="tab:blue")

#creates second y-acis and plots sea level rise
ax2 = ax1.twinx()
ax2.set_ylabel("Sea Level Rise (mm)", color="tab:green")
ax2.plot(yearly_avg["Year"], yearly_avg["Sea Level Rise (mm)"], color="tab:green", label="Sea Level Rise")
ax2.tick_params(axis='y', labelcolor="tab:green")

#creates graph title and uses grid for readability
plt.title("Average Temperature and Sea Level Rise Over Time")
fig.tight_layout()
plt.grid()
plt.show()