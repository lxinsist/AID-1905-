"""
前情回顾
1.什么是正则表达式:普通字符和元字符构成的字符串,描述一类字符串规则
2.元字符:有特殊含义的符号
3.元字符:|
"""

# import re
# f=re.findall("^Jame","jame,hello")#1
# print(f)
# f=re.findall("^Jame","jame,hello")#2
# print(f)
# f=re.findall("^Jame","jame,hello")#3
# print(f)
# f=re.findall("^Jame","jame,hello")#4
# print(f)
# f=re.findall("^Jame","jame,hello")#5
# print(f)
# f=re.findall("^Jame","jame,hello")#6
# print(f)
# f=re.findall("^Jame","jame,hello")#7
# print(f)
# f=re.findall("^Jame","jame,hello")#8
# print(f)
# f=re.findall("^Jame","jame,hello")#9
# print(f)
# f=re.findall("^Jame","jame,hello")#10
# print(f)
# f=re.findall("^Jame","jame,hello")#6
# print(f)
# A12=re.findall("^Jame$","jame")#绝对匹配(必须只有中间的才能匹配到)
# print(A12)
# A13=re.findall('wo*',"wooooo~~w!")#匹配前面的字符出现0次或多次
# print(A13)#["Wooooo","w"]只是w,表示0次(没有o);wo表示一次(第一次有o),*只作用于前面一个字符,只是对规则的表述
# A14=re.findall("[a-zA-Z]*","How are yue?")
# print(A14)
# A14=re.findall("[A-Z][a-z]*","How are yue?")#匹配大写字母开头的单词
# print(A14)#"How
# A20=re.findall("-?[0-9]+","-28 27")
# A21=re.findall("[^ ]+","ab cd ef")#除空格外的所有字符串,以空格分开
# s="[hqg],[cqz],[lzcq]"
# A30=re.findall(r"\[.+?\]",s)
# 练习1
# 1.匹配一个.com的邮箱格式字符串
# 2.匹配一个密码 8-12位数字字母下划线
# 3.匹配一个数字 正数,负数,整数,小数 分数1/2,百分数45%
# 4.匹配一段文字中以大写字母开头的单词,注意文字中可能有 iPython(不算)  H-base(算)
#    单词可能有 大写字母 小写字母
import re
a="li@163.com"
b="8875_41aA_1142"
c="14 -13 18 1.43 1/2 45%"
d="Hollw iPython H-base ABC"

A31=re.findall(r"\w+@\w+\.com",a)
B31=re.findall(r"\w{8,12}",b)
C31=re.findall(r"-?\d+/?\.?\d*%?",c)#可能有可能没有(一个),加?
D31=re.findall(r"\b[A-Z][-_a-zA-Z]*",d)#以大写开头
print(A31)
print(B31)
print(C31)
print(D31)
e="51382119920420489X"
E=re.findall("\d{17}[0-9A-Z]",e)
print(E)