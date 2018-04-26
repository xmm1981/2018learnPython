"""
1 描述符是什么:描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议
__get__():调用一个属性时,触发
__set__():为一个属性赋值时,触发
__delete__():采用del删除属性时,触发

2 描述符是干什么的:描述符的作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)

3 描述符分两种
	一 数据描述符:至少实现了__get__()和__set__()
	二 非数据描述符:没有实现__set__()

4 注意事项:
	一 描述符本身应该定义成新式类,被代理的类也应该是新式类
	二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
	三 要严格遵循该优先级,优先级由高到底分别是
		1.类属性
		2.数据描述符
		3.实例属性
		4.非数据描述符
		5.找不到的属性触发__getattr__()


	描述符优先级是：
	类属性  >  数据描述符 >  实例属性  >  非数据描述符  非数据描述符  >  找不到
	"""
#缓存不起来了
# ============================================================================================
# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         if instance is None:
#             return self
#         else:
#             value=self.func(instance)
#             instance.__dict__[self.func.__name__]=value
#             return value
#         # return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情
#     def __set__(self, instance, value):
#         print('hahahahahah')

# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length

#     @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
#     def area(self):
#         return self.width * self.length

# print(Room.__dict__)
# r1=Room('alex',1,1)
# print(r1.area)
# print(r1.area) 
# print(r1.area) 
# print(r1.area) #缓存功能失效,每次都去找描述符了,为何,因为描述符实现了set方法,
# 它由非数据描述符变成了数据描述符,数据描述符比实例属性有更高的优先级,因而所有的属性操作都去找描述符了
# ============================================================================================

# 利用描述符原理完成一个自定制@classmethod

# class ClassMethod:
#     def __init__(self,func):
#         self.func=func

#     def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
#         def feedback():
#             print('在这里可以加功能啊...')
#             return self.func(owner)
#         return feedback

# class People:
#     name='linhaifeng'
#     @ClassMethod # say_hi=ClassMethod(say_hi)
#     def say_hi(cls):
#         print('你好啊,帅哥 %s' %cls.name)

# People.say_hi()

# p1=People()
# p1.say_hi()
#疑问,类方法如果有参数呢,好说,好说
# ---------------------------------------------------------------------------------------
# class ClassMethod:
#     def __init__(self,func):
#         self.func=func

#     def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
#         def feedback(*args,**kwargs):
#             print('在这里可以加功能啊...')
#             return self.func(owner,*args,**kwargs)
#         return feedback

# class People:
#     name='linhaifeng'
#     @ClassMethod # say_hi=ClassMethod(say_hi)
#     def say_hi(cls,msg):
#         print('你好啊,帅哥 %s %s' %(cls.name,msg))

# People.say_hi('你是那偷心的贼')

# p1=People()
# p1.say_hi('你是那偷心的贼')
# ============================================================================================

# 利用描述符原理完成一个自定制的@staticmethod
# class StaticMethod:
#     def __init__(self,func):
#         self.func=func

#     def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
#         def feedback(*args,**kwargs):
#             print('在这里可以加功能啊...')
#             return self.func(*args,**kwargs)
#         return feedback

# class People:
#     @StaticMethod# say_hi=StaticMethod(say_hi)
#     def say_hi(x,y,z):
#         print('------>',x,y,z)

# People.say_hi(1,2,3)

# p1=People()
# p1.say_hi(4,5,6)
# ============================================================================================
# 再看property
# 一个静态属性property本质就是实现了get，set，delete三种方法

# class Foo:
#     @property
#     def AAA(self):
#         print('get的时候运行我啊')

#     @AAA.setter
#     def AAA(self,value):
#         print('set的时候运行我啊')

#     @AAA.deleter
#     def AAA(self):
#         print('delete的时候运行我啊')

# #只有在属性AAA定义property后才能定义AAA.setter,AAA.deleter
# f1=Foo()
# f1.AAA
# f1.AAA='aaa'
# del f1.AAA
#---------------------------------------------------------------------------------------
# class Foo:
#     def get_AAA(self):
#         print('get的时候运行我啊')

#     def set_AAA(self,value):
#         print('set的时候运行我啊')

#     def delete_AAA(self):
#         print('delete的时候运行我啊')
#     AAA=property(get_AAA,set_AAA,delete_AAA) #内置property三个参数与get,set,delete一一对应

# f1=Foo()
# f1.AAA
# f1.AAA='aaa'
# del f1.AAA
# ============================================================================================
# 怎么用？
# class Goods:
#     def __init__(self):
#         # 原价
#         self.original_price = 100
#         # 折扣
#         self.discount = 0.8
#     @property
#     def price(self):
#         # 实际价格 = 原价 * 折扣
#         new_price = self.original_price * self.discount
#         return new_price
#     @price.setter
#     def price(self, value):
#         self.original_price = value
#     @price.deleter
#     def price(self):
#         del self.original_price
# obj = Goods()
# obj.price         # 获取商品价格
# print(obj.price)        # 获取商品价格
# obj.price = 200   # 修改商品原价
# print(obj.price)
# del obj.price     # 删除商品原价
# ============================================================================================
#实现类型检测功能

#第一关：
# class People:
#     def __init__(self,name):
#     	self.name= name

#     @property
#     def name(self):
#         return self.name

# p1=People('xxxx') #property自动实现了set和get方法属于数据描述符,
# 比实例属性优先级高,所以你这面写会触发property内置的set,抛出异常


# #第二关：修订版

# class People:
#     def __init__(self,name):
#         self.name=name #实例化就触发property

#     @property
#     def name(self):
#         # return self.name #无限递归
#         print('get------>')
#         return self.DouNiWan

#     @name.setter
#     def name(self,value):
#         print('set------>')
#         self.DouNiWan=value

#     @name.deleter
#     def name(self):
#         print('delete------>')
#         del self.DouNiWan

# p1=People('alex') #self.name实际是存放到self.DouNiWan里
# print(p1.name)
# print(p1.name)
# print(p1.name)
# print(p1.__dict__)

# p1.name='egon'
# print(p1.__dict__)

# del p1.name
# print(p1.__dict__)


# #第三关:加上类型检查
# class People:
#     def __init__(self,name):
#         self.name=name #实例化就触发property

#     @property
#     def name(self):
#         # return self.name #无限递归
#         print('get------>')
#         return self.DouNiWan

#     @name.setter
#     def name(self,value):
#         print('set------>')
#         if not isinstance(value,str):
#             raise TypeError('必须是字符串类型')
#         self.DouNiWan=value

#     @name.deleter
#     def name(self):
#         print('delete------>')
#         del self.DouNiWan


# p1=People('alex') #self.name实际是存放到self.DouNiWan里
# print(p1.name)
# p1.name="1"
# print(p1.name)
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================



