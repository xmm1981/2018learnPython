# try:
# 	age=input('1>>:')
# 	int(age)
# 	num2=input('2>>:')
# 	int(num2)
# 	# D=[]
# 	# D[1000]
# 	dic={}
# 	dic['name']
# except Exception as e:
# 	print(e)

while  True:
	try:
		age=input('1>>:')
		int(age)
		break
	except Exception as e:
		print('请重新输入',e)
print("执行最后面了，hehe")