Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list = [10,20,30,50,60]
for i in range(5):
    m = m + list[i]

    
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    m = m + list[i]
NameError: name 'm' is not defined
int m = 0
SyntaxError: invalid syntax
m = 0
for i in range(5):
    m = m + list[i]

    
m
170
n = 0
m = 0
for i in range(5):
    if m > n:
        n = m

        
n
0
for i in range(5):
    if list[i] > list[i+1]:
        n = list[i]

        
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    if list[i] > list[i+1]:
IndexError: list index out of range
n = list[0]
for i in range(5):
    if list[i] >= n:
        n = list[i]

        
n
60
a = [2,3,,4,5,6]
SyntaxError: invalid syntax
a = [2,3,4,5,6]
list1 = [3,5,7]
list2 = [2,3,4,5,6]
for i in range(3)
SyntaxError: expected ':'
for i in range(3):
    for j in range(5):
        print(i, '*' ,j '=',i*j)
        
SyntaxError: invalid syntax
for i in range(3):
    for j in range(5):
        print(i, '*' ,j ,'=',list1[i] * list2[j])

        
0 * 0 = 6
0 * 1 = 9
0 * 2 = 12
0 * 3 = 15
0 * 4 = 18
1 * 0 = 10
1 * 1 = 15
1 * 2 = 20
1 * 3 = 25
1 * 4 = 30
2 * 0 = 14
2 * 1 = 21
2 * 2 = 28
2 * 3 = 35
2 * 4 = 42
for i in range(3):
    for j in range(5):
        print(list1[i], '*' ,list2[j] ,'=',list1[i] * list2[j])

        
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
>>> src = 'a2b3c6a2c3f1g1'
>>> n = int(input('n을 입력하세요:'))
n을 입력하세요:3
>>> list = []
>>> a, b, c= input('3개의 수를 입력하세요: ').split()
3개의 수를 입력하세요: 1 2 3
>>> list[0] = max(a,b,c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list[0] = max(a,b,c)
IndexError: list assignment index out of range
>>> lista = []
>>> lista = [a,b,c]
>>> list[0] = max(lista)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list[0] = max(lista)
IndexError: list assignment index out of range
>>> lista[0] = a
>>> lista[1] = b
>>> lissta[2] = c
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    lissta[2] = c
NameError: name 'lissta' is not defined. Did you mean: 'lista'?
>>> max(lista)
'3'
