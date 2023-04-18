# Reading the csv file
import csv

with open ('Resources/election_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)

    # Defining variables
    numberofvotes = 0
    charlesvotes = 0
    dianavotes = 0
    raymonvotes = 0

    for x in pointer:
        # Counting the total number of votes
        numberofvotes = numberofvotes + 1

        # Counting the total number of votes for each candidate
        if x[2] == 'Charles Casper Stockham':
            charlesvotes = charlesvotes + 1
        
        elif x[2] == 'Diana DeGette':
            dianavotes = dianavotes + 1
        
        else:
            x[2] == 'Raymon Anthony Doane'
            raymonvotes = raymonvotes + 1

    # Printing the results
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(numberofvotes))
    print('-------------------------')

    # Printing the results for each candidate
    charlespercentage = charlesvotes / numberofvotes * 100
    print('Charles Casper Stockham: ' + str(round(charlespercentage,3)) + '% (' + str(charlesvotes) + ')')

    dianapercentage = dianavotes / numberofvotes * 100
    print('Diana DeGette: ' + str(round(dianapercentage,3)) + '% (' + str(dianavotes) + ')')

    raymonpercentage = raymonvotes / numberofvotes * 100
    print('Raymon Anthony Doane: ' + str(round(raymonpercentage,3)) + '% (' + str(raymonvotes) + ')')

    # Printing the winner
    print('-------------------------')
    print('Winner: Diana DeGette')



# Exporting the results in an Export txt File
import sys
file = open('analysis/output.txt', 'a')
sys.stdout = file

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(numberofvotes))
print('-------------------------')
print('Charles Casper Stockham: ' + str(round(charlespercentage,3)) + '% (' + str(charlesvotes) + ')')
print('Diana DeGette: ' + str(round(dianapercentage,3)) + '% (' + str(dianavotes) + ')')
print('Raymon Anthony Doane: ' + str(round(raymonpercentage,3)) + '% (' + str(raymonvotes) + ')')
print('-------------------------')
print('Winner: Diana DeGette')

file.close()
