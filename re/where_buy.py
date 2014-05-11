#coding=utf-8
import re

data =[ "从亚马逊买的,价格很实惠",
        "在京东买的，价格蛮实惠的"
        ]
data2 = ['this is good',
         'this is bad']
for d in data:
    m = re.search(r'(在|从).*买的', d)
    if m:
        print(m.group())
