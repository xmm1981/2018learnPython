# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
# ###########################
     import pymysql
     # 创建连接
     conn = pymysql.connect(host='192.168.71.137', port=3306, user='root', passwd='xmmxmmxmm', db='xmmtest')
     # 创建游标
     cursor = conn.cursor()
     # effect_row = cursor.execute("select * from students")
     # print (effect_row)
     # print(cursor.fetchone())
     data = [
         ("lily", "women", 25, "13305790021"),
         ("mike", "man", 24, "13305790024"),
         ("candy", "man", 45, "13305790045"),
         ("oly", "women", 55, "13305790055"),
     ]
     cursor.executemany("insert into students (name,sex,age,tel) values (%s,%s,%s,%s)" ,data)
     conn.commit()
     conn.close()
# ------插入新增加数据 data

# ###########################
# import pymysql
#
# # 创建连接
# conn = pymysql.connect(host='192.168.71.137', port=3306, user='root', passwd='xmmxmmxmm', db='xmmtest')
# # 创建游标
# cursor = conn.cursor()
#
# effect_row = cursor.execute("select * from students")
# print (effect_row)
# print(cursor.fetchone()) #每执行一次，读一条记录

# ###########################
# # -*- coding:utf-8 -*-
# import pymysql
#
# # 创建连接
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xmmxmmxmm', db='xmmtest')
# # 创建游标
# cursor = conn.cursor()
#
# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update students set name = 'xmm222' where id =1")
#
# # 执行SQL，并返回受影响行数
# #effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
#
# # 执行SQL，并返回受影响行数
# #effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
#
#
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()
# ###########################
# ###########################
# Mysql:
#     xmm# mysqladmin -u root password "new_password"; #创建新密码
#     xmm# mysql -uroot -pxxxx
#     xmm# mysql -uroot -p #都可以 

#     Mariadb>show databases;
#     Mariadb>use mysql;
#     Mariadb [mysql]>show tables; 
#     Mariadb [mysql]>desc user; #查看表结构
#     Mariadb [mysql]>show columns from 数据表 #和上面的命令一样，查看表结构
#     MariaDB [(none)]> create database xmmdb charset utf8; #创建数据库 支持utf8
#     MariaDB [(none)]> drop database xmmdb;


#     MariaDB [mysql]> select * from user\; #查看表内所有数据
#     MariaDB [mysql]> select * from user\G; #按竖表查看表内所有数据
#             PRI:primary key
#     MariaDB [(none)]> grant ALL on test.* to 'xmm'@'localhost' identified by 'jhwc';#创建新用户 只操作test的所有库


# ****************************************
# MariaDB [(none)]> show create database xmmdb; #查看数据表  CHARACTER SET latin1只支持拉丁文
# +----------+------------------------------------------------------------------+
# | Database | Create Database                                                  |
# +----------+------------------------------------------------------------------+
# | xmmdb    | CREATE DATABASE `xmmdb` /*!40100 DEFAULT CHARACTER SET latin1 */ |
# +----------+------------------------------------------------------------------+
# 1 row in set (0.00 sec)   
# ****************************************

# ****************************************
# #创建一个表 student
# MariaDB [xmmdb]> create table student( 
#     id int auto_increment, 
#     name char(32) not null, 
#     age int not null, 
#     register_date date not null, 
#     primary key (id));
# ****************************************

# ****************************************
#         [root@localhost ~]# more /etc/my.cnf
#         [mysqld]
#         datadir=/var/lib/mysql
#         socket=/var/lib/mysql/mysql.sock
#         # Disabling symbolic-links is recommended to prevent assorted security risks
#         symbolic-links=0
#         # Settings user and group are ignored when systemd is used.
#         # If you need to run mysqld under a different user or group,
#         # customize your systemd unit file for mariadb according to the
#         # instructions in http://fedoraproject.org/wiki/Systemd

#         [mysqld_safe]
#         log-error=/var/log/mariadb/mariadb.log
#         pid-file=/var/run/mariadb/mariadb.pid

#         #
#         # include all files from the config directory
#         #
#         !includedir /etc/my.cnf.d
# ****************************************
# ###########################
# 静态方法：与类无关，不能访问类里的任何属性和方法
# 类方法：只能访问类变量
# 属性@property
#     把一个方法变成一个静态属性
#     flight.status
#     @status.setter
#     flight.status = 3
#     @status.delter
# 反射
#     getattr(object, str)
#     setattr(object,str,val)
#     hasattr(object, str)
#     delattr(object, str)



