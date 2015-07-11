#coding:utf-8
import re
input_str = r'''\1. 21\r\n \2. togod  \3.weldone'''

result = re.sub(r'\\(\d)', '·\g<1>. ', input_str)
print result
