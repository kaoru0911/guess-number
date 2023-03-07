# 重複猜1~100的整數
# 提示大小
# 計數猜幾次

import random
n = input('自訂猜數字的範圍最小整數是：')
m = input('自訂猜數字的範圍最大整數是：')
n = int(n)
m = int(m)
r = random.randint(n, m)
i = 0
while True:
	i += 1  #i = i + 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('答對了！')
		print('總共猜了',i , '次')
		break
	elif num > r:
		print('再小一點')
	elif num < r:
		print('再大一點')
	