# 官方不建议用这个：
#     # __import__("lib.aa")#导入的是lib
#     # lib.aa
# 官方建议用这个：
#     import importlib
#     importlib.import_module('lib.aa')#这个导入的是aa
        #与上面的效果一样，官方建议用这个
# ###########################
# Sokter 通信###########################
#服务器端
    # import socket
    # server = socket.socket()
    # server.bind(('localhost',6969))#绑定要监听的端口
    # server.listen()#监听
    # print("我要开始打电话了、、、")
    # #server.accept()#等电话 打过来
    # conn,addr = server.accept()#等电话 打过来
    # #conn就是客户端连过来而在服务器端为其生成的一个连接实例
    # print(conn,addr)
    # print("电话来了、、、")
    # #data = server.recv(1024)
    # data = conn.recv(1024)
    # print("recv:",data)
    # #server.send(data.upper())
    # conn.send(data.upper())
    # server.close()

    # #客户端
    # import socket
    # client = socket.socket() #声明socket类型，同时生成socket连接对象
    # client.connect(('localhost',6969))
    # client.send(b"Hello World!")
    # data = client.recv(1024)
    # print ("recv:", data)
    # client.close()
# 类的特殊成员方法###########################
      # xxx.__doc__
      #   '''xxx is xxx'''
      # xxx.__module__
      #   #输出模块是哪个  lib.aa.bb.xxx
      # xxx.__class__
      #   #输出类
      # xxx.__init__
      # xxx.__del__
      # xxx.__call__ 
# 静态方法###########################
    # @staticmethod  #静态方法实际上跟类没什么关系
    # def xxxx(self):
    #     ....
    #     #只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
    # @classmethod   #区别是
    # def xxxx(self):
    #     ....
    #     #只能访问类变量，不能访问实例变量
    # @property   #属性方法     #attribute 
    # def xxxx(self):
    #     ....
    #     #把一个方法变成一个静态属性 本来是d.eat() 现在是d.eat
    # @property
    # def eat(self):
    #     pass

    # @eat.setter
    # @eat.deleter  



# ###########################
# 多态 ###########################
    # 一种接口，多种实现！！！！ 实现接口的重用。

    # 多态性是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，
    # 父对象就可以根据当前赋值给它的子对象的特性以不同的方式动作。简单的说，
    # 就是一句话：允许将子类类型的指针赋值给父类类型的指针。
#------实例讲解###########################


# 继承 ###########################
#------实例讲解###########################
    # #学校里有 主讲师 学生
    # class School(object):
    #     def __init__(self,name,addr):
    #         self.name = name
    #         self.addr = addr
    #         self.students = []
    #         self.teachers = []
    #         self.staffs = []
    #         print('''
    #     ----学校名称：%s 地址：%s----
    #         '''%(self.name, self.addr))
    #     def enroll(self,stu_obj):
    #         print("为学员%s 办理注册手续" % stu_obj.name)
    #         self.students.append(stu_obj)
    #     def hire(self,staff_obj):
    #         print("为教师%s 办理注册手续" % staff_obj.name)
    #         self.staffs.append(staff_obj)
    # class SchoolMember(object):
    #     def __init__(self,name,age,sex):
    #         self.name = name
    #         self.age = age
    #         self.sex = sex
    #     def tell(self):
    #         pass
    # class Teacher(SchoolMember):
    #     def __init__(self,name,age,sex,salary,course):
    #         super(Teacher,self).__init__(name,age,sex)
    #         self.salary = salary
    #         self.course = course
    #     def tell(self):
    #         print('''
    #         --- info of Teacher:%s ---
    #         Name:%s
    #         Age:%s
    #         Sex:%s
    #         Salary:%s
    #         Course:%s
    #         '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    #     def teach(self):
    #         print("%s is teaching course [%s]" %(self.name,self.course))
    # class Student(SchoolMember):
    #     def __init__(self,name,age,sex,stu_id,grade):
    #         super(Student,self).__init__(name,age,sex)
    #         self.stu_id = stu_id
    #         self.grade = grade
    #     def tell(self):
    #         print('''
    #         --- info of Student:%s ---
    #         Name:%s
    #         Age:%s
    #         Sex:%s
    #         Stu_id:%s
    #         Grade:%s
    #         '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    #     def pay_tuition(self,amount):
    #         print("%s has paid tuition for $%s"% (self.name,amount))
    # school = School("第一中学","金华市婺城区兰溪街")
    # t1 = Teacher("张老师",56,"M",5000,"WIN7")
    # t2 = Teacher("李老师",25,"F",8000,"Centos7")
    # s1 = Student("张小明",14,"M",2018001,"WIN7")
    # s2 = Student("李小四",13,"M",2018102,"Centos7")
    # t1.tell()
    # s1.tell()
    # s2.tell()
    # school.hire(t1)
    # school.enroll(s1)
    # school.enroll(s2)
    # print(school.students)
    # print(school.staffs)
    # school.staffs[0].teach()
    # for stu in school.students:
    #     stu.pay_tuition(500)
