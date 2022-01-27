#ADD
def add(n1,n2):
    return n1 + n2
#Substract
def sub(n1,n2):
    return n1 - n2    
#Multiply    
def multiply(n1,n2):
    return n1 * n2   
#Divide     
def divide(n1,n2):
    return  n1 / n2  

num1=int(input("enter first number \n"))
symbol_list={"+": add, "-":sub,
             "*":multiply,"/": divide  }  

#IT LOOPS THROUGH OPERATOR LIST AND PRINTS THEM
for key in symbol_list:
    print(key)            

should_continue=True
while should_continue:
    symbol=input("enter the operator\n")
    num2=int(input("Enter next number\n"))
    answer=symbol_list[symbol](num1,num2)
    print(answer)
    user=input("Enter yes to continue or No to exit \n").lower()
    #HERE IT CHECKS IF USER WANT TO CONTINUE 
    #  THEN STORES NUM1 WITH ANSWER OR EXITS THE LOOP
    if user=="yes":
        num1=answer 
    else:
        should_continue=False  