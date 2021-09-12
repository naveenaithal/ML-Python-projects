counter=0
def binary_search(numbers,number,left,right):
    global counter
    counter+=1
    if left>right:
        return -1
    mid=(left+(right-1))//2
    if number==numbers[mid]:
        return mid
    elif number>numbers[mid]:
        return binary_search(numbers,number,mid+1,right)
    elif number<numbers[mid]:
        return binary_search(numbers,number,left,mid-1)
    else:
        if number not in numbers[number]:
            return "try another number"
numbers=[ 2, 3, 4, 10, 40 ]

result=binary_search(numbers,10,0,len(numbers)-1)
print(result)
# print(f'is {result}')

