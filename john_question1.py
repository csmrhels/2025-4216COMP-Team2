import matplotlib.pyplot as plt
import csv
file = {
    'UK': {'x':[], 'y':[]},
    'USA': {'x':[], 'y':[]},
    'China': {'x':[], 'y':[]},
    'Australia': {'x':[], 'y':[]}
}

 
with open('climate_change_dataset_rounded.csv','r') as csvfile:
    plots = csv.reader(csvfile)

    csv.reader= csv.reader(csvfile) 
    next(csv.reader) #skips the headings

    for int, row in enumerate (plots):
        year = (row[1]) #inserts the years
        sea_level = (float(row[4])) #inserts the sea level rise

        if 298 <= int <= 319:
            file['UK']['x'].append(year)
            file['UK']['y'].append(sea_level)
        elif 320 <= int < 342:
            file['USA']['x'].append(year)
            file['USA']['y'].append(sea_level)
        elif 92 <= int < 113:
            file['China']['x'].append(year)
            file['China']['y'].append(sea_level)
        elif 24 <= int < 45:
            file['Australia']['x'].append(year)
            file['Australia']['y'].append(sea_level)

fig, axs = plt.subplots(2,2)

axs[0][0].plot(file['UK']['x'], file['UK']['y'])
axs[0][0].set_title("UK")

axs[0][1].plot(file['USA']['x'], file['USA']['y'])
axs[0][1].set_title("USA")

axs[1][0].plot(file['China']['x'], file['China']['y'])
axs[1][0].set_title("China")

axs[1][1].plot(file['Australia']['x'], file['Australia']['y'])
axs[1][1].set_title("Australia")

plt.show()