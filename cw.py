import matplotlib.pyplot as plt
import pandas as pd

file_path = r"M:4216-cw\climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path)


canada_data = df[df["Country"] == "Canada"]

fig, ax1 = plt.subplots(figsize=(10, 5))
plt.plot(canada_data["Year"], canada_data["Avg Temperature (°C)"], marker="o", linestyle="-", color="b", label="Avg Temperature")

plt.ylabel("Avg Temperature (°C)")
plt.xlabel("Year")
plt.title("Is there any anomolies in Canada's Average Temperature Over the Years")
plt.grid(True)
plt.show()