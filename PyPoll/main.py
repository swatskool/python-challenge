# initialising required libraries
import os
import csv
from collections import OrderedDict
county= {}
name = {}
# function that returns the key corresponding to the value in a dictionary
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
            return key
 
# opening the csv resource file
csv_path = os.path.join('..','PyPoll', 'Homework_03-Python_PyPoll_Resources_election_data.csv')
i=0
#csvfile = open(csv_path)
with open(csv_path,'r') as csvfile:

    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)
    for line in csv_reader:
        
        name[int(line[0])] = line[2]# creating a dictionary with key as voteID and candidate name as value
    total = len(name)# total number of votes
count = {}
i = 0
c= 0
name_set =  set(name.values())# getting unique names of the candidates

for n in name_set:
    for key,value in name.items():
        if n == value:
            c +=1 
        
    count[n]= c #counting the votes of each candidate and updating it into a list
    percent = round((c/total)*100) # percentage votes per candidate
    c= 0
    i+=1

# counting the highest number of votes
max_value = max(count.values())
# candidate name against the highest number of votes
candidate = get_key(count,max_value)
    

#printing the output on the terminal
print('\nElection Results')
print('--------------------------')
print(f'Total Votes: {total}')
print('--------------------------')

count = OrderedDict(sorted(count.items(), reverse = True, key=lambda x: x[1])) # sorting the dictionary on descending value of votes
for cname, votes in count.items(): 
   percent = float((votes/total)*100) # percentage votes per candidate
   print(f'{cname} : {round(percent)}% ({votes})')
print('--------------------------')
print(f'Winner: {candidate}')
print('--------------------------')

#output to a text file PyPoll_Swati.txt
with open('PyPoll_Swati.txt', 'w') as f:
	f.write('\nElection Results\n')
	f.write('--------------------------\n')
	f.write(f'Total Votes: {total}\n')
	f.write('--------------------------\n')
	for cname, votes in count.items(): 
   		percent = float((votes/total)*100) # percentage votes per candidate
   		f.write(f'{cname} : {round(percent)}% ({votes})\n')
	f.write('--------------------------\n')
	f.write(f'Winner: {candidate}\n')
	f.write('--------------------------\n')


