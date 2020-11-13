from student import Student 

class ZhangSan(Student):
    grade = ''
    # 私有变量
    __flag = 0x123
    #self代表类的实例
    def __init__(self, name, age,w,g):
        Student.__init__(self,name,age,w)
        self.grade = g
    
    def getGrade(self):
        self.__getFlag()
        return self.grade
    
    def getFlag(self):
        self.__getFlag()

    # 私有方法
    def __getFlag(self):
        print("private method")
        print(self.__flag)

    

 


