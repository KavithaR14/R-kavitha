a = int(input("Enter a number: "))
if a % 2 == 0:
   normalized_a = a-1
else:
   normalized_a = a

for i in range(1,2*normalized_a, 2):
    print(i, end=" ")
