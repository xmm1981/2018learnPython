class Lazyproperty:
	def __init__(self, func):
		# print('======>', func)
		self.func=func
	def __get__(self, instance, owner):
		# print('get')
		# print(instance)
		# print(owner)
		res=self.func(instance)
		return res
		# return self.func(instance)

class Romm:
	# area1=1
	def __init__(self, name, width, length):
		self.name=name
		self.width=width
		self.length=length
	# @property	#area=proerty(area)  类似于class Room下的area1="1"
	@Lazyproperty	#area=Lazyproperty(area)
	def area(self):
		return self.width * self.length

	@property
	def test(self):
		return '11111111111111111'
# print(Romm.__dict__)
# print(r1.area.func(r1))

r1 = Romm('厕所',1,1)

# print(r1.__dict__)
print(r1.area)
print(r1.test)
