#기본 자료형
#리터럴 상수(Scaler data type)-int, float, bool, None
#리스트(list), 튜플(tuple),딕션너리(dictionary),접합(set)

var1 = "Hello python"
print(var1)
print(type(var1))

var1 = 100
print(var1)
print(type(var1))

var1 = 123.23
print(var1)
print(type(var1))

var1=True
print(var1)
print(type(var1))

#자료형 변환(casting)
a = 10.5
b = 20.14
c=int(True)
d=int(False)
sum = a+b
print('합계',sum)
print('합계',int(sum))
print(int(True),int(False))
str='2'
print(int(str)**4)
#print(str**3)

#문자열
# 따옴표(',')(",")('''........''')
oneLine = 'abcdefghijklmnopqrstuvwxyz'
print(oneLine)
oneLine = "abcdefghijklmnopqrstuvwxyz"
print(oneLine)
multiLine = '''abcd
efghijkl
mnopqrsty
vwxyz'''
print(multiLine)
multiLine="abcdefg\nhijklmn\nopqrstuvwxyz"
print(multiLine)

input="나는 문어~ 꿈을 꾸는 문어~"
print(input[0:6])
print(input[-1])
print('python'+"application")
print('python'+repr(3.0))