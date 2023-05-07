print('welcome to calculator')

num1=int(input('please enter a num1: '))
print('***********')
print('+,-,/,*,')
print('***********')
type=input('please enter what u wanna do with number from the above: ')

num2=int(input('please enter a num2: '))

def sum():
    print(num1+num2)
def cikar():
    print(num1-num2)
def divide():
    print(num1/num2)
def carp():
    print(num1*num2)  

if type=='+':
    sum()
if type=='-':
    cikar()
if type=='/':
    divide()        
if type=='*':
    carp()                 
