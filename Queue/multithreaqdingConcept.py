import time
import threading

def calculateSquare (num) :
  print("Square of the provided numbeers is as follows: ")
  for ele in num :
    time.sleep(0.2)
    print (f"Square of {ele}:- {ele**2}")

def calculateCube (num) :
  print("Cube of the provided numbers is as follows: ")
  for n in num :
    time.sleep(0.2)
    print(f"Cube of {n}:- {n**3}")

arr = [2, 3, 8, 9]
# initialTime = time.time()
# calculateSquare(arr)
# calculateCube(arr)

task1 = threading.Thread(target = calculateSquare, args=(arr,))
task2 = threading.Thread(target= calculateCube, args= (arr,))
initialTime = time.time()

task1.start()
task2.start()

task1.join()
task2.join()
finalTime = time.time()
print("Execution done in:" , finalTime-initialTime)