# 继承###########################
    #在python2当中，经典类是按深度优先去继承构造函数的,新式类是按广度优先来继承构造函数的
    #在python3当中,经典类和新式类都是统一按广度优先来继承构造函数的
# -------经典类与新式类###########################
    # class A:
    #     ....    #这样的是经典类 
    # class A(object):
    #     ....    #这样的是新式类
# 举个例子：
# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     pass
#     #def __init__(self):
#     #    print("B")
# class C(A):
#     def __init__(self):
#         print("C")
# class D(B, C):
#     pass
#     #def __init__(self):
#     #    print("D")
# DD=D() 

# 类与类的继承###########################
    # class People(object): #新式类
    #     def __init__(self, name, age, ):
    #         self.name = name
    #         self.age = age
    #         self.friends = []

    #     def eat(self):
    #         print("%s is eating..." % self.name)

    #     def talk(self):
    #         print("%s is talking..." % self.name)

    #     def sleep(self):
    #         print("%s is sleeping..." % self.name)

    # class Relation(object):
    #     def make_friends(self,obj): #W1
    #         print("%s is making friends with %s" %(self.name,obj.name))
    #         self.friends.append(obj)

    # class Man(People,Relation):
    #     def __init__(self,name,age,money):
    #         #People.__init__(self,name,age)
    #         super(Man,self).__init__(name,age)
    #         self.money = money
    #         print("%s 一出生就有 %s money" %(self.name,self.money))

    #     def piao(self):
    #         print("%s is piaoing... 20s .... done" % self.name)
    #     def sleep(self):
    #         People.sleep(self)
    #         print("man is sleeping...")

    # class Women(People,Relation):
    #     def get_birth(self):
    #         print("%s is born a baby..." % self.name)


    # m1 = Man("男人1",29,100)
    # # m1.eat()
    # # m1.piao()
    # # m1.sleep()
    # w1 = Women("女人1" ,26)
    # # w1.get_birth()
    # m1.make_friends(w1)
    # print(m1.friends[0].name)



# ###########################
# 模块定义、导入、优化：
#     1、定义
#     模块：用来从逻辑上组织python代码(变量,函数,类,逻辑:实现一个功能),
#     本质就是.py结尾的python文件（文件名:test.py,对应的模块名：test）
#     包：用来从逻辑上组织模块，本质就是一个目录(必须带有一个__init__.py文件)

#     2、导入方法
#     import module_name  #module_xmm ----->里， 面的所有代码
#     import module1_name,module2_name
#     from module_xmm import *  #全部导入
#     from module_xmm import m1,m2,m3
#     from module_xmm import logger as logger_xmm #设置别名 导入本模块 优化速度

#     3、import本质(路径搜索和搜索路径)
#     导入模块的本质就是把python文件解释执行一遍 
#     (import test test='test.py all code')
#     (from test import name   只把test.py中的m1 拿来解释执行一遍 name='code')
#     import module_name ---->module_name.py--->module_name.py的路径--->sys.path
#         import sys,os
#         print (os.path.dirname(os.path.abspath(__file__)))
#         x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         sys.path.append(x)  #sys.path.insert(x) 插入到最前面

#     导入包的本质就是去执行该包(目录)下的__init__.py文件

