#Rainfall Information Calculator
#This program will state the highest, lowest, and the average rainfalls for the year of 2011 in Toronto

print " Yearly Rainfall"
Total = 0
Items1 = " "
Items2 = " "
MonthsList = []
RainfallList = []
Months = open("months.txt","r")
Rainfall = open("rainfall.txt","r")
while Items1 != "":
              Items1 = Months.readline()
              MonthsList.append(Items1.rstrip("\n"))
while Items2 != "":
              Items2 = Rainfall.readline()
              RainfallList.append(Items2.rstrip("\n"))
Max = max(RainfallList)
Index = RainfallList.index(Max)
print "Maximum       " + MonthsList[Index] + "          " + str(RainfallList[Index])
del RainfallList[RainfallList.index("")]
Min = min(RainfallList)
Index2 = RainfallList.index(Min)
print "Minimum       " + MonthsList[Index2] + "      " + str(RainfallList[Index2])              
for values in RainfallList:
    values = float(values)
    Total = Total + values
    Average = Total/len(RainfallList)
print "Average Monthly            ", round(Average,1)
raw_input()
