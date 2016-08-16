#coding:utf-8
#斐波那契数列
def fibs(n):
	result = [0,1]
	for i in range (n-2):
		result.append(result[-2]+result[-1])
	return result
if __name__ == '__main__':
	lst = fibs(10)
	print lst 