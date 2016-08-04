#coding:utf-8
myfile = open('user.txt','r')
islogin = 1 #标志位
logintimes = 1  #登录次数，初始化为1
while True:
	if islogin == 1:
		if logintimes == 4:
			print "你登录已超过三次，请找回密码"
			break
		else:
			account = raw_input("请输入要登录的账号：")
			passwd = raw_input("请输入要登录的密码：")
			print "这是你第%d次登录，你还剩%d次机会。" %(logintimes,3-logintimes)
			myfile.seek(0,0)
			for buf in myfile:
				account_buf = buf.split(':')[0] #取出账号
				passwd_buf = buf.split(':')[1][:-1] #取出密码
				if account == account_buf and passwd == passwd_buf:
					print "你登录成功了！",account_buf
					islogin = 0
					break
			logintimes += 1
			continue
	else:
		break