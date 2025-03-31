#Question: What countries have the highest average CO2 emissions per person.
import matplotlib.pyplot as plt
import pandas as pd
import csv

path = "climate_change_dataset_rounded.csv"
df = pd.read_csv(path)

#Group by the country to work out average for each one and find mean.
averageCo2Cont = df.groupby("Country")["CO2 Emissions (Tons/Capita)"].mean()

print("The Country with the highest average emmissions was: ", averageCo2Cont.idxmax(), " with ", averageCo2Cont.max(), "tons average per person.")
print("The Country with the lowest average emmissions was: ", averageCo2Cont.idxmin(), " with ", averageCo2Cont.min(), "tons average per person.")

#Plot the results on the table... as there is 15 countries sort highest to lowest from all countires
topCont = averageCo2Cont.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
bars = plt.barh(topCont.index, topCont.values, color='grey')

#Sort the values out so they dont highlight the incorrect values.
averageCo2Cont = averageCo2Cont.sort_values()
highest_bar_index = list(averageCo2Cont.index).index(averageCo2Cont.idxmax())
lowest_bar_index = list(averageCo2Cont.index).index(averageCo2Cont.idxmin())

bars[highest_bar_index].set_color('green')  # Highlight lowest due to flipped
bars[lowest_bar_index].set_color('red')  # Highlight highest due to flipped




plt.xlabel("Average CO2 Emissions (tons) / per person")
plt.ylabel("Country")
plt.title("Countries with the highest average CO2 emissions per person.")
plt.gca().invert_yaxis() #flip so highest emissions is at the top
plt.show()


