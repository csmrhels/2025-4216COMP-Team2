import matplotlib.pyplot as plt
import pandas as pd
import csv

path = "climate_change_dataset_rounded.csv"
df = pd.read_csv(path)

#Group by the country to work out average for each one and find mean.
averageCo2Cont = df.groupby("Country")["CO2 Emissions (Tons/Capita)"].mean()
print(averageCo2Cont.idxmax())
print(averageCo2Cont.max())

#Plot the results on the table... as there is 15 countries sort highest to lowest from all countires
topCont = averageCo2Cont.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
plt.barh(topCont.index, topCont.values, color='blue')
plt.xlabel("Average CO2 Emissions (tons)")
plt.ylabel("Country")
plt.title("Countries with the highest average CO2 emissions.")
plt.gca().invert_yaxis() #flip so highest emissions is at the top
plt.show()