#     4、导入优化s
#     from module_test import test\

    # 5、模块的分类(分三类)：
    # 5-1:标准库
    #     1.time与datetime
    #         将时间戳转换成元组的方式，有二种
    #         gmtime: 结果为UTC时区
    #         localtime：结果为UTC+8时区

    #         把元组转换成字符 互转
    #         strftime("格式",struct_time) --->"格式化的字符串"
    #         strptime("格式化的字符串"，"格式") -->struct_time
    #         >>> x = time.localtime()
    #         >>> time.strftime("%Y-%m-%d %H:%M:%S" ,x)
    #             '2018-01-24 20:40:13'
    #         >>> time.strptime('2018-01-24 20:40:13',"%Y-%m-%d %H:%M:%S")
    #             time.struct_time(tm_year=2018, tm_mon=1, tm_mday=24, tm_hour=20, tm_min=40, tm_s
    #             ec=13, tm_wday=2, tm_yday=24, tm_isdst=-1)
    #         datetime.datetime.xxx() 自已了解吧
    
            # #!/usr/bin/env python
            # #_*_encoding: utf-8_*_
            # import random
            # print (random.random())  #0.6445010863311293  
            # #random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
            # print (random.randint(1,7)) #4
            # #random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。
            # # 其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
            # print (random.randrange(1,10)) #5
            # #random.randrange的函数原型为：random.randrange([start], stop[, step])，
            # # 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
            # # 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
            # # random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
            # print(random.choice('liukuni')) #i
            # #random.choice从序列中获取一个随机元素。
            # # 其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
            # # 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。
            # # list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章。
            # # 下面是使用choice的一些例子：
            # print(random.choice("学习Python"))#学
            # print(random.choice(["JGood","is","a","handsome","boy"]))  #List
            # print(random.choice(("Tuple","List","Dict")))   #List
            # print(random.sample([1,2,3,4,5],3))    #[1, 2, 5]
            # #random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
          
    # 5-2:开源模块
    # 5-3:自定义模块
# 内置方法###########################
# json和pickle模块       
    # 用于序列化的两个模块
    # json，用于字符串 和 python数据类型间进行转换
    # pickle，用于python特有的类型 和 python的数据类型间进行转换
    # Json模块提供了四个功能：dumps、dump、loads、load
    # pickle模块提供了四个功能：dumps、dump、loads、load


    # json的使用方法  还有一个pickle 是二进制的
    # import json
    # info = {
    #     'name':'xmm',
    #     'age':'33',
    #     'sex':'F'
    # } 
    # f = open("test.txt","w")
    # f.write(json.dumps(info))
    # f.close()
    # #--------------------------------
    # import json
    # f = open("test.txt","r")
    # data = json.loads(f.read())
    # print(data["age"])
    # print(data)

#__import__('os') ######

#zip() 拉链的用法。zip就是拉链的意思
# a = [1,2,3,4,5,6]
# b = ['a','b','c','d']
# for i in zip(a, b):
#     print (i)
    #sorted()的使用方法
    # a = {6:-2,8:0,-1:4,5:7,-3:55,66:444}
    # print(a)
    # print(sorted(a))
    # print(sorted(a.items()))
    # print(sorted(a.items(), key = lambda x: x[1]))
# a = frozenset([1,2,343,2,1])
# b = set([1,2,3,4,5,6])  #set()和 frozenset()工厂函数分别用来生成可变和不可变的集合
# def test():
#     xmm = 22
#     print(locals())
# test()
# print(globals())
    # import functools
    # res = functools.reduce(lambda x,y: x*y, range(1,10))
    # print (res)
#res = filter(lambda n: n>5, range(10)) #变成一个生成器
#res = map(lambda n: n*2, range(10)) #变成一个生成器
# res = [ lambda n: n*2 for n in range(10) ] #变成一个生成器
# for i in res:
#     print(i)
    # def sayhi(n):
    #     print (n)
    #     for i in range(n):
    #         print (i)
    # sayhi(3)
    # #calc = lambda n:print(n)
    # calc = lambda n:3 if n<4 else n
    # print(calc(1))
# code1 = "1+3/2*6"
# code2 = "for i in range(10):print(i)"
# c1 = compile(code1, '', 'eval')
# c2 = compile(code2, 'err.log', 'exec')
# print (eval(c1))
# print (exec(c2),exec(code2))  #compile不用也行
    # a = bytes("abcde", encoding="utf-8")
    # b = bytearray("abcde", encoding="utf-8")
    # print (b[2])
    # b[1] = 91
    # print(b)
