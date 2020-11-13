class Student(object):
    name = ''
    age = 0
    __weight = 0
    #self代表类的实例
    def __init__(self, name, age,w):
        self.name = name
        self.age = age
        self.__weight = w
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def sayHello(self):
        return "hello,name:{0},age:{1},weight:{2}".format(self.name,self.age,self.__weight)


