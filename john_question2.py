import matplotlib.pyplot as plt 
import csv 
  
x = [] 
y = [] 
  
with open('climate_change_dataset_rounded.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        x.append(row[0]) 
        y.append(float(row[7])) 
  
plt.bar(x, y, color = 'g', width = 0.72, label = "renewable energy %") 
plt.xlabel('countires') 
plt.ylabel('percentage of renewable energy') 
plt.title('graph showing which country has the highest percentage of renewable energy') 
plt.legend() 
plt.show()