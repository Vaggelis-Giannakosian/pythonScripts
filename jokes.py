from typing import TextIO

import pyjokes
import datetime
from collections import Counter, defaultdict, OrderedDict


li = [1,2,3,4,5,6,7,7,7,7,7]
countObj = Counter(li)

print(countObj[li[len(li)-1]])
# print(Counter())

print(datetime.datetime(2012,10,28,17,30,12))
print(datetime.datetime.today())


print(pyjokes.get_joke('en' , 'adult'))

with open('C:/Users/Lostre/PycharmProjects/modules/aaa/sample.txt', encoding='UTF-8', mode='r+') as sample:
    sample.write('halloooooo \n')
    print(sample.readlines())
    sample.seek(0)
    print(sample.read())
