import matplotlib.pyplot as plt 
import csv
  
x = [] 
y = [] 


with open('climate_change_dataset_rounded.csv','r') as csvfile:
    plots = csv.reader(csvfile)

    csv.reader= csv.reader(csvfile) 
    next(csv.reader) #skips the headings

    for row in plots:
        x.append(row[0]) #inserts the countries
        y.append(float(row[7])) #inserts the renewable energy %
        
  
plt.bar(x, y, color = 'r', width = 0.5, label = "renewable energy %") 

plt.xlabel('countires') 
plt.ylabel('countries highest percentage of renewable energy') 
plt.title('graph showing which country has the highest percentage of renewable energy')
plt.legend() 
plt.grid(True)
plt.ylim(34,51)
plt.yticks(range(34,51,2))


plt.show()