import matplotlib.pyplot as plt
import pandas as pd


file_path = "climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path, encoding="latin1")

#calculates the total c02 emissions as data is stored per capita
df["Total CO2 Emissions"] = df["CO2 Emissions (Tons/Capita)"] * df["Population"]

#groups data by year and adds values together
df_total = df.groupby("Year").agg({"Total CO2 Emissions": "sum", "Population": "sum"}).reset_index()

#sets bar chart width and positions
bar_width = 0.4
x = list(range(len(df_total)))

#creates the bar chart
fig, ax1 = plt.subplots(figsize=(12, 6))

#plots total c02 emissions on the chart
ax1.set_xlabel("Year")
ax1.set_ylabel("Total CO2 Emissions", color="tab:red")
ax1.bar([i - bar_width/2 for i in x], df_total["Total CO2 Emissions"],
        width=bar_width, color="tab:red", label="Total CO2 Emissions")
ax1.tick_params(axis="y", labelcolor="tab:red")
ax1.set_xticks(x)
ax1.set_xticklabels(df_total["Year"], rotation=45)

#plots population on y-axis
ax2 = ax1.twinx()
ax2.set_ylabel("Total Population", color="tab:blue")
ax2.bar([i + bar_width/2 for i in x], df_total["Population"],
        width=bar_width, color="tab:blue", label="Total Population")
ax2.tick_params(axis="y", labelcolor="tab:blue")

#creates graph title
plt.title("Relationship Between Population and Total CO2 Emissions Over Time")
plt.grid(axis='y')

plt.show()