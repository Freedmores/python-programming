# with open("./data/input.txt","a") as f:
#     f.write('6,8')
#     f.write('\n7,6')
#     f.write('\n2,8')
#     f.write('\n9,5')
#     f.write('\n9,6')
list_of_numbers =[]
with open("./data/input.txt","r") as f:
    line = f.read().split('\n')
# print(line)

for item in line:
    print('The sum of,',item[0],'&',item[2],'is',str(int(item[0])+int(item[2])))
    list_of_numbers=list_of_numbers + item.split(',')

# get count for each number
print('\n.... count of each number ....')
list_of_unique_numbers = set(list_of_numbers)
dictNumbers ={}
def countNum():
    for num in list_of_unique_numbers:
        dictNumbers[num]=0
        for i in list_of_numbers:
            if num==i:
                dictNumbers[num]=dictNumbers[num]+1
    for k,v in dictNumbers.items():
        print(k,':',v)
countNum()