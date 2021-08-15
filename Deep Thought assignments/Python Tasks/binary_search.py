import random 
lst=[]
for i in range(0,100,2): #Generates random numbers 0 to 100 with  difference  2 between them.
    num=lst.append(i)
lst2=[]
for i in range(5):
    n=random.choice(lst)
    lst2.append(n)
    lst2.sort() #list  with random sucseedin numbers in sorted order
print(lst2)

def binary_search(lst2, low, high, x):
     
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if lst2[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left sub lst2
        elif lst2[mid] > x:
            return binary_search(lst2, low, mid - 1, x)
 
        # Else the element can only be present in right sub lst2
        else:
            return binary_search(lst2, mid + 1, high, x)
 
    else:
        # Element is not present in the lst2
        return -1
    
x=int(input("Enter digit"))
result = binary_search(lst2, 0, len(lst2)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
