
print("Enter the operation")
opa = input('operation')

if opa == '+':
    x = input('enter first number :')
    y = input('enter first number :')
    print(  'answer',int(x) + int(y))
elif opa == '/':
    x = input('enter first number :')
    y = input('enter first number :')
    print( 'answer',int(x) / int(y))
elif opa == '*':
    x = input('enter first number :')
    y = input('enter first number :')
    print(  'answer',int(x) * int(y))
elif opa == '-':
    x = input('enter first number :')
    y = input('enter first number :')
    print( 'answer', int(x) - int(y))
else:
    print('undefined')

