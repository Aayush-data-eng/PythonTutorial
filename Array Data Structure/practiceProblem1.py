# from ifelse import expence
monthlyExpence = {
  "January" : 2200 ,
  "February" : 2350,
  "March" : 2009 ,
  "April" : 2130 ,
  "May" : 2190
}
print ("This is your first five monthly expenses:")
for month in monthlyExpence :
  print (month , " expence = " , monthlyExpence[month])

print ("\nNow these are the answes given by you in the previous questionaire round:-")

print (f"1. In Feb, how many dollars you spent extra compare to January?:- ${monthlyExpence['February'] - monthlyExpence['January']}/-")

# we need to sum for the first 3 months. 
print ("2. Find out your total expense in first quarter (first three months) of the year:-" , end = " ")
lastMonth = 3
# total = sum(expence for i , (month , expence) in enumerate(monthlyExpence.items()) if i < lastMonth)
total = sum (monthlyExpence[month] for i , month in enumerate(monthlyExpence) if i < lastMonth)
print (f"${total}/-")

print ("3. Find out if you spent exactly 2000 dollars in any month:-" , end = ' ')
for month in monthlyExpence :
  resMonth = ''
  if monthlyExpence[month] == 2000 :
    resMonth = month
    break
if (resMonth == "") :
  print ("No such month, where I spent exactly $2000/-")
else :
  print (resMonth)

print ("4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list")
monthlyExpence["June"] = 1980
print ("The updated monthly expences list is as follows:-")
for month in monthlyExpence :
  print (month , " expence = " , monthlyExpence[month])

print ("5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.")
monthlyExpence["April"] += 200
print ("The updated record of the monthly expence is as follows: ")
for month , expence in monthlyExpence.items() :
  print (f"{month}'s' expence:- {expence}")