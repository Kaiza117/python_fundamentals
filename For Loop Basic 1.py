#1. 
for i in range(0,151,1):
    print(i)
#2. 
for i in range(5,1005,5):
    print(i)
#3. 
for i in range(1,101,1):
    if i%5 == 0:
        if i%10 == 0:
            i = "Coding Dojo"
        else:
            i = "Coding"
    print(i)
#4. 
sum = 0
for i in range(1,500000,2):
    sum += i
print(sum)
#5. 
for i in range(2018,0,-4):
    print(i)
#6. 
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)