class Romm:
	# area1=1
	def __init__(self, name, width, length):
		self.name=name
		self.width=width
		self.length=length
	@property	#area=proerty(area)  类似于class Room下的area1="1"
	def area(self):
		return self.width * self.length

r1 = Romm('厕所',1,1)
# print(r1.area1)
print(r1.area)