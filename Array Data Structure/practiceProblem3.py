maxNumber = int(input("Enter a number of your choice: "))
oddElements = []
#for i in range(maxNunmber+1) :
#  if i % 2 != 0:
#    oddElements.append(i)
#print (oddElements)

# This can be written in some other way as well in only a single line using list comphrehension
oddEle = [num for num in range(maxNumber + 1) if num % 2 != 0]
print (oddEle)