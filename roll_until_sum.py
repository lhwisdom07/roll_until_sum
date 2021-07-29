import random
from random import randrange

random.randrange(1,7) 
target = int(input("Enter the target number : ")) 
counts=0;

while(True):
    counts=counts + 1 
    val1=(int(random.random()*10))%6+1 
    val2=(int(random.random()*10))%6+1 
  
    sum = val1 + val2 
    print("Roll : ",val1," and ",val2, " sum is ",sum)
    if(sum == target): 
        break
  
print("Got it in ",counts," rolls")