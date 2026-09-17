records = {}
with open ("nyc_weather.csv", 'r') as fs :
  for line in fs :
    try:
      token = line.split(",")
      temperature = int(token[1])
      day = token[0]
      records [day] = temperature
    except :
      print("Invalid Temperature, Ignore this row, it would be the heading of the rows of the required data.")


#print(records)
print("\n(1)nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,")

print("(i) What was the average temperature in first week of Jan :-" , end = " ")
tempSum = 0
dayCount = 0
for day in records:
  if day == 'Jan 8' : break
  tempSum += records[day]
  dayCount += 1

print(round(tempSum/dayCount, 4))

print("(ii)What was the maximum temperature in first 10 days of Jan:-", end =" ")
maxTemp = 0
for day, temp in records.items() :
  maxTemp = max(maxTemp, temp)
print(maxTemp, "F")  


print ("(2)nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,")

print("(i)What was the temperature on Jan 9? ", records['Jan 9'], "F")
print("(ii)What was the temperature on Jan 4?", records["Jan 4"], "F")      