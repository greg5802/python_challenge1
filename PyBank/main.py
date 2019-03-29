#1/2
import os

import csv

csvpath = os.path.join('PyBank','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)

    for row in csvreader:
        #print(csvreader)
        count_row = sum(1 for row in csvreader)
        print("Total Months:",count_row)


#---------------------------------------------------------------------------------------------
#2
import os

import csv

csvpath = os.path.join('PyBank','budget_data.csv')

#rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csvreader:
        #print(csvreader)
        total = int(row[1]) -total

    print(total)

#---------------------------------------------------------------------------------------------
#3
average = total/count_row
print(average)
#--------------------------------------------------------------------------------------------
#4
import os

import csv

csvpath = os.path.join('PyBank','budget_data.csv')

rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rand_list.append(int(row[1]))
        max_num = max(rand_list)

    print(max_num)

#------------------------------------------------------------------------------------------------
import os

import csv

csvpath = os.path.join('PyBank','budget_data.csv')

rand_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rand_list.append(int(row[1]))
        min_num = min(rand_list)

    print(min_num)
