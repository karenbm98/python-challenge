# Reading the csv file
import csv

with open ('Resources/budget_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)

    # Defining variables
    totalmonths = 0
    total = 0
    changes = 0
    first = 1088983
    listofchanges = []
    listofmonths = []

    for x in pointer:

        # Counting the number of months
        totalmonths = totalmonths + 1

        # Adding all total values
        total = total + int(x[1])

        # Creating a list of the months
        listofmonths.append(x[0]) 

        # Finding the delta from the current month vs one period before
        second = int(x[1])
        changes = second - first
        first = int(x[1])

        # Creating a list of the deltas
        listofchanges.append(changes)

# Printing the results
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(totalmonths))
print('Total: $' + str(total))
    
# Finding the average of the deltas and printing the result
avechange = sum(listofchanges) / (len(listofchanges)-1)
print('Average Change: $' + str(round(avechange,2)))
   
# Finding the max value of the deltas and printing the result
maxchange = max(listofchanges)
indexmax = listofchanges.index(maxchange)
print('Greatest Increase in Profits: ' + listofmonths[indexmax] + ' $' + str(maxchange))
   
# Finding the min value of the deltas and printing the result
minchange = min(listofchanges)
indexmin = listofchanges.index(minchange)
print('Greatest Decrease in Profits: ' + listofmonths[indexmin] + ' $' + str(minchange))


# Exporting the results in an Export txt File
import sys
file = open('analysis/output.txt', 'a')
sys.stdout = file

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(totalmonths))
print('Total: $' + str(total))
print('Average Change: $' + str(round(avechange,2)))
print('Greatest Increase in Profits: ' + listofmonths[indexmax] + ' $' + str(maxchange))
print('Greatest Decrease in Profits: ' + listofmonths[indexmin] + ' $' + str(minchange))

file.close()
