"""
flags.py
flags 扩张功能演示
"""
import re
s="""Hello
北京
"""

#只能匹配ASKII编码 A
# regex=re.compile(r"\w+",flags=re.A)#A只匹配ASKII码

#不区分大小写 I
# regex=re.compile(r"[a-z]+",flags=re.I)#I不区分大小写

#.可以匹配换行 S
# regex=re.compile(r".+",flags=re.S)#(.本来不能支持换行)

#^,$ 匹配每一行的开头结尾位置 M
# regex=re.compile(r"^北京",flags=re.M)

regex=re.compile(pattern,flags=re.X)
l=regex.findall(s)
print(l)