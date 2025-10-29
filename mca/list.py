array= []
for i in range (5):
     value= int(input(f"Enter Element {i+1}: "))
     array.append(value)
number=[]

for i in array :
    if i > 0 :
        number.append(i)
square=[]
for i in array :
    num=i*i
    square.append(num)
    
print ("your array:", array)
print ("positive array" , number)
print ("square array:" ,square)



string=input("enter the characters: ")

vowels = set ("aeiouAEIOU")

for i in string:
    for j in vowels:
        if(i==j):
            print (i)


charc=input("enter the charctores: ")
ordinal=[]

for i in charc:
    value=ord(i)
    ordinal.append(value)

print(ordinal)
            
