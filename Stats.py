# Stats.py
# This program calculates the mean, standard deviation, and median
# for a user generated data set.


# imports math library
import math

# method that returns the standard deviation of a user-supplied data set
def getStdDev(numbers):
    sum = 0
    n = len(numbers)
    mean = getMean(numbers)
    for i in range(n):
        sum += ((numbers[i] - mean)**2)
    s = math.sqrt(sum / (n - 1))
    return s

# method that returns the mean of a user-supplied data set
def getMean(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    mean = sum / len(numbers)
    return mean

# method that returns the median of a user-supplied data set
def getMedian(numbers):
    numbers.sort()
    total = len(numbers)
    if total % 2 == 0:
        count = total // 2
        median =(numbers[count - 1] + numbers[-count]) / 2
        return median
    else:
        count = (total // 2)
        median = numbers[count]
        return median

# list to hold the user generated numbers
numbers = []

# prompts user for how many numbers in their data set
userInput= input("How many numbers are in your data set: ")

# checks to see if the user entered a valid length for their data set
while True:
    try:
        setLength = int(userInput)
    except:
        print("That is not valid input.")
        userInput = input("Try again: ")
        continue
    break

# keeps the user from entering a negative length for the data set
setLength = int(userInput)
if(setLength < 0):
    setLength *= -1


# prompts the user to enter the numbers in the data set, one at a time
for i in range(1, setLength + 1):
    numInput = input("Enter number" + str(i) + ": ")

    # keeps the user from entering invalid data
    while True:
        try:
            number = float(numInput)
        except:
            print("That is not valid input.")
            numInput = input("Try again: ")
            continue
        break
    # adds the valid number to the list
    numbers.append(float(number))

# calls the methods for mean, standard deviation, and median and assigns the
# return value to the appropriate variable
mean = getMean(numbers)
stdDev = getStdDev(numbers)
median = getMedian(numbers)

# outputs the data set and its mean, standard deviation, and median
print("The data set:", numbers)
print("The data set's mean = {:.4f}".format(mean) + ".")
print("The data set's standard deviation = {:.4f}".format(stdDev) + ".")
print("The data set's median = " + str(median) + ".")

