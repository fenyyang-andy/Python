#coding:utf-8

"""
ex3 注释和井号
"""
# print "I will now count my chickens:"

# print "Hens",25 + 30 / 6
# print "Roosters", 100 - 25 * 3 % 4
# print "Now I will count the eggs:"

# print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# print "Is it true that 3 + 2 < 5 - 7?"

# print 3 + 2 < 5 - 7

# print "what is 3 + 2?",3 + 2
# print "what is 5 - 7 ?",5 - 7

# print "Oh,that's why it's False."
# print "How about some more."
# print "Is it greater?",5 > -2
# print "Is it greater or equal?",5 >= -2
# print "Is it less or equal?",5 <= -2


"""
ex4 变量和命名
"""
# cars = 100 
# space_in_a_car  = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars- drivers
# cars_driven = drivers 
# carpool_capacity = cars_driven * space_in_a_car

# average_passenger_per_car = passengers / cars_driven

# print "There are", cars," cars available."
# print "There are only",drivers," drivers available."
# print "There will be",cars_not_driven," empty cars today."
# print "We can transport", carpool_capacity," people today."
# print "We have", passengers, 'to carpool today.'
# print "we need to put about", average_passenger_per_car,"in each car"


"""
ex5 更多的变量和打印
"""
# name = 'Zed A.Shaw'
# age = 35 #not a lie
# height = 74 #inches
# weight = 180 #lbs
# eyes = 'Blue'
# teech = 'White'
# hair = 'Brown'


# print "Let's talk about %r." % name
# print "He's %r inches tall." % height
# print "He's %r pounds heavy." % weight
# print "Actually that's not too heavy."
# print "He's got %r eyes and %r hair." %(eyes,hair)
# print "His teeth asre usually %r depending on the coffee." % teech

# # this line is triky, try to get it exactly right

# print "If I add %r,%r, and %r I get %d." %(
# 	age,height,weight,age + height)


"""
ex6 字符串 和文本
"""
# x = "There are %d types of people."  % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." %(binary,do_not)

# print x
# print y 

# print "I said: %r." % x
# print "I also said: '%s'." %y

# hilarious = False 
# joke_evaluation = "Inn't that joke so funncy? %r"

# print joke_evaluation % hilarious

# w = "This is the left side of ....."
# e = "a string with a right side."

# print w + e


"""
ex7 更多打印
"""
# print "Mary had a little lamb."
# print "Its fleece was white as %s." % 'snow'
# print "And everywhere that Mary went."
# print "." * 10 #what'd that do ?

# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"

# # watch that comma at the end.try removing it to see what happens
# print end1 + end2 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12

"""
ex8 打印, 打印
"""

# formatter = "%r %r %r %r"

# print formatter %(1,2,3,4)
# print formatter %("one","two","three","four")
# print formatter %(True, False, False, True)
# print formatter %(formatter, formatter, formatter, formatter)
# print formatter %(
# 	"I had this thing.",
# 	"That you could type up right.",
# 	"But it didn't sing.",
# 	"So I said goodnight."
# 	)


"""
ex9 打印, 打印，打印
"""

#Here's some new strange stuff, remenber type it exactly

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print "Here are the days: %s ", days
# print "Here are the months: %s", months


# print """
# There's something going on here.
# With the three double-quote.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5 ,or 6.
# """



"""
ex10  那是什么
"""

print "I am 6'2\" tall."  # 将字符串中的双引号转义
print "I am 6\'2 tall."  #将字符串中的单引号转义

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat ."

fat_cat = """
I'll do a list:
\t* cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
