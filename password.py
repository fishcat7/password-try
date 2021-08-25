password = 'a123456'
x = 3
print('最多輸入三次密碼')
while x > 0:
	x = x - 1 
	code = input('請輸入密碼:')
	if code == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', x, '次機會')
		if x <= 0:
			print('登入失敗')
			break
	

