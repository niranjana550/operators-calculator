operation = input("enter the operator:")
if operation in["addition","subraction","multiplicatin","division","modulus","floor division"]:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    if operation == "addition":  
       print("addition of two number is:",num1+num2)
    elif operation == "subraction": 
       print(" subraction of two number is:",num1-num2) 
    elif operation == "multiplication":    
       print("multiplication of two number is:",num1*num2)
    elif  operation == "division":
       print("division of two number is:",num1/num2)  
    elif  operation == "modulus": 
       print("modulus of two number is:",num1%num2)    
    elif operation == "floor division": 
       print("floor division of two number is:",num1//num2) 
     

elif operation in["<",">","<=",">=","==","!="]:
      num1=int(input("enter a number:"))
      num2=int(input("enter a numbe:"))
      if operation== "<":
         print("boolian is:",num1<num2)
      elif operation== ">":
         print("boolian is:",num1>num2)
      elif operation== "<=":
         print("boolian is:",num1<=num2)
      elif operation== ">=":
         print("boolian is:",num1>=num2) 
      elif operation== "==":
         print("boolian is:",num1==num2) 
      elif operation== "!=":
         print("boolian is:",num1!=num2)                      
       

