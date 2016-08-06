#coding:utf-8
#dict = {'key':函数对象}
def  jiafa(x,y):
	return x + y

def jianfa(x,y):
	return x - y

def chengfa(x,y):
	return x * y

def chufa(x,y):
	return x / y
mydict = {"+":jiafa,"-":jianfa,"*":chengfa, "/":chufa}

while  True:
	x = raw_input("请输入第一个数: ")
	y = raw_input("请输入第二个数: ")
	if not (x.isdigit() and y.isdigit()):   #判断用户输入的是否为数字
		print "please input interger."
	else:	
		x = int (x)
		y = int (y)
		operate = raw_input("请输入要进行的运算符：")
		print("结果是%d"%mydict[operate](x,y))


# while  True:	
# 		x = int (raw_input("请输入第一个数: "))
# 		y = int (raw_input("请输入第二个数: "))
# 		operate = raw_input("请输入要进行的运算符：")
# 		print("结果是%d"%mydict[operate](x,y))