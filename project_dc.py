# David Crowley g00364706
#52167 project
#project starting off file (copied from exercise 5)


# open file iris.data in read mode (for text which is the default anyway)


with open('iris.data', 'rt') as irisdata:
    # for each line in the data set
    for line in irisdata:
        # print(line)
        # split the line and store it
        splitline = line.split(",")
        # print out details needed with the added string details to show the user the details needed
        print("Petal Length: " + splitline[0] + " " + "Petal Width: " + splitline[1] + " " + "Sepal Length: " + splitline[2] + " "+ "Sepal Width: " + splitline[3]) 
# close the file       
irisdata.close()
