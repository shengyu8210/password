password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤！' )
		i = i - 1
		if i > 0:
			print('你還有', i, '次機會！')
		else:
			print('沒機會了！你的帳號要被鎖住囉！')


		

