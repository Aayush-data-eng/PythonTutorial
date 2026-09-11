heros=['spider man','thor','hulk','iron man','captain america']

print ("1. Length of the list:-" , end = " ")
lengthOfHeroList = len(heros)
print (lengthOfHeroList)

print ("2. Add 'black panther' at the end of this list.")
heros.append("black panther")
print ("Our records of the super heros, having added 'black panther':-")
print ("Records:-" , end= " ")
for hero in heros:
  if hero == heros[len(heros)-1] :
    print (hero , end= ".")
    break
  print (hero , end= ", ")
print ()

print ("3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'")
heros.remove("black panther")
#in real we don't kne exactly wher is the hulk present in our heros list record so:
position = 0
for hero in heros:
  position += 1
  if hero == "hulk" : break
# print (position)
heros.insert(position , "black panther")
print ("Our records of the super heros, having added 'black panther' at  the right position:-")
print ("Records:" , end= " ")
for hero in heros:
  if hero == heros[len(heros)-1] :
    print (hero , end= ".")
    break
  print (hero , end= ", ")
print ()

print ("4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code.")
heros[1:3] = ["doctor strange"]
print ("records:" , end= " ")
for hero in heros:
  if hero == heros[len(heros)-1] :
    print (hero , end= ".")
    break
  print (hero , end= ", ")
print ()

print ("5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)")
# print (dir())
heros.sort()
print ("records:" , end= " ")
for hero in heros:
  if hero == heros[len(heros)-1] :
    print (hero , end= ".")
    break
  print (hero , end= ", ")
print ()