# aa = ascii([1,2,3,"你好的"])
# print(type(aa),[aa])
# print (all([1,-1,3]))
# print (any([0,0,0]))
# ###########################
#第四周-第13章节-Python3.5-迭代器与生成器并行.avi
# ###########################
# 生成器：只有在调用时才会生成相应的数据
#         只记录当前位置
# 只有一个__next__()方法    python2里面是 next()
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         #print(b)
#         yield b 
#         a, b = b, a+b
#         n = n + 1
#     #return 'done'
# f = fib(100)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# 装饰器 终极版2###########################
# import time
# user,passwd = 'xmm','123'
# def auth(auth_type):
#     print("auth func:",auth_type)
#     def outer_wrapper(func):
#         def wrapper(*args, **kwargs):
#             print("wrapper func args:", *args, **kwargs)
#             if auth_type == "local":
#                 username = input("Username:").strip()
#                 password = input("Password:").strip()
#                 if user == username and passwd == password:
#                     print("User has passed authentication!")
#                     res = func(*args,**kwargs) #from home
#                     print("-------after authentication")
#                     return res
#                 else:
#                     exit("Invalid username or password!") 
#             elif auth_type == "ldap":
#                 print("搞毛线ldap,不会....")
#         return wrapper
#     return outer_wrapper
# def index():
#     print("welcome to index page!")
# @auth(auth_type="local")
# def home():
#     print("welcome to home page!")
# @auth(auth_type="ldap")
# def bbs():
#     print("welcom to bbs page!")
# index()
# home()
# bbs()
# 装饰器 终极版1#######################
# import time
# user,passwd = 'xmm','123'
# def auth(func):
#     def wrapper(*args, **kwargs):
#         username = input("Username:").strip()
#         password = input("Password:").strip()
#         if user == username and passwd == password:
#             print("User has passed authentication!")
#             func(*args,**kwargs)
#         else:
#             exit("Invalid username or password!")
#     return wrapper

# def index():
#     print("welcome to index page!")
# @auth
# def home():
#     print("welcome to home page!")
# @auth
# def bbs():
#     print("welcom to bbs page!")

# index()
# home()
# bbs()
# 装饰器2  高潮111#######################
# import time
# def timer(func):
#     def deco(*args, **kwargs):
#         start_time=time.time()
#         func(*args, **kwargs)
#         stop_time=time.time()
#         print ("the func run time is %s" %(stop_time-start_time))
#     return deco
# @timer 
# def test1():
#     time.sleep(1)
#     print ('in the test1')

# @timer
# def test2(name, age):
#     print ("test2:", name, age)
# test1()
# test2("xmm",33)
# 装饰器1########################
# import time
# def timer(func):
#     def deco():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print ("the func run time is %s" %(stop_time-start_time))
#     return deco
# @timer #test1=timer(test1)
# def test1():
#     time.sleep(2)
#     print ('in the test1')

