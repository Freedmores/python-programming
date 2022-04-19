#Basic exceptions
#ZeroDivisionError
#TypeError
#etc

x=input('Enter number 1: ')
y=input('Enter number 2: ')
try:
    z = int(x)/int(y)
except Exception as e:
    print('Exception occured',e)
    z='None'
print("Division is: ",z)