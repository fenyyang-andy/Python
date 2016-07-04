#!usr/bin/env python
#coding:utf-8

#--------------------------------------------------------------

# class RoundFloat(object):
# 	def __init__(self,val):
# 		assert isinstance(val,float),"value must be a float."
# 		self.value = round(val,2)

# 	def __str__(self):
# 		return "{:.2f}".format(self.value)

# 		__repr__ == __str__  #在类被调用，即向变量提供__str__()里的内容。

# if __name__ == '__main__':
# 	r = RoundFloat(2.185)
# 	print r
# 	print type(r)

#--------------------------------------------------------------
# class Fraction(object):
# 	def __init__(self,number,denom):
# 		self.number = number 
# 		self.denom = denom

# 	def __str__(self):
# 		return str(self.number) + '/' + str(self.denom)

# 		__repr__ == __str__

# if __name__ == '__main__':
# 	f = Fraction(2,3)
# 	print f

#----------------------------------------------------------

# def gcd(a,b):
# 	if not a > b:
# 		a,b = b,a
# 	while b != 0:
# 		remainder = a % b
# 		a,b = b,remainder
# 	return a

# def lcm(a,b):
# 	return (a * b)/gcd(a,b)

# if __name__ == '__main__':
# 	print gcd(8,20)
# 	print lcm(8,20)


#--------------------------------------------------------
# def gcd(a,b):
# 	if not a > b:
# 		a,b = b,a
# 	while b != 0:
# 		remainder = a % b
# 		a,b = b,remainder
# 	return a

# def lcm(a,b):
# 	return (a * b)/gcd(a,b)

# class Fraction(object):
# 	def __init__(self,number,denom):
# 		self.number = number 
# 		self.denom = denom

# 	def __str__(self):
# 		return str(self.number) + '/' + str(self.denom)

# 		__repr__ == __str__

# 	def __add__(self,o  ther):
# 		lcm_num = lcm(self.denom,other.denom)
# 		number_sum = (lcm_num / self.denom * self.number) +(lcm_num /other.denom * other.number)
# 		return Fraction(number_sum,lcm_num)

# if __name__ == '__main__':
# 	m = Fraction(1,3)
# 	n = Fraction(1,2)
# 	s = m + n
# 	print m,"+",n,"=",s

#--------------------------------------------------------------------------------------------------

# class RoundFloat(object):
# 	def __init__(self,val):
# 		assert isinstance(val,float),"value must be a float"
# 		self.value = round(val,2)

# 	def __str__(self):
# 		return "{:.2f}".format(self.value)

# 		__repr__ = __str__  #在类被调用，即向变量提供__str__()里的内容

# if __name__ == '__main__':
# 	r = RoundFloat(2.1333)
# 	print r
# 	print type(r)
#---------------------------------------------------

# """
# study __getattr__ and __setattr__
# """

# class Rectangle(object):
# 	"""
# 	the width and length of Rectangle
# 	"""

# 	def __init__(self):
# 		self.width = 0
# 		self.length = 0

# 	def setSize(self,size):
# 		self.width,self.length = size
# 	def getSize(self):
# 		return self.width,self.length

# 		size = property(getSize,setSize)


# if __name__ == '__main__':
# 	r = Rectangle()
# 	r.width = 3
# 	r.length = 4
# 	print r.getSize()
# 	r.size = 30,40
# 	print r.width
# 	print r.length
#-------------------------------------------------------

# class NewRectangle(object):
# 	def __init__(self):
# 		self.width = 0
# 		self.length = 0

# 	def __setattr__(self,name,value):
# 		if name == "size":
# 			self.width,self.length = value
# 		else:
# 			self.__dict__[name] = value

# 	def __getattr__(self,name):
# 		if name == "size":
# 			return self.width,self.length
# 		else:
# 			raise AttibuteError

# if __name__ == '__main__':
# 	r = NewRectangle()
# 	r.width = 3
# 	r.length = 4
# 	print r.size
# 	r.size = 30,40
# 	print r.width
# 	print r.length

#-------------------------------------------------------	

# """
# the interator as range()
# """

# class MyRange(object):
# 	def __init__(self,n):
# 		self.i = 1
# 		self.n = n

# 	def __iter__(self):
# 		return self 

# 	def next(self):
# 		if self.i <= self.n:
# 			i = self.i
# 			self.i += 1
# 			return i 
# 		else:
# 			raise StopIteration()

# if __name__ == '__main__':
# 	x = MyRange(7)
# 	print [i for i in x]

#------------------------------------------------------

# """
# compute Fibonacci by iterator
# """
# class Fibs(object):
# 	def __init__(self,max):
# 		self.max = max
# 		self.a = 0
# 		self.b = 1

# 	def __iter__(self):
# 		return self

# 	def next(self):
# 		fib = self.a 
# 		if fib > self.max:
# 			raise StopIteration
# 		# else:
# 		self.a,self.b = self.b,self.a + self.b
# 		return fib

