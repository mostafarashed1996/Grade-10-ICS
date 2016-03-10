monthfiles = open("months.txt","r")
rainfallfiles = open("rainfall.txt","r")
count = 0
average = 0
damonthslist = []
darainfalllist = []
while True:
    months = monthfiles.readline()
    rainfall = rainfallfiles.readline()
    if months == "":
        break
    damonthslist.append(months.rstrip("\n"))
    darainfalllist.append(float(rainfall.rstrip("\n")))
wetmonth = damonthslist[darainfalllist.index(max(darainfalllist))]
drymonth = damonthslist[darainfalllist.index(min(darainfalllist))]
wet = max(darainfalllist)
dry = min(darainfalllist)
for t in darainfalllist:
    t = float(t)
    count = count + t
    average=count/len(darainfalllist)
print "Toronto's Rainfall Report in 2011\nMinimum \t%s\t %.1f CM\nMaximum \t%s %.1f CM\nAverage \tAll Months %.1f CM " %(wetmonth, wet, drymonth, dry, average)
raw_input()         
