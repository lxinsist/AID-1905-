"""
regex.py re模块 功能函数演示
"""
import  re

#目标字符串
s="Alex:1994,sunny:1996,hah:2008"
pattern=r"\w+:\d+"  #正则表达式
pattern2=r"(\w+:)\d+"
pattern3=r"\w+:(\d+)"  #只能匹配子组内容
pattern4=r"(\w+:)(\d+)"  #正则表达式
pattern5=r"((\w+:)(\d+))"  #正则表达式
#re模块调用 findall
l1=re.findall(pattern,s)#返回的是匹配的内容列表,如果正则表达式有子组则只能获取到
# 子组对应的内容,当出现多个子组的时候,每个子组都取一个,组成一个元组,
l2=re.findall(pattern2,s)
l3=re.findall(pattern3,s)
l4=re.findall(pattern4,s)
l5=re.findall(pattern5,s)
# 无法获取整体的内容
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

#通过compile 对象调用findall
regex=re.compile(pattern)
l=regex.findall(s,2,17)#(2,17指的是取目标字符串的第三个到第17个作为新的字符串,再按正则表达式进行匹配)
print(l)

# 按照正则表达式匹配内容切割字符串,返回切割后的内容列表
l=re.split(r"[:]",s)
print(l)

#替换目目标字符串
s=re.sub(r":","-",s,1)
print(s)