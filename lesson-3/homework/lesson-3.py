### Container Types Intro
Container/Reference Types:

- 'list'
- 'tuple'
- 'dictionary'
- 'set'

fruits = ['apple', 'cherry', 'banana']
type(fruits)

numbers = [1, 4, 6, 7]
print(numbers)
type(numbers)
mixed = ['apple', 1, True]
print(mixed)
list([1, 2])

list('abcd')

my_str = 'ab,cd'
my_str.split(",")
a = 5
b = a
a += 1 # a = a + 1
print(a)
print(b)
a = [1, 2, 3]
b = a
a.append(4)
print(a)
print(b)
a = [1, 2, 3]
a.append(4)
a.append(5)
print(a)



a = [1, 2, 3]
b = a.copy()
print(id(a))
print(id(b))


x = [1, 'da']
x = [3, 4]
x[0:2]
x = [
    [1, 'da'],
    [3, 4]
    ]
x
x = [
    [1, 2],
    [3, 4]
    ]
y = x.copy()
x[0].append(5)
print(x)
print(y)
from copy import deepcopy
a = 1
x = [
    [1, 2],
    [3, 4]
    ]
y = deepcopy(x)
x[0].append(5)
print(x)
print(y)
### List Methods
- append()
- clear()
- copy()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reserve()
- sort()


fruits = ['apple', 'banana', 'apple']
fruits.append('cherry')
fruits

fruits.clear()
fruits
fruits.copy()
fruits
fruits.count('apple')

fruits.extend(['melon', 'ananas'])
fruits
fruits.append(['melon', 'ananas'])
fruits
fruits.index('ananas',0)

fruits.index('ananas',1)
fruits.pop()
fruits
fruits.pop()
fruits.pop()
fruits
fruits.remove(fruits[3])
fruits.remove('apple')
fruits
#fruits.remove(fruits[0])
#fruits
#fruits.reverse() # in-place reverse  
fruits
fruits.sort()
fruits
fruits = ['banan', 'a', 'ananas', 'ab']
sorted(fruits, key=lambda x: len(x)) 
numbers = [-6, 4, 3, 2, 7]
sorted(numbers, key=lambda r: abs(r))
numbers
numbers[0] = 1
numbers 
l = [1, True, 'apple', None, 5.6]
l
### Tuple

a = (1, 2, 3)
type(a)
len(a)
b = (1,)
type(b)
a[0:1]
append,sort,pop,remove,extend,reverse,insert = mutate
index,count
copy,
person1 = ('John', 'Doe', 40)
grades = [40, 50, 70]
### Dictionary
person = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
  }
type(person)
person.keys()
person.values()
person.items()

dict([('name', 'John'), ('email', 'john@gmail.com'),('age', 50)])
dict(name='Adam', age=40)
person['lname'] = 'Doe'
person

{
   1: "dfs", 
   True: 'adfg'
}

k1 = 1
k2 = False
k3 = 'keys'
k4 = (1, 2, 3)

d1 = {
    k1: 'a',
    k2: 'ab',
    k3: 'abc',
    k4: 'abcd'
 }
d1

d1[(1, 2, 3)]
hash((1, 2))
print(hash((1, 23, 65, 6, 7, 45, 4)))
print(hash((1, 23, 65, 6, 4, 45, 4)))

(1, 23, 65, 6, 7, 45, 4) ==(1, 23, 65, 6, 7, 45, 4)
a1 = {
 'a': 1,
 'b': 2     
}

a1 = {
    'a': 1,
    'b': 2
}

a1.update({'c': 3, 'a': 5})

a1
### SET
letters = {'a', 'b', 'c', 'd',}
type(letters)
a = {'a', 'b', 'c', 'd', 'a', 'a', 'b'}
list(set(a))
for i in letters:
 print(i)
 
     
s1 = {'a', 'b', 'c'}
s2 = {'r', 'a', 'b'}
s1.union(s2)
s1 | s2
s1.difference(s2)
s1 - s2
s1.symmetric_difference(s2)
s1 ^ s2
'apple' in ['apple', 'banana', 'cherry']
### Namedtuple
from collections import namedtuple

# RGB = (200, 100, 230)

Color = namedtuple("Color", ['x', 'y', 'z'])

white = Color(255, 255, 255)
black = Color(0, 0, 0)
green = Color(0, 255,0)
green[1]
type(green)
isinstance(green, tuple)
isinstance(green, list)
person['name']
