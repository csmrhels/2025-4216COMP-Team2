import pandas as pd 
import matplotlib.pyplot as plt

# loading data from the dataset
data = pd.read_csv("climate_change_dataset_rounded.csv", encoding="latin1")

#picking a specific country to compare data in reliably
country = "USA"
data_country = data[data["Country"] == country]

#sorting the data from the USA by each year
data_country = data_country.sort_values(by="Year")

fig, ax1 = plt.subplots(figsize=(10, 5))

#plotting the average temperature on the primary y axis of the line graph
ax1.set_xlabel("Year")

ax1.set_ylabel("Avg Temperature (°C)", color="red")

ax1.plot(data_country["Year"], data_country["Avg Temperature (°C)"], marker="o", color="red", label="Avg Temp")

ax1.tick_params(axis="y", labelcolor="red")

#plotting the number of extreme weather events on the secondary y axis of the line
ax2 = ax1.twinx()
ax2.set_ylabel("Extreme Weather Events", color="blue")
ax2.plot(data_country["Year"], data_country["Extreme Weather Events"], marker="s", linestyle="--", color="blue", label="Extreme Weather")
ax2.tick_params(axis="y", labelcolor="blue")

#creating a title and a grid behind the data to make it more readable
plt.title(f"Avg Temperature vs Extreme Weather Events ({country})")
ax1.grid(True, linestyle="--", alpha=0.6)

# Show plot
plt.show()

