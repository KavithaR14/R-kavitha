number =input()
n=list(map(int, number.split(',')))

base_list=[1,2,3,4,5,6,7,8,9,10]
result={}
for base in base_list:
    count=0
    for num in n:
        if num % base == 0:
            count+=1
    result[base]=count
print(result)