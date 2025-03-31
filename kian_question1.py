import pandas as pd
import matplotlib.pyplot as plt
import csv

with open('climate_change_dataset_rounded.csv','r') as f:
    csv_reader=csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

data = pd.read_csv("climate_change_dataset_rounded.csv", dtype= {
    "Country": "category",
    "Year": "int16",
    "Avg Temperature (°C)": "float32",
    "CO2_Emissions": "float32",
    "Sea Level Rise (mm)": "float32",
    "Rainfall (mm)": "float32",
    "Population": "int32",
    "Renewable Energy (%)": "float32",
    "Extreme Weather Event": "int8",
    "Forest Area (%)": "float32",
})

#sorting data into country/year to find each instance of renewable energy percentage from the group
data_sorted = data.sort_values(by=['Country','Year'])

#finding the minimum/maximum renewable energy percentage to compare to other countries
first_last = data_sorted.groupby('Country').agg(
    First_Year=('Year', 'min'),
    Last_Year=('Year', 'max'),
    First_Renewable_Energy=('Renewable Energy (%)', 'first'),
    Last_Renewable_Energy=('Renewable Energy (%)', 'last')
)

#calculation to find the difference in increase
first_last['Renewable Energy Increase'] = first_last['Last_Renewable_Energy'] - first_last['First_Renewable_Energy']

max_increase_country = first_last['Renewable Energy Increase'].idxmax()
print("Country with the biggest increase in renewable energy:")
print(first_last.loc[max_increase_country])

country_data = data_sorted[data_sorted['Country'] == max_increase_country].sort_values(by='Year')

plt.figure(figsize=(12,8))

plt.plot(country_data['Year'], country_data['Renewable Energy (%)'], marker='o', linestyle='-', color='b', linewidth=2)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Renewable Energy (%)', fontsize=12)
plt.title(f'Renewable Energy (%) in {max_increase_country} Over Time', fontsize=14)

#creating a grid for more clarity
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()