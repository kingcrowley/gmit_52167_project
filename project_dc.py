# David Crowley g00364706
#52167 project
#project starting off file (copied from exercise 5)


# open file iris.data in read mode (for text which is the default anyway)
from statistics import median, mode, pstdev, mean
from matplotlib import pyplot as plt
sepalLengthList = []
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
        totalSepalLength += float(splitline[0])
        # store latest petal length in the list for calculations.
        sepalLengthList.append(float(splitline[0]))
        # print out details needed with the added string details to show the user the details needed
        # used for testing in this project. commented out
        # print("Sepal Length: " + splitline[0] + " Sepal Width: " + splitline[1] + " Petal Length: " + splitline[2] + " Petal Width: " + splitline[3] + " Class: " + splitline[4]) 
        count = count +1
        
        
# close the file       
irisdata.close()
# for testing
# print(count)
# using inbuilt python function to calcluate median etc. 
# statistics link - https://docs.python.org/3/library/statistics.html
# I could have used mean inbuilt into the statistics module to calculate the mean
print("Sepal Length - Descriptive Stats")
print("Mean from stats module: " + str(mean(sepalLengthList)))
# mean calculated by using total divided by count. Unnessecary with the stats module. 
print("Mean: " + str(totalPetalLength/count))
print("Median: " + str(median(sepalLengthList)))
print("Mode: " + str(mode(sepalLengthList)))
print("Standard Deviation: " + str(pstdev(sepalLengthList)))
print("Max: " + str(max(sepalLengthList)))
print("Min: " + str(min(sepalLengthList)))


