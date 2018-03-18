#!/usr/bin/python3

# age = input('please enter you age: ')
# age = int(age)
# if age >= 18 :
# 	print('your age is' , age)
# 	print('adult')
# elif age >= 12 :
# 	print('teenanger...')
# else :
# 	print('baby...')

# for ... in ...

# tennis_player = ['Roger', 'Rafa', 'Stan']
# for a in tennis_player :
# 	print(a)


# sum = 0
# for a in list(range(100)) :
# 	sum += a;
# print(sum)


# while ...

# sum = 0
# i = 99
# while i > 0 :
# 	sum += i
# 	i = i - 2
# print(sum)


# dict

# d = {'Roger':20, 'Rafa': 16, 'Stan': 2}
# d['Roger'] = 21
# print('Tomas' in d)
# print(d.get('Tomas'))
# print(d.get('Tomas', -1))
# print(d['Roger'])


# set

# s1 = set([1, 2, 3])
# s1.add(4)
# s1.remove(2)
# s2 = set([3, 4, 5, 6])

# syu = s1 & s2
# shuo = s1 | s2

# print(syu)
# print(shuo)


# function

def my_abs(x):
	if x > 0 :
		return	x
	else :
		return -x

def nop() :
	pass

if age > 18 :
	pass


def move(x, y, step, angle = 0) :
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

import math

def keyofabc(a, b, c) :
	if a == 0 :
		print('a should be zero...')
	elif b*b - 4*a*c < 0 :
		print('no key for this equation...')
	elif b*b - 4*a*c == 0 :
		print('there is two equal key of the equation')
		print('key is', -b/2/a)
	else :
		print('there is two key of the equation')
		print('key is', (-b - math.sqrt(b*b-4*a*c))/(2*a), (-b + math.sqrt(b*b-4*a*c))/(2*a))


function par

def add_end(l = None) :
	if l is None :
		l = []
	l.append('END')
	return l

def cal(*number) :
	sum = 0
	for x in number :
		sum += x*x
	return sum


def person(name, age, **kw):
	print('name', name, 'age', age, 'other', kw)


def person(name, age, *, city, job):
	print('name:', name, 'age:', age, 'city:', city, 'job:', job)


def product(*num) :
	ans = 1;
	for x in num :
		ans *= x
	return ans


qiepian

def trim(s) :
	while s[:1] == ' ' :
		s = s[1:]
	while s[-1:] == ' ' :
		s = s[:-1]
	return s


iter

def findMinAndMax(l) :
	if len(l) == 0 :
		return None, None
	else :
		vmax = l[0]
		vmin = l[0]
		for x in l :
			if x > vmax :
				vmax = x
			if x < vmin :
				vmin = x
		return vmin, vmax




L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


rabbit

def fib(max) :
	n, a, b = 0, 0, 1
	while n < max :
		yield b
		a, b = b, a+b
		n += 1
	return 'done'	


triangles

import copy
def triangles(max) :
	n = 1
	l1, l2 = [1], [1]
	if max == 0 :
		print('par must greater than zero...')
		return
	if n == 1 :
		yield [1]
		n += 1
	while n <= max :
		l1.append(0)
		l2.insert(0, 0)
		l = [l1[i] + l2[i] for i in range(n)]
		yield l
		l1 = copy.deepcopy(l)
		l2 = copy.deepcopy(l)
		n += 1
	return 



isinstance(object, Iterable)
isinstance(object, Iterator)


def add(x, y, f) :
	return f(x) + f(y)


def char2nums(x, y) :
	return 10 * int(x) + int(y)

def fn(x, y) :
	return 10*x + y

def char2nums(s) :
	digital = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	for ch in s :
		return digital[ch]

from functools import reduce
def str2int(s):
	DIGITAL = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

	def fn(x, y):
		return 10*x + y

	def char2nums(ch) :
		return DIGITAL[ch]

	return reduce(fn, map(char2nums, s))


def normalize(l):
	def nor(s):
		s = s.casefold()
		s = s.capitalize()
		return s
	return list(map(nor, l))

from functools import reduce
def prod(l):
	def tim(x ,y):
		return x*y
	return reduce(tim, l)



def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列


# huishu

def is_palindrome(x):
	l1 = list(str(x))
	l2 = list(str(x))
	l2.reverse()
	return l1 == l2


sorted
def by_name(d):
	return d[0]

def by_score(d):
	return d[1]


sum 

def later_cal_sum(*argv):
	def cal_sum():
		s = 0
		for x in argv:
			s += x
		return s
	return cal_sum


# count

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs


def createCounter():
	j = 0
	def tmp(j):
		def counter():
			j += 1
			return j
		return counter
	return tmp(j)


def createCounter():
	i=[0]
	def counter():
		i[0]+=1
		return i[0]
	return counter



decorator

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		func(*args, **kw)
		return 
	return wrapper

@log
def now():
	print('2018-2-6')

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s call %s()' % (text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2018-2-6')
















