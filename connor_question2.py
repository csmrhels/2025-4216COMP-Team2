import matplotlib.pyplot as plt
import pandas as pd
import csv
# Climate Change Data Analysis
with open('climate_change_dataset_rounded.csv','r', encoding="latin1") as f:
    sv_reader=csv.reader(f)
    header_row = next(sv_reader)
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
#making the data more readable
data['Country'] = data['Country'].astype('category')
data['Year'] = data['Year'].astype('int16')
data['Avg Temperature (°C)'] = data['Avg Temperature (°C)'].astype('float32')
data['Sea Level Rise (mm)'] = data['Sea Level Rise (mm)'].astype('float32')
data['Rainfall (mm)'] = data['Rainfall (mm)'].astype('float32')
data['Population'] = data['Population'].astype('int32')
data['Renewable Energy (%)'] = data['Renewable Energy (%)'].astype('float32')
data['Forest Area (%)'] = data['Forest Area (%)'].astype('float32')
#The hottest year in the world
hottest_year = data.loc[data['Avg Temperature (°C)'].idxmax()]
print(f"The hottest year in the world is {hottest_year['Year']} with an average temperature of {hottest_year['Avg Temperature (°C)']}°C.")
#The coldest year in the world
coldest_year = data.loc[data['Avg Temperature (°C)'].idxmin()]
print(f"The coldest year in the world is {coldest_year['Year']} with an average temperature of {coldest_year['Avg Temperature (°C)']}°C.")
#Comparing the average temperature of the hottest and coldest year
plt.figure(figsize=(10, 6))
plt.bar(['Hottest Year', 'Coldest Year'], [hottest_year['Avg Temperature (°C)'], coldest_year['Avg Temperature (°C)']], color=['red', 'blue'])
plt.title('Average Temperature Comparison')
plt.xlabel('Year')
plt.ylabel('Avg Temperature (°C)')
plt.grid()
plt.tight_layout()
plt.savefig('avg_temp_comparison.png')
plt.show()