num=input("Enter a number: ")
num=int(num)
if num%2 ==0:
    print("Number is even")
else:
    print('Number is odd')

indian=['samosa','daal','naan']
chinese=['egg role','pot sticker','fried ride']
italian=['pasta','pizza','risotto']

dish = input('Enter a dish name:')

if dish in indian:
    print("indian")
elif dish in chinese:
    print('Chinese')
elif dish in italian:
    print("Italian")
else:
    print("Based on the little knowledge i have, i don't know which cuisine is ", dish)