# if __name__ == '__main__':
# 	fibs = Fibs(5)
# 	print list(fibs)
#------------------------------------------------------

# while 1:
# 	print "this is a division program."
# 	c = raw_input("input 'c' continue,otherwise logout:")
# 	if c == 'c':
# 		a = raw_input("first number:")
# 		b = raw_input("second number:")
# 		try:
# 			print float(a)/(b)
# 			print "********************"
# 		except ZeroDivisionError:
# 			print "**************************"
# 		except ValueError:
# 			print "please input number."
# 			print "************************"

# 	else:
# 		break
##------------------------------------------------------

# class Calculator(object):
# 	is_raise = False
# 	def calc(self,express):
# 		try:
# 			return eval(express)
# 		except ZeroDivisionError:
# 			if self.is_raise:
# 				print "Zero can not be division."
# 			else:
# 				raise
# if __name__ == '__main__':
# 	c = Calculator()
# 	c.is_raise = True
# 	print c.calc("8/0")

##------------------------------------------------------

# class Person(object):
# 	def speak(self):
# 		print "I love u"

# 	def setHeight(self):
# 		print "The height is:1.60m"

# 	def breast(self,n):
# 		print "My breast is:",n

# class Girl(Person):
# 	def setHeight(self):
# 		print "The height is:1.70m"

# if __name__ == '__main__':
# 	cang = Girl()
# 	cang.setHeight()
# 	cang.speak()
# 	cang.breast(90)

##---------------------------------------------

# class Person(object):
# 	def eye(self):
# 		print "Two eyes"

# 	def breast(self,n):
# 		print "The breast is:",n

# class Girl(object):
# 	age = 28
# 	def color(self):
# 		print "The girl is white"

# class HotGirl(Person,Girl):
# 	pass

# if __name__ == '__main__':
# 	kong = HotGirl()
# 	kong.eye()
# 	kong.breast(90)
# 	kong.color()
# 	print kong.age

##-------------------------------------------------
# class Person(object):
# 	def __init__(self):
# 		self.height = 160

# 	def about(self,name):
# 		print "{} is about {}".format(name,self.height)

# class Girl(Person):
# 	def __init__(self):
# 		super(Girl,self).__init__()
# 		self.breast = 90

# 	def about(self,name):
# 		print "{} is a hot girl,she is about {},and her breast is {}".format(name,self.height,self.breast)
# 		super(Girl,self).about(name)

# if __name__ == '__main__':
# 		cang = Girl()
# 		cang.about("canglaoshi")		

##------------------------------------------------------

# class Person(object):
# 	def __init__(self):
# 		self.height = 160

# 	def about(self,name):
# 		print "{} is about {}".format(name,self.height)

# class Girl(Person):
# 	def __init__(self):
# 		super(Girl,self).__init__()
# 		self.breast = 90

# 	def about(self,name):
# 		print "{} is a hot girl,she is about{}, and her breast is {}".format(name,self.height,self.breast)
# 		super(Girl,self).about(name)


# if __name__ == '__main__':
# 	cang = Girl()
# 	cang.about("canglaoshi")

##---------------------------------------------------------
# __metaclass__ = type

# class StaticMethod:
# 	@staticmethod
# 	def foo():
# 		print "This is a static method foo()."

# class ClassMethod:
# 	@classmethod
# 	def bar(cls):
# 		print "This is class method bar()."
# 		print "bar() is part of class:",cls.__name__

# if __name__ == '__main__':
# 	static_foo = StaticMethod()
# 	static_foo.foo()
# 	StaticMethod.foo()
# 	print  "******************"
# 	class_bar = ClassMethod()
# 	class_bar.bar()
# 	ClassMethod.bar()


##---------------------------------------------------------
# class Animal(object):
# 	def __init__(self,name=""):
# 		self.name =name
# 	def talk(self):
# 		print "Meow"

# class Cat(Animal):
# 	def talk(self):
# 		print "Meow"

# class Dog(Animal):
# 	def talk(self):
# 		print "woof"
# a = Animal()
# a.talk()
# c = Cat("Missy")
# c.talk()
# d = Dog("Rocky")
# d.talk()


##---------------------------------------------------------
# class ProtectMe(object):
# 	def __init__(self):
# 		self.me = "qiwsir"
# 		self.__name = "kivi"

# 	def __python(self):
# 		print "I love python"

# 	def code(self):
# 		print "which language do you like?"
# 		self.__python
# if __name__ == '__main__':
# 	p = ProtectMe()
# 	p.code()
# 	p.__python()

##---------------------------------------------------------

class ProtectMe(object):
	def __init__(self):
		self.me = "qiwsir"
		self.__name = "kivi"

	@property
	def name(self):
		return self.__name

if __name__ == '__main__':
	p = ProtectMe()
	print p.name