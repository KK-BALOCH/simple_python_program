def Gender():
            gender = str(input("gender male/female :"))
            return gender
def Names():
        name = str(input("enter the student name :"))
        return name
def Gpa():
     gpa = float(input("enter the Gpa:"))
     return gpa
def Age():
        age = int(input("enter the age:"))
        return age
def Enrolling():
        Enrolled = str(input("enrolled:yes/no :"))
        return Enrolled
class StudentRecords:
    name =None
    age =None
    is_enrolled = None
    gpa = None
    gender = None
    def __init__(self):
        self.name =  Names()
        self.age =  Age()
        self.is_enrolled= Enrolling()
        self.gender =  Gender()
        self.gpa =  Gpa()
    def printValue(self):
        print('')
        print('The student name is '+ self.name)
        if(self.age>=18):
            print(self.name + ' is ',self.age ,'years old')
        if(self.is_enrolled=='yes'):
            print(self.is_enrolled, ' ', self.gender , 'is enrolled')
        else:
            print(self.is_enrolled, '', self.gender , 'is not enrolled')
        print(self.gender+' has acheived ', self.gpa , ' in the last semester')

studentRecordInstance = StudentRecords()
studentRecordInstance.printValue()