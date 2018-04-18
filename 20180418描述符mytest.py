class Typed:
	def __init__(self, key,expected_type):
		self.key=key
		self.expected_type=expected_type

	def __get__(self, instance, value):
		print('这里是get方法')
		return instance.__dict__[self.key]

	def __set__(self, instance, value):
		print('这里是set方法')
		if not isinstance(value,self.expected_type):
			raise TypeError('%s 传入的类型不是 %s' %(self.key, self.expected_type))
		instance.__dict__[self.key]=value			

	def __delete__():
		print('这里是delete方法')
		instance.__dict__.pop[self.key]

class People:
	name = Typed('name',str)
	age = Typed('age',int)
	salary = Typed('salary',float)
	def __init__(self, name, age, salary):
		self.name=name
		self.age=age
		self.salary=salary

p1=People('xmm',33,4434.00)
print(p1.__dict__)