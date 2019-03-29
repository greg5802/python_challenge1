#1

import os

import csv

total_vote = 0
csvpath = os.path.join('PyPoll','election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)

    for row in csvreader:
        total_vote = total_vote + 1

    print(f"Total Votes:",total_vote)


-------------------------------------------------------------------------------------------------
#2
import os

import csv

count_khan = 0
count_correy = 0
count_li = 0
count_otooley = 0

csvpath = os.path.join('PyPoll','election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)


    for row in csvreader:
        if row[2] == "Khan":
            count_khan = count_khan + 1
        elif row[2] == "Correy":
            count_correy = count_correy + 1
        elif row[2] == "O'Tooley":
            count_otooley = count_otooley + 1
        elif row[2] == "Li":
            count_li = count_li + 1

    print(f"Khan:",round((count_li/total_vote)*100,4),"%","("+str(count_li)+")")
    print(f"Correy:",round((count_correy/total_vote)*100,4),"%","("+str(count_correy)+")")
    print(f"Khan:",round((count_khan/total_vote)*100,4),"%","("+str(count_khan)+")")
    print(f"O'Tooley:",round((count_otooley/total_vote)*100,4),"%","("+str(count_otooley)+")")
