def generate_fibonacci(value):
    if value<=1:
        return value
    else:
        return generate_fibonacci(value-1) + generate_fibonacci(value-2)


num = int(input("Enter the term to generate fibonacci series: "))
if num<=0:
    print("Enter a positive number. ")
else:
    for i in range(num):
        result= generate_fibonacci(i)    
        print(result, end=" ")