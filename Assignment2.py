'''
1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
'''

def myreduce(function, dataset):

    a = dataset[0]
    for i in dataset[1:]:
        a = function(a, i)
    return a

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def do_sum(x,y):
    return x+y

print(myreduce(do_sum,dataset))

'''
1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
'''
def myfilter(function, dataset):
    a = []
    for i in dataset:
        if function(i):
            a.append(i)
    return a

def is_positive(b):
    if b > 0:
        return True
    else:
        return False

dataset=[-3, -5, 1, 5, 6, 8]

print(myfilter(is_positive, dataset))


'''
Implement List comprehensions to produce the following lists. 
 
Write List comprehensions to produce the following Lists 
A. ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 
'''
str_value='ACADGILD'

value = [X for X in str_value]
print(value)

'''
B. ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
'''
list_value=['x', 'y', 'z']

result = [i*j for i in list_value for j in range(1, 5)]
print(result)


'''
C. ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] 
'''
list_value=['x', 'y', 'z']

result = [j*i for j in range(1, 5) for i in list_value]
print(result)


'''
D. [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
'''

list_value = [2,3,4]
result = [[i+j] for i in list_value for j in range(0,3)]
print(result)


'''
E. [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
'''

list_value = [2,3,4,5]
result = [[i+j for i in list_value] for j in range(0,4)]
print(result)

'''
F. [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 
'''

list_value = [1, 2, 3]
result = [(j, i) for i in list_value for j in range(1, 4)]
print(result)


'''
3. Implement a function longestWord() that takes a list of words and returns the longest one.
'''

def longestword(list_of_words):
    a = []
    for i in list_of_words:
        a.append((len(i), i))
    a.sort()
    return a[-1][1]

list_of_words=['Python', 'smalleragain', 'longest']

print(longestword(list_of_words))

'''
Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
 area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
Function to take the length of the sides of triangle from user
should be defined in the parent class and function to calculate the area should be defined in subclass.
'''
class triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class area_calc(triangle):
    def __init__(self, *args):
        super(area_calc, self).__init__(*args)


    def cal_area(self):
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

ta = area_calc(6, 3, 6)
print(ta.cal_area())

'''
 1.2 Write a function filter_long_words() that takes a list of words and an integer n 
 and returns the list of words that are longer than n
'''
def filter_long_words(list_of_words, n):
    a = []
    for i in list_of_words:
        if len(i)>n:
            a.append(i)
    return a

list_of_words=['Python', 'Java', 'Selenium', 'API testing']

print(filter_long_words(list_of_words, 4))


'''
 2.1 Write a Python program using function concept that maps  list of words into a list of
  integers representing the lengths of the corresponding words​. 
 Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] 
 Here 2,3 and 4 are the lengths of the words in the list. 
'''
def map_fun(list_of_words):
    a = []
    for i in list_of_words:
        a.append(len(i))
    return a

list_of_words = ['ab', 'cde', 'erty']

print(map_fun(list_of_words))

'''
2.2 Write a Python function which takes a character (i.e. a string of length 1) and 
returns True if it is a vowel, False otherwise. 
'''
def vowel_check(char_letter):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if char_letter in vowel:
        return True
    else:
        return False
print(vowel_check('o'))


