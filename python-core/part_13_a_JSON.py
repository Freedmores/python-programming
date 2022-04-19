book = {}

book['tom'] = {
    'name':'tom',
    'address':'1 red street, NY',
    'phone':78765645
}

book['bob'] = {
    'name':'bob',
    'address':'1 green street, NY',
    'phone':76456734
}

import json
s = json.dumps(book)
print(s)

with open("./data/book.txt",'w') as f:
    f.write(s)