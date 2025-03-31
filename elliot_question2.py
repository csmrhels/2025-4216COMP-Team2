#Question: Does an increase in rainfall have an effect on sea levels rising in the USA?
import pandas as pd
import matplotlib.pyplot as plt

#Read data
file_path = "climate_change_dataset_rounded.csv"
df = pd.read_csv(file_path)

#Define columns
country_col = 'Country'  
year_col = 'Year'  
rainfall_col = 'Rainfall (mm)'  
sea_level_col = 'Sea Level Rise (mm)'  

#Filter USA data
df_usa = df[df[country_col] == "USA"]

# Group by year, calculate average rainfall and sea level rise
df_usa_avgRain = df_usa.groupby(year_col)[[rainfall_col]].mean().reset_index()
df_usa_avgSea = df_usa.groupby(year_col)[[sea_level_col]].mean().reset_index()

#Define 3 seperate plots
fig, axes = plt.subplots(1, 3, figsize=(20, 5))

#Rainfall plot
axes[0].plot(df_usa_avgRain[year_col], df_usa_avgRain[rainfall_col], marker='o', linestyle='-', color='blue')
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Avg Rainfall (mm)")
axes[0].set_title("Average Rainfall in the USA Over Time")
axes[0].grid(True)

#Sea level plot
axes[1].plot(df_usa_avgRain[year_col], df_usa_avgSea[sea_level_col], marker='s', linestyle='--', color='red')
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Avg Sea Level Rise (mm)")
axes[1].set_title("Average Sea Level Rise in the USA Over Time")
axes[1].grid(True)

#Combined plot... Rainfall y-axis
axes[2].plot(df_usa_avgRain[year_col], df_usa_avgRain[rainfall_col], marker='o', linestyle='-', color='blue', label="Avg Rainfall (mm)")
axes[2].set_xlabel("Year")
axes[2].set_ylabel("Avg Rainfall (mm)", color='blue')
axes[2].set_title("Rainfall vs Sea Level Rise Trend in the USA")
axes[2].tick_params(axis='y', labelcolor='blue')

#Sea Level Rise y-axis into combined plot
axes3 = axes[2].twinx()
axes3.plot(df_usa_avgRain[year_col], df_usa_avgSea[sea_level_col], marker='s', linestyle='--', color='red', label="Avg Sea Level Rise (mm)")
axes3.set_ylabel("Avg Sea Level Rise (mm)", color='red')
axes3.tick_params(axis='y', labelcolor='red')


plt.title("Rainfall vs Sea Level Rise Trend in the USA")
fig.tight_layout()
plt.show()
