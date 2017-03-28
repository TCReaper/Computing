# Name: Hao Shaun

# 2017 - Term 2 - SH1 Computing Practical Lecture Test 2
# Code for Task 2

fcost = open("COSTS.TXT","r")
costs = []
for i in fcost:
    i = i[:len(i)-1]
    costs.append(int(i))

frev = open("REVENUES.TXT","r")
revenue = []
for i in frev:
    i = i[:len(i)-1]
    revenue.append(int(i))

statAmount = len(costs)
profits = []
for i in range(statAmount):
    profit = revenue[i] - costs[i]
    profits.append(profit)

years = [2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
month = ["January","February","March","June","May","April","July","August","September","October","November","December"]

minprofit = min(profits)
mindex = profits.index(minprofit)
mincost = costs[mindex]
minrev = revenue[mindex]
minyear = years[(mindex+1)//12]
minmonth = month[((mindex+1)%12)-1]

maxprofit = max(profits)
maxdex = profits.index(maxprofit)
maxcost = costs[maxdex]
maxrev = revenue[maxdex]
maxyear = years[(maxdex+1)//12]
maxmonth = month[((maxdex+1)%12)-1]

print(str(minmonth)+" "+str(minyear)+" had the least profit of "+str(minprofit)+", with "+ str(minrev)+" revenue and "+str(mincost)+" cost")
print(str(maxmonth)+" "+str(maxyear)+" had the most profit of "+str(maxprofit)+", with "+ str(maxrev)+" revenue and "+str(maxcost)+" cost")
print("I gave up on merge sort :D")















def mergeSort(data):
    if len(data)<2:
        return data
    else:
        return merge(mergesort(data[:len(data)//2]),mergesort(data[len(data)//2:]))


    
