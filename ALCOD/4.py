num = int(input("Enter a number: "))
Enter a number: 153
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

   
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

    
153 is an Armstrong number