# @timer#test1=timer(test1)
# def test2():
#     time.sleep(2)
#     print ('in the test2')
# #test1=timer(test1)        此处@前身：）
# test1()
# test2()
# ###########################
# 装饰器：
# 定义：本质是函数，（装饰其他函数）就是为其他函数添加附加功能
# 原则：  1、不能修改被装饰的函数的源代码
#         2、不能修改被装饰的函数的调用方式
# 实现装饰器知识储备
# 1、函数即“变量”
# 2、高阶函数
#     a:把一个函数名当做实参传给另一个函数(在不修改被装饰函数源代码的情况下为其添加功能)
#     b:返回值中包含函数名(不修改函数的调用方式)
# 3、嵌套函数
# 高阶函数+嵌套函数=》装饰器
# ###########################
# 高阶函数
# 文件操作
# f = open  r,w,a  r+,w+,a+  rb,wb,ab
# f = open('test.txt', 'wb', encoding="utf-8")
# f.seek, tell, truncate flush()
# f.close
#
# ###########################
# 递归
#	1、明确的结束条件
# 	2、问题规模每递归一次都应该比上一次的问题规模有所减少
# 	3、效率低
# ###########################
# 递归
# def calc(n):
# 	print(n)
# 	if int(n/2) > 0:
# 		return calc(int(n/2))
# 	print('-->',n)
# calc(10)
# ###########################
# def test4(name,age=18,*args,**kwargs):
# 	print (name)
# 	print (age)
# 	print (args)
# 	print (kwargs)
# test4('xmm',age=11,sex='M',hobby='tesla')
# ###########################
# **kwars：接受N个关键字参数，转换成字典的方式
# def test2(**kwargs):
# 	print (kwargs)
# test2(name='xmm',age=22,sex='F')
# ###########################
# *args:接受N个位置参数，转换成元组形式
# def test(*args):
# 	print (args)
# test(1,2,3,4,5,6)
# ###########################
# 位置参数和关键字参数#######
# def test(x, y，z):
# 	print (x)
# 	print (y)
# x = 1
# y = 2
# test(x=x, y=y) 	#与形参顺序无关
# test(1,2)		#与形参一一对应
# test(x=2,3) #不行
# test(2,y=3) #行
# test(3,z=2,y=6) #关键字参数是不能写在位置参数前面，就可以。
# ###########################
# 函数返回值数
# 返回值数=0：返回None
# 返回值数=1：返回object
# 返回值数>1：返回tuple
# def test1():
# 	print ('in the test1')
# def test2():
# 	print ('in the test2')
# 	return 0
# def test3():
# 	print ('in the test3')
# 	return 1,'hello',['alex','xmm'],{'name':'xmm'}
# x = test1()
# y = test2()
# z = test3()
# print (x)
# print (y)
# print (z)
# 	ctrl+B
# 	in the test2
# 	in the test3
# 	None
# 	0
# 	(1, 'hello', ['alex', 'xmm'], {'name': 'xmm'})
# ###########################
# with open('/home/share/www_access_20171225.log') as f:
# 	accessDict = {}
# 	for oneAccess in f.readlines():
# 		oneAccessList = oneAccess.split(' ')
# 		accessDictKey = (oneAccessList[8], oneAccessList[6], oneAccessList[0])
# 		if accessDictKey in accessDict:
# 			accessDict[accessDictKey] += 1
# 		else:
# 			accessDict[accessDictKey] =1
# for k, v in accessDict.items():
# 	print [k[0], k[1], (k[2], v)]

# ###########################
# 插入排序 
# array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
# for i in range(1, len(array)):
#     if array[i - 1] > array[i]:
#         temp = array[i]     # 当前需要排序的元素
#         index = i           # 用来记录排序元素需要插入的位置
#         while index > 0 and array[index - 1] > temp:
#             array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
#             index -= 1
#         array[index] = temp # 把需要排序的元素，插入到指定位置
# print(array)
# 求两个数组共同的值（去重）
# ###########################
# add1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# add2 = [2,1,3,2,43,234,454,452,234,14,21,14]
# add_no1 = []
# add_no2 = []
# for i1 in add1:
# 	for i2 in add2:
# 		if i1 == i2:
# 			add1.remove(i1)
# 			add2.remove(i2)
# for o1 in add1:
# 	if o1 not in add_no1:
# 		add_no1.append(o1)
# for o2 in add2:
# 	if o2 not in add_no2:
# 		add_no2.append(o2)		
# print (add_no1)
# print (add_no2)
# ###########################
#  冒泡排序 从小到大排序
# arr = [14,26,655,555,988,65535,38,56]
# for j in range(len(arr)):
# 	for i in range(len(arr)-1-j):
# 		if arr[i] > arr[i+1]:
# 			arr[i],arr[i+1] = arr[i+1], arr[i]
# print (arr)	
# ###########################
# 数组去重
# add = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# add2 = []
# for i in add:
# 	if i not in add2:
# 		add2.append(i)
# print (add2)
# ###########################
# 引导复习一下list的知识：
	# 怎么定认一个list
	# in,len,max,min,del
	# 切片
	# append,count,extend,index,insert,pop,remove,reverse
# ###########################
# add = list('hello')
# add_reverse = []
# while len(add) > 0:
# 	add_reverse.append(add.pop())
# print (add_reverse)
# ###########################
# add = list('abcd')
# add.reverse()
# print (add)
# add.remove('a')
# print (add)
# ###########################
# add = []
# while True:
# 	action = input('input you action:')
# 	if action == 'add':
# 		detail = input('input things you want:')
# 		add.append(detail)
# 		print (add)
# 	elif action == 'do':
# 		if len(add) == 0:
# 			break
# 		print (add.pop(0))
# ###########################