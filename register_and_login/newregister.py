#coding:utf-8
myfile = open('user.txt','a+')
a = 1 #标志位
while True:
	account = raw_input("请输入你的账号：")
	myfile.seek(0,0)  #回到开始的地方
	for buf in myfile:
		account_buf = buf.split(':')[0]  #切片取出账号
		if account == account_buf:    #比较文本中的账号
			a = 0
			print "用户名已经被注册"
			break
	if a == 1:
		passwd1 = raw_input("请输入你的密码：")
		passwd2 = raw_input("请再次输入你的密码：")
		if passwd1 == passwd2:
			str = "%s:%s"%(account,passwd1)  #按账号：密码形式写入文本中
			myfile.write(str)   #写入文件
			print "恭喜你，注册成功"
			break
		else:
			print "密码不一样，请重新输入。"
			continue
	else:
		break
