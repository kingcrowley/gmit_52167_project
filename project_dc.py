# David Crowley g00364706
#52167 project
#project starting off file (copied from exercise 5)


# open file iris.data in read mode (for text which is the default anyway)

totalPetalLength = 0
totalPetalWidth = 0
totalSepalLength = 0
totalSepalWidth = 0

# to count the number of lines in the dataset
count = 0
with open('iris.data', 'rt') as irisdata:
    # for each line in the data set
    for line in irisdata:
        count = count +1;
        # print(line)
        # split the line and store it
        splitline = line.split(",")
        totalPetalLength += float(splitline[0])
        # print out details needed with the added string details to show the user the details needed
        print("Petal Length: " + splitline[0] + " " + "Petal Width: " + splitline[1] + " " + "Sepal Length: " + splitline[2] + " "+ "Sepal Width: " + splitline[3]) 
# close the file       
irisdata.close()
print(count)
print(totalPetalLength/count)
