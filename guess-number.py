# 重複猜1~100的整數
# 提示大小
# 計數猜幾次

import random
r = random.randint(1, 100)
i = 0
while True:
	i += 1  #i = i + 1
	num = input('請猜數字(1~100)：')
	num = int(num)
	if num == r:
		print('答對了！')
		print('總共猜了',i , '次')
		break
	elif num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')
	


