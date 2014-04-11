#encoding=utf-8
from pyquery import PyQuery
snippet = '''html><ul> <li>
<a href="baidu.com">food</a> ">"
<a href="baidu.com">wine</a> ">"
<a href="baidu.com">beer</a>
</li> <li>
<a href="baidu.com">food</a> ">"
<a href="baidu.com">wine</a> ">"
<a href="baidu.com">present</a>
</li> </ul></html>'''

pq_obj = PyQuery(snippet)
print pq_obj('li')[0][-1].text_content()
print len(pq_obj('li')[0])#[-1].text_content()
