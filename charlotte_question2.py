import matplotlib.pyplot as plt
import pandas as pd
             
file_path = r"climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Group the data by 'Country' and calculate the mean of the 'Avg Temperature (°C)' for each country
meanTempPerCountry = df.groupby("Country")[["Avg Temperature (°C)"]].mean().reset_index()

# Sort the countries by their average temperature in ascending order
meanTempPerCountry= meanTempPerCountry.sort_values(by="Avg Temperature (°C)", ascending=True)

# Create the plot and define size of plot
plt.figure(figsize=(12, 6))
 
# Create a horizontal bar plot showing the average temperature by country
plt.barh(meanTempPerCountry["Country"], meanTempPerCountry["Avg Temperature (°C)"], color="red")

#Label axis
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Country")

#Add tiltle
plt.title("Average Temperature by Country")

#Add gridlines
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
