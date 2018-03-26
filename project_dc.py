# David Crowley g00364706
#52167 project
#project starting off file (copied from exercise 5)


# open file iris.data in read mode (for text which is the default anyway)
from statistics import median, mode, pstdev, mean
from matplotlib import pyplot as plt
petalLengthList = []
totalPetalLength = 0
totalPetalWidth = 0
totalSepalLength = 0
totalSepalWidth = 0

# to count the number of lines in the dataset
count = 0
with open('iris.data', 'rt') as irisdata:
    # for each line in the data set
    for line in irisdata:
        
        # print(line)
        # split the line and store it
        splitline = line.split(",")
        totalPetalLength += float(splitline[0])
        # store latest petal length in the list for calculations.
        petalLengthList.append(float(splitline[0]))
        # print out details needed with the added string details to show the user the details needed
        print("Sepal Length: " + splitline[0] + " Sepal Width: " + splitline[1] + " Petal Length: " + splitline[2] + " Petal Width: " + splitline[3] + " Class: " + splitline[4]) 
        count = count +1
        
        
# close the file       
irisdata.close()
print(count)
# using inbuilt python function to calcluate median etc. 
# statistics link - https://docs.python.org/3/library/statistics.html
# I could have used mean inbuilt into the statistics module to calculate the mean
print("Mean from stats module: " + str(mean(petalLengthList)))
# mean calculated by using total divided by count. Unnessecary with the stats module. 
print("Mean: " + str(totalPetalLength/count))
print("Median: " + str(median(petalLengthList)))
print("Mode: " + str(mode(petalLengthList)))
print("Standard Deviation: " + str(pstdev(petalLengthList)))
print("Max: " + str(max(petalLengthList)))
print("Min: " + str(min(petalLengthList)))


