import matplotlib.pyplot as plt
import pandas as pd
import csv
# Climate Change Data Analysis
with open('climate_change_dataset_rounded.csv','r') as f:
    sv_reader=csv.reader(f)
    header_row = next(sv_reader)
    print(header_row)
    data = pd.read_csv("climate_change_dataset_rounded.csv", dtype= {
    "Country": "category",
    "Year": "int16",
    "Avg Temperature (C)": "float32",
    "CO2_Emissions": "float32",
    "Sea Level Rise (mm)": "float32",
    "Rainfall (mm)": "float32",
    "Population": "int32",
    "Renewable Energy (%)": "float32",
    "Extreme Weather Event": "int8",
    "Forest Area (%)": "float32",
    })
#Has the world switched to renewable energy from 2013 to 2023?
renewable_energy = data[data['Year'].between(2013, 2023)]
renewable_energy = renewable_energy.groupby('Year')['Renewable Energy (%)'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(renewable_energy['Year'], renewable_energy['Renewable Energy (%)'], marker='o')
plt.title('Global Renewable Energy Adoption (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Renewable Energy (%)')
plt.grid()
plt.xticks(renewable_energy['Year'], rotation=45)
plt.tight_layout()
plt.savefig('renewable_energy_adoption.png')
plt.show()
