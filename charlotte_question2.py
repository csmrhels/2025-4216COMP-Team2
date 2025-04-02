import matplotlib.pyplot as plt
import pandas as pd
             
file_path = r"climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path, encoding="latin1")

meanTempPerCountry = df.groupby("Country")["Avg Temperature (Â°C)"].mean().reset_index()

meanTempPerCountry= meanTempPerCountry.sort_values(by="Avg Temperature (Â°C)", ascending=True)

plt.figure(figsize=(12, 6))
plt.barh(meanTempPerCountry["Country"], meanTempPerCountry["Avg Temperature (Â°C)"], color="red")
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Country")
plt.title("Average Temperature by Country")
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
