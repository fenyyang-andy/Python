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
	x = int(raw_input("请输入第一个数"))
	operate = raw_input("请输入要进行的运算符：")
	y = int(raw_input("请输入第二个数"))
	print("结果是%d"%mydict[operate](x,y))