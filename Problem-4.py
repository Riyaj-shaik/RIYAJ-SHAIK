list_of_numbers=list(map(int,input().split(",")))
dictionary=dict()
for i in range(1,10):
    dictionary[i]=0
    for element in list_of_numbers:
        if(element % i ==0):
            dictionary[i] +=1
print(dictionary.items())