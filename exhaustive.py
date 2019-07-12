import itertools
import random
import time


def randomSet():
    #initialize the array
    set = []

    #set length of array
    length = 20

    #for loop append randomize numbers into array
    for i in range(length):
        r = random.randint(0, 901)
        if r not in set: 
            set.append(r)
        else: 
            while r in set:
                r = random.randint(0, 901)
            set.append(r)
            
    
    return set

def _sum(arr, n):
    return sum(arr)

def partitions(arr):

    found = False # determine if the set of numbers have solution at the end of the loops

    sum = 0

    #partition = []# partition stores the index where the numbers are added in the partition of the set

    for i in range (len(arr)):#calculate sum of list
        sum += arr[i] 

    #if the sum is divisible by 2, it can be divided into 2 partitions with equal sum
    if (sum%2) == 0 :
        print(sum)
    else:
        print(sum)
        return False#return false to loop and generate new set of random numbers

    for i in range (len(arr)):
        test = list(itertools.combinations(arr,i))
        #print("All partition",test)

        for j in range (int(len(test)/2)):
            #print("Sum partition",_sum(test[j], len(test)))
            if (_sum(test[j], len(test))) == (sum/2):
                found = True
                print(test[j]," and ", findMissing(arr,test[j],len(arr),len(test[j])))
                break

        if found is True:
            break
                


        
    return found


def findMissing(a, b, n, m): 

    part = []  
    
    # Store all elements of second  
    # array in a hash table 
    s = dict() 
    for i in range(m): 
        s[b[i]] = 1
  
    # Print all elements of first array  
    # that are not present in hash table 
    for i in range(n): 
        if a[i] not in s.keys(): 
            part.append(a[i])
            #print(a[i], end = " ") 

    return(part)


def main():

    t = time.process_time()#initialize var to store starting time

    #get set from randomSet function
    set = randomSet()
    #print out array
    print(set)

    output = partitions(set)
    

    while output == False:
        set = randomSet()
        print(set)

        output = partitions(set)

    elapsed_time = time.process_time() - t
    print(elapsed_time)


    

main()




