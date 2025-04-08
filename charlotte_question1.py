import matplotlib.pyplot as plt
import pandas as pd

file_path = r"climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Filter the dataset to get only the rows where the country is Canada
canada_data = df[df["Country"] == "Canada"]

# Create a new figure and axis for plotting
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot the average temperature in Canada over the years
plt.plot(canada_data["Year"], canada_data["Avg Temperature (C)"], marker="o", linestyle="-", color="b", label="Avg Temperature")

# Label axis
plt.ylabel("Avg Temperature (°C)")
plt.xlabel("Year")

# Add title
plt.title("Is there any anomolies in Canada's Average Temperature Over the Years")

# Add Gridlines
plt.grid(True)

# Show the plot
plt.show()