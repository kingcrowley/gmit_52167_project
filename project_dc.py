# David Crowley g00364706
#52167 project
#project starting off file (copied from exercise 5)


# open file iris.data in read mode (for text which is the default anyway)
from statistics import median, mode, pstdev, mean
from matplotlib import pyplot as plt
import math
from collections import Counter

sepalLengthList = []
setosaSepalLengthList = []
versicolorSepalLengthList = []
virginicaSepalLengthList = []
sepalWidthList = []
setosaSepalWidthList = []
versicolorSepalWidthList = []
virginicaSepalWidthList = []
petalLengthList = []
setosaPetalLengthList = []
versicolorPetalLengthList = []
virginicaPetalLengthList = []
petalWidthList = []
setosaPetalWidthList = []
versicolorPetalWidthList = []
virginicaPetalWidthList = []
classList = []
#totalPetalLength = 0
#totalPetalWidth = 0
totalSepalLength = 0
#totalSepalWidth = 0

# to count the number of lines in the dataset
count = 0
with open('iris.data', 'rt') as irisdata:
    # for each line in the data set
    for line in irisdata:
        
        # print(line)
        # split the line and store it
        splitline = line.split(",")
        print(splitline[0])
        totalSepalLength += float(splitline[0])
        # store latest sepal length + width in lists for calculations.
        sepalLengthList.append(float(splitline[0]))
        sepalWidthList.append(float(splitline[1]))
        petalLengthList.append(float(splitline[2]))
        petalWidthList.append(float(splitline[3]))
        classList.append(splitline[4])
        
        if splitline[4].strip()=="Iris-setosa":
            setosaSepalLengthList.append(float(splitline[0]))
            setosaSepalWidthList.append(float(splitline[1]))
            setosaPetalLengthList.append(float(splitline[2]))
            setosaPetalWidthList.append(float(splitline[3]))
        elif splitline[4].strip()=="Iris-versicolor":
            versicolorSepalLengthList.append(float(splitline[0]))
            versicolorSepalWidthList.append(float(splitline[1]))
            versicolorPetalLengthList.append(float(splitline[2]))
            versicolorPetalWidthList.append(float(splitline[3]))
        elif splitline[4].strip()=="Iris-virginica":
            virginicaSepalLengthList.append(float(splitline[0]))
            virginicaSepalWidthList.append(float(splitline[1]))
            virginicaPetalLengthList.append(float(splitline[2]))
            virginicaPetalWidthList.append(float(splitline[3]))


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

# TODO put this into a function for printing/testing purposes. Just pass in the specific list i need to use
""" print("Sepal Length - Descriptive Stats")
print("Mean from stats module: " + str(mean(sepalLengthList)))
# mean calculated by using total divided by count. Unnessecary with the stats module. 
print("Mean: " + str(totalSepalLength/count))
print("Median: " + str(median(sepalLengthList)))
print("Mode: " + str(mode(sepalLengthList)))
print("Standard Deviation: " + str(pstdev(sepalLengthList)))
print("Max: " + str(max(sepalLengthList)))
print("Min: " + str(min(sepalLengthList))) """
# for testing
# print(sepalLengthList)
#print(sepalWidthList)

""" print("Sepal Width- Descriptive Stats")
print("Mean from stats module: " + str(mean(sepalWidthList)))
print("Median: " + str(median(sepalWidthList)))
print("Mode: " + str(mode(sepalWidthList)))
print("Standard Deviation: " + str(pstdev(sepalWidthList)))
print("Max: " + str(max(sepalWidthList)))
print("Min: " + str(min(sepalWidthList))) """


def do_desc_stats(aList, title=""):
    print(title + " - Descriptive Stats")
    print("Mean from stats module: " + str(mean(aList)))
    print("Median: " + str(median(aList)))
    if not (title =="Setosa Sepal Length" or title =="Versicolor Sepal Length"):
        print("Mode: " + str(mode(aList)))
    #if(title !="Setosa Sepal Length"):
    #    print("Mode: " + str(mode(aList)))
    
    print("Standard Deviation: " + str(pstdev(aList)))
    print("Max: " + str(max(aList)))
    print("Min: " + str(min(aList)))
    print("******************")

# code edited from Data Science from Scratch Chapter 10
def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

#plot_histogram(sepalLengthList, .2, "Sepal Length Histogram")
#plot_histogram(sepalWidthList, .2, "Sepal Width Histogram")
do_desc_stats(sepalLengthList, "Sepal Length")
#do_desc_stats(sepalWidthList, "Sepal Width")
#do_desc_stats(petalLengthList, "Petal Length")
#do_desc_stats(petalWidthList, "Petal Width")

do_desc_stats(setosaSepalLengthList, "Setosa Sepal Length")
do_desc_stats(versicolorSepalLengthList, "Versicolor Sepal Length")
do_desc_stats(virginicaSepalLengthList, "Virgincia Sepal Length")


#do_desc_stats(setosaSepalWidthList, "Setosa Sepal Width")
#do_desc_stats(setosaPetalLengthList, "Setosa Petal Length")
#do_desc_stats(setosaPetalWidthList, "Setosa Petal Width")






#plt.scatter(sepalLengthList, sepalWidthList,alpha=0.2, s=100*petalLengthList, c = classList, cmap='viridis')
plt.scatter(sepalLengthList, sepalWidthList,alpha=0.2, s=100*petalLengthList)
plt.show()