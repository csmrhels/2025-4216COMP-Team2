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

    #skips header row
    next(plots) 

    for int, row in enumerate (plots):

        #inserts the years
        year = (row[1])
        #inserts the sea level rise
        sea_level = (float(row[4])) 

        #gets the information about each county
        if 296 <= int <= 317:
            file['UK']['x'].append(year)
            file['UK']['y'].append(sea_level)
        elif 318 <= int <= 339:
            file['USA']['x'].append(year)
            file['USA']['y'].append(sea_level)
        elif 90 <= int <= 110:
            file['China']['x'].append(year)
            file['China']['y'].append(sea_level)
        elif 22 <= int <= 42:
            file['Australia']['x'].append(year)
            file['Australia']['y'].append(sea_level)

#plotting the graph
fig, axs = plt.subplots(2,2, figsize=(10, 8))
plt.tight_layout()

axs[0][0].plot(file['UK']['x'], file['UK']['y'])
axs[0,0].set_ylabel("sea level rise mm")
axs[0][0].set_title("UK")

axs[0][1].plot(file['USA']['x'], file['USA']['y'])
axs[0,1].set_ylabel("sea level rise mm")
axs[0][1].set_title("USA")

axs[1][0].plot(file['China']['x'], file['China']['y'])
axs[1,0].set_ylabel("sea level rise mm")
axs[1][0].set_title("China")

axs[1][1].plot(file['Australia']['x'], file['Australia']['y'])
axs[1,1].set_ylabel("sea level rise mm")
axs[1][1].set_title("Australia")

plt.show()