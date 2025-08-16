def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = int(input()); 
print("Number: ",num)
print("Factorial: ",factorial(num))



def fibonacci(num):
    if(num==1):
        return 0
    elif(num == 2):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
    


print(fibonacci(num))