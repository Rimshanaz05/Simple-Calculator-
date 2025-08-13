def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Solution: ")
print("1:Add")
print("2:Substract")
print("3:Multiply")
print("4:Divide")
while True:
   choice=float(input("Choose from 1/2/3/4"))
   if choice in('1','2','3','4'):
       try:
           num1=float(input("Enter the first number "))
           num2=float(input("Enter the second number: "))
       except ValueError:
           print("Invalid Entry")
           continue
       if choice =='1':
           print("Result=",add(num1,num2))
       elif choice =='2':
           print("Result=",sub(num1,num2))
       elif choice =='3':
           print("REsult=",multiply(num1,num2))
       elif choice =='4':
           print("Result=",divide(num1,num2))
       else:
           print("Invalid")
         
           
