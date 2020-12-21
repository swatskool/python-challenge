#initialising libraries
import csv
import os
dates = [] # list of dates 
profit_loss = [] # list of profit/ loss
change = [] # list of change on every date
total = 0 # total change
change_sum = 0
#my_dict = {'name':0}
value = 0
csv_path = os.path.join('..','PyBank', 'Homework_03-Python_PyBank_Resources_budget_data.csv')
with open(csv_path, 'r') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)#getting rid of header
    for line in csv_reader:
            profit_loss.append(int(line[1])) # daily profit/loss
            total += int(line[1]) # total over the month
            dates.append(line[0]) # number of dates
#f.close()
end_value = len(profit_loss)
 
for i in range(1,end_value):
    value = profit_loss[i]-profit_loss[i-1]
    change.append(value) # change in profit loss
    change_sum += value # total profit/loss

total_months = len(dates)
average = change_sum/(total_months-1)
max_change_month = dates[change.index(max(change))+1]
min_change_month = dates[change.index(min(change))+1]
max_change = max(change)
min_change = min(change)

#output on the terminal

print('\nFinancial Analysis\n')
print('-----------------------\n')
print(f'Total Months: {total_months}\n')
print(f'Total: $ {total}\n')
print(f'Average  Change: $: {round(average,2)}\n')
print(f'Greatest Increase in Profits: {max_change_month}  $({round(max_change)})\n')
print(f'Greatest Decrease in Profits: {min_change_month}  $({round(min_change)})\n')

#output in the new file named PyBank_Swati.txt
with open('PyBank_Swati.txt', 'w') as f:
    f.write('\nFinancial Analysis\n')
    f.write('-----------------------\n')
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: $ {total}\n')
    f.write(f'Average  Change: $: {round(average,2)}\n')
    f.write(f'Greatest Increase in Profits: {max_change_month}  $({round(max_change)})\n')
    f.write(f'Greatest Decreasein Profits: {min_change_month}  $({round(min_change)})\n')

