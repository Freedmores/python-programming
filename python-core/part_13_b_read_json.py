f=open("./data/book.txt", "r")
s=f.read()
print(s)

import json
book = json.loads(s)
print(type(book))
index =1

for name,infor in book.items():
    print("Record:", index)
    print('-----------------')
    for k, v in infor.items():
        print(k,':',v)
    index = index+1
    print('\n')
