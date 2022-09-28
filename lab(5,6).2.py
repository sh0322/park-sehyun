Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
prime_list = [2,3,5,7]
print('소수 목록 : ',prime_list)
prime_list.append(11)
print('추가 후 소수 목록 : ',prime_list)

prime_list = [2,3,5,7,11]
print('삭제 전 소수 목록 : ',prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 : ',prime_list)

nations = ['Korea','China','Russia','Malaysia']
print('국가 목록 : ',nations)
nations.append('Nepal')
print('추가 후 국가 목록 : ',nations)
SyntaxError: multiple statements found while compiling a single statement
prime_list = [2,3,5,7]
print('소수 목록 : ',prime_list)

SyntaxError: multiple statements found while compiling a single statement
a = [11,22]
prime_list = [2,3,5,7]

print('소수 목록 : ',prime_list)
소수 목록 :  [2, 3, 5, 7]
nations = ['Korea','China','Russia','Malaysia']
if (Japan in nations):
    print()
print('Japan은 국가목록에 없습니다')
SyntaxError: invalid syntax
if (Japan in nations):
    print()
print('Japan은 국가목록에 없습니다')
SyntaxError: invalid syntax
if (Japan in nations):
    print()
else:
    print('Japan은 국가목록에 없습니다')

    
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    if (Japan in nations):
NameError: name 'Japan' is not defined
if ('Japan' in nations):
    print()
else:
    print('Japan은 국가목록에 없습니다')

    
Japan은 국가목록에 없습니다
if ('Russia' in nations):
    print('Russia은 국가목록에 있습니다')
else:
    print('Japan은 국가목록에 없습니다')

    
Russia은 국가목록에 있습니다
prime_list = [2,3,5,7]
print('1에서 10까지의 소수',prime_list)
1에서 10까지의 소수 [2, 3, 5, 7]
1에서 10까지의 소수 [2, 3, 5, 7]
SyntaxError: invalid decimal literal
print('최솟값 : ',min(prime_list))
최솟값 :  2
print('최댓값 : ',max(prime_list))
최댓값 :  7
print('합계 : ',sum(prime_list))
합계 :  17
print('평균 : ',len(prime_list))
평균 :  4
nations = ['Korea','China','Russia','Malaysia']
print('국가 목록 : ',nations)
국가 목록 :  ['Korea', 'China', 'Russia', 'Malaysia']
print('사전에서 가장 먼저 나오는 나라 : 'min(nations))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('사전에서 가장 먼저 나오는 나라 : ',min(nations))
사전에서 가장 먼저 나오는 나라 :  China
print('사전에서 가장 뒤에 나오는 나라 : ',max(nations))
사전에서 가장 뒤에 나오는 나라 :  Russia
a = [1,2,3]
b = [10,20,30]
a.append(b)
a
[1, 2, 3, [10, 20, 30]]
a.extend(b)
a
[1, 2, 3, [10, 20, 30], 10, 20, 30]
a = [1,2,3]
b = [10,20,30]
SyntaxError: multiple statements found while compiling a single statement
a = [1,2,3]
b = [10,20,30]
a.extend(b)
a
SyntaxError: multiple statements found while compiling a single statement
a.extend(b)

a
[1, 2, 3, 10, 20, 30]
nlist = [1,2,3,4,5,6,7,8,9,10]
nlist.insert(0,0)
nlist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlist.reverse()
nlist
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nlist.pop(10)
0
print('마지막 원소 = ',nlist.pop(10))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print('마지막 원소 = ',nlist.pop(10))
IndexError: pop index out of range
nlist = [1,2,3,4,5,6,7,8,9,10]
nlist.insert(0,0)
nlist.reverse()
nlist.pop(10)
0
n;ist
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    n;ist
NameError: name 'n' is not defined
nlist
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
m = int(input('반복할 정수를 입력하시오 : "))
              
SyntaxError: unterminated string literal (detected at line 1)
m = int(input('반복할 정수를 입력하시오 : '))
              
반복할 정수를 입력하시오 : 3
list = [1,2,3]
              
list * m
              
[1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(15):
              n_list = [i]

              
n_list
              
[14]
n_list = []
              
for i in range(15):
              n_list.append()

              
Traceback (most recent call last):
  File "<pyshell#66>", line 2, in <module>
    n_list.append()
TypeError: list.append() takes exactly one argument (0 given)
for i in range(15):
              n_list.append(i)

              
n_list
              
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print('s_list1 = ',n_list(0:5))
              
SyntaxError: invalid syntax
print('s_list1 = ',n_list[0:5])
              
s_list1 =  [0, 1, 2, 3, 4]
print('s_list2 = ',n_list[5:11])
              
s_list2 =  [5, 6, 7, 8, 9, 10]
print('s_list3 = ',n_list[11:15])
              
s_list3 =  [11, 12, 13, 14]
print('s_list4 = ',n_list[2:11:2])
              
s_list4 =  [2, 4, 6, 8, 10]
print('s_list5 = ',n_list[-5:-10])
              
s_list5 =  []
print('s_list5 = ',n_list[-9:-4])
              
s_list5 =  [6, 7, 8, 9, 10]
print('s_list5 = ',n_list[-9:-4].reverse())
              
s_list5 =  None
n_list[-9:-4]
              
[6, 7, 8, 9, 10]
print('s_list5 = ',n_list.reverse())
              
s_list5 =  None
n_list.reverse()
              
n_list
              
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print('s_list5 = ',n_list[-4:-9])
              
s_list5 =  []
print('s_list5 = ',n_list[:-9])
              
s_list5 =  [0, 1, 2, 3, 4, 5]
print('s_list5 = ',n_list[:-5])
              
s_list5 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('s_list5 = ',n_list[-5:])
              
s_list5 =  [10, 11, 12, 13, 14]
print('s_list5 = ',n_list[-9:])
              
s_list5 =  [6, 7, 8, 9, 10, 11, 12, 13, 14]
print('s_list5 = ',n_list[-9:] - n_list[-4:])
              
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('s_list5 = ',n_list[-9:] - n_list[-4:])
TypeError: unsupported operand type(s) for -: 'list' and 'list'
n_list[-9:] - n_list[-4:]
              
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    n_list[-9:] - n_list[-4:]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
print('s_list5 = ',n_list[::-1])
              
s_list5 =  [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print('s_list5 = ',n_list[2:5:-1])
              
s_list5 =  []
print('s_list5 = ',n_list[-2:-9:-1])
              
s_list5 =  [13, 12, 11, 10, 9, 8, 7]
print('s_list5 = ',n_list[-5:-10:-1])
              
s_list5 =  [10, 9, 8, 7, 6]
print('s_list5 = ',n_list[-5:-15:-2])
              
s_list5 =  [10, 8, 6, 4, 2]
capital_dic = {'korea':'seoul','China':'Beijing','USA':'Washington DC'}
              
capital_dic['Korea']
              
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    capital_dic['Korea']
KeyError: 'Korea'
capital_dic[Korea]
              
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    capital_dic[Korea]
NameError: name 'Korea' is not defined
capital_dic = {'korea':'seoul'}
              
capital_dic = ['korea']
              

capital_dic = {'korea':'seoul'}
              
capital_dic['korea']
              
'seoul'
capital_dic = {'korea':'seoul','China':'Beijing','USA':'Washington DC'}
              
capital_dic['korea']
              
'seoul'
capital_dic['China']
              
'Beijing'
capital_dic['USA']
              
'Washington DC'
fruits_dic = {'apple':5000,'banana':4000,'grape':5300,'melon':6500}
              
print('apple의 가격은 ',fruits_dic['apple'],'원입니다.)
      
SyntaxError: unterminated string literal (detected at line 1)
print('apple의 가격은 ',fruits_dic['apple'],'원입니다.')
      
apple의 가격은  5000 원입니다.
print('banana의 가격은 ',fruits_dic['banana'],'원입니다.')
      
banana의 가격은  4000 원입니다.
print('grape의 가격은 ',fruits_dic['grape'],'원입니다.')
      
grape의 가격은  5300 원입니다.
print('melon의 가격은 ',fruits_dic['melon'],'원입니다.')
      
melon의 가격은  6500 원입니다.
person = {'이름':'홍길동','나이':26,'몸무게':82}
      
person['특기'] = '분신술'
      
person
      
{'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술'}
person['아버지'] = '홍판서ㅓ
      
SyntaxError: unterminated string literal (detected at line 1)
person['아버지'] = '홍판서'
      
person
      
{'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}
del.person['나이']
      
SyntaxError: invalid syntax
del person['나이']
      
person
      
{'이름': '홍길동', '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}
capital_dic = {'korea':'seoul','China':'Beijing','USA':'Washington DC'}
      
'Korea' in capital_dic
      
False
'China' in capital_dic
      
True
'korea' in capital_dic
      
True
'indonesia' in capital_dic
      
False
'Beijing' in capital_dic
      
False
'Beijing' in capital_dic
      
False
fruits_dic = {'apple':5000,'banana':4000,'grape':5300,'melon':6500}
      
fruits_dic = {'apple':5000,'melon':3000,'banana':5000,'orange':7000}
      
fruits_dic.keys()
      
dict_keys(['apple', 'melon', 'banana', 'orange'])
fruits_dic.values()
      
dict_values([5000, 3000, 5000, 7000])
fruits_dic.pop('apple')
      
5000
fruits_dic.clear()
      
fruits_dic
      
{}
fruits_dic = {'apple':6000,'melon':3000,'banana':5000,'orange':4000}
      
for key in fruits_dic:
      print(fruits_dic[key])

      
6000
3000
5000
4000
for key in fruits_dic:
      print(format(key,))

      
apple
melon
banana
orange
for key in fruits_dic:
      print('[ , ]'format(key))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for key in fruits_dic:
      print('[ , ]',format(key))

      
[ , ] apple
[ , ] melon
[ , ] banana
[ , ] orange
for key in fruits_dic:
      print('[ ,'format(key),' ]')
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for key in fruits_dic:
      print('[ ,',format(key),' ]')

      
[ , apple  ]
[ , melon  ]
[ , banana  ]
[ , orange  ]
list = []
      
for key in fruits_dic:
      list[key]

      
Traceback (most recent call last):
  File "<pyshell#154>", line 2, in <module>
    list[key]
TypeError: list indices must be integers or slices, not str
for key in fruits_dic:
      list[values]

      
Traceback (most recent call last):
  File "<pyshell#156>", line 2, in <module>
    list[values]
NameError: name 'values' is not defined
for key in fruits_dic:
      list[fruits_dic[key]]

      
Traceback (most recent call last):
  File "<pyshell#158>", line 2, in <module>
    list[fruits_dic[key]]
IndexError: list index out of range
for key in fruits_dic:
      list = [fruits_dic[key]]

      
list
      
[4000]
for key in fruits_dic:
      list.append(fruits_dic[key])

      
list
      
[4000, 6000, 3000, 5000, 4000]
list = []
      
for key in fruits_dic:
      list.append(key)

      
list
      
['apple', 'melon', 'banana', 'orange']
len(fruits_dic)
      
4
'apple' in fruits_dic:
      
SyntaxError: invalid syntax
'apple' in fruits_dic()
      
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    'apple' in fruits_dic()
TypeError: 'dict' object is not callable
'apple' in fruits_dic.keys()
      
True
if 'apple' in fruits_dic.keys():
      printf('okay')

      
Traceback (most recent call last):
  File "<pyshell#175>", line 2, in <module>
    printf('okay')
NameError: name 'printf' is not defined. Did you mean: 'print'?
if 'apple' in fruits_dic.keys():
      print('okay')

      
okay
t = (1919,3,1)
      
print(t[0],'년',t[1],'월',t[2],'일은 삼일절 입니다')
      
1919 년 3 월 1 일은 삼일절 입니다
month = t[0]
      
year = t[0]
      
month = t[1]
      
day = t[2]
      
print(year,'년',month,'월',day,'일은 삼일절 입니다')
      
1919 년 3 월 1 일은 삼일절 입니다
list = [10,20,30]
      
 = ()
      
SyntaxError: unexpected indent
t = ()
      
for i in 4:
      t = (list)

      
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    for i in 4:
TypeError: 'int' object is not iterable
for i in range(4):
      t = (list)

      
t
      
[10, 20, 30]
a = t[2]
      
b = t[1]
      
c = t[0]
      
print('a = ',a)
      
a =  30
print('b = ',b)
      
b =  20
print('c = ',c)
      
c =  10
person = ('홍길동',2019001,179)
      
person[1] = 2019003
      
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    person[1] = 2019003
TypeError: 'tuple' object does not support item assignment
list = list(person)
      
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    list = list(person)
TypeError: 'list' object is not callable
plist = list(person)
      
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    plist = list(person)
TypeError: 'list' object is not callable
person = ('홍길동',2019001,179)
      
plist = list(person)
      
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    plist = list(person)
TypeError: 'list' object is not callable
person = (1,2)
      
alist = list(person)
      
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    alist = list(person)
TypeError: 'list' object is not callable
person = ('홍길동',2019001,179)
      
plist = list(person)
...       
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    plist = list(person)
TypeError: 'list' object is not callable
>>> list = ['apple','mango','banana']
...       
>>> fset = set(list)
...       
>>> fset
...       
{'apple', 'banana', 'mango'}
>>> greet = 'Good afternoon'
...       
>>> s2 = set(greet)
...       
>>> s2
...       
{'n', 'f', 'e', 't', 'G', 'r', 'd', ' ', 'o', 'a'}
>>> s2 = set(greet)
...       
>>> s2
...       
{'n', 'f', 'e', 't', 'G', 'r', 'd', ' ', 'o', 'a'}
>>> s1 = {10,20,30,40}
...       
>>> s2 = {30,40,50,60,70}
...       
>>> s1 | s2
...       
{70, 40, 10, 50, 20, 60, 30}
>>> s1 & s2
...       
{40, 30}
>>> s1 - s2
...       
{10, 20}
>>> s1 ^ s2
...       
{50, 20, 70, 10, 60}
>>> s1.issubset(s2)
...       
False
>>> s1.issuperset(s2)
...       
False
>>> s1.isdisjioint(s2)
...       
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    s1.isdisjioint(s2)
AttributeError: 'set' object has no attribute 'isdisjioint'. Did you mean: 'isdisjoint'?
>>> s1.isdisjoint(s2)
...       
False
