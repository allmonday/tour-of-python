#coding: utf-8
import re
input_str = '''<br/>  <br><br>KPMG Chinas Public Policy and Regulatory Affairs Unit P'''

input_str = re.sub(r'(<br>|<br\/>)\s+', '<br>', input_str)
print input_str
result = re.sub('(<br>){2,}', '<br>'*2, input_str)
print(result)

