class Student(object):
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def sayHello(self):
        return "hello,name:{0},age:{1}".format(self.name,self.age)


