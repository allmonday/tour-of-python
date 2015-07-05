import re
input_str = '''are <br>\n  <br> hello wdalsdf <br><br><br>  line2 <br>  <br>  <br>'''

input_str = re.sub('<br>\s+', '<br>', input_str)
result = re.sub('(<br>){2,}', '<br><br>', input_str)
print result

