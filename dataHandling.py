import csv
import statistics
import math

with open("data.csv") as f:
    df = csv.reader(f)
    dfList = list(df)

tempList = []

for sublist in dfList:
    for element in sublist:
        tempList.append(float(element))

mean = statistics.mean(tempList)

summation = 0

for i in tempList:
    deviationsq = (i - mean)**2
    summation += deviationsq

denominator = len(tempList) - 1

standardDeviation = math.sqrt(summation/denominator)
print(standardDeviation)

automatic = statistics.stdev(tempList)
print(automatic)