#제어문
#조건문
score = 100
if score<=100 and score>=85 : grade="우수"
elif score<=84 and score>=70 : grade="보통"
else : grade="부족"
print(grade)

num=9
result=0
if(num>6):
    result=num*2
else:
    result=num+2
print(result)
    
print(num*2 if num>6 else num+2)
#반복문
#while문
cnt=tot=0
datalst=[]
while cnt<5:
    cnt+=1
    tot+=cnt
    datalst.append(cnt)
    print(cnt,tot)
print(datalst)


numbers = []  # 4의 배수를 저장할 리스트
sum_of_numbers = 0  # 4의 배수들의 합을 저장할 변수

for i in range(1, 101):
    if i % 4 == 0:  # 4의 배수인 경우
        numbers.append(i)  # 리스트에 추가
        sum_of_numbers += i  # 합을 구하기 위해 변수에 더함
        
print("4의 배수들:", numbers)
print("4의 배수들의 합:", sum_of_numbers)


i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==6:
        break
    print(i,end=' ')
    
    
    
#for문
string='abcdefg'
print(len(string))
for s in string:
    print(s)
    
lst=[1,2,3,4,5,6,7]
for e in lst:
    print(e,end=' ')
print()    
print(range(10))
for e in range(10):
    print(e,end=' ')
print()     
for e in range(1,10,2):
    print(e,end=' ')
print()

lst=['A','B','C'] 
if 'D' in lst:
    print("Ok")
else :
    print('No')