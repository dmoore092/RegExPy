import re

students = []
i = 0
agecheck = re.compile('^([1-9]{1,2}){1}(\.[1-9]{1,2})?$')

gpacheck = re.compile('^[0-3]\.[0-9]')

gpacheck1 = re.compile('4.0')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def getStudentInfo(self):
        while True:
            yesorno = raw_input("Enter Student Data? ").upper()
            if yesorno == 'Y':
                if not re.match("[Y]", yesorno):
                    print 'Please enter just Y or N'
                else:
                    break
            elif yesorno == 'N':
                break
        return yesorno

    def setName(self):
        self.name = raw_input("Name: ").strip()
        return self.name

    def setAge(self):
        while True:
            self.age = int(raw_input("Age: "))
            if not re.match(agecheck, str(self.age)):
                print 'Age must be between 1 and 99'
            else:
                break
        return self.age

    def setGpa(self):
        while True:
            self.gpa = raw_input("GPA: ")
            if not gpacheck.match(self.gpa) or gpacheck1.match(self.gpa):
            #if not re.match("\d.\d", self.gpa):
                print 'Input GPA to one decimal place'
            else:
                break
        return self.gpa

    def setOutfile(self):
        outfile = raw_input("Enter File Name: ")
        return outfile

    def getName(self):

        return self.name
    def getAge(self):

        return self.age
    def getGpa(self):

        return self.gpa

while True:

    stdnt = Student("blank", 00, 0.0)
    k = 0
    if stdnt.getStudentInfo() == 'Y':
        stdnt.setName()
        stdnt.setAge()
        stdnt.setGpa()
        students.append(stdnt)

    else:
        i = 0
        outfile = open(stdnt.setOutfile() + '.txt', 'w')
        while i < len(students):
            stu = students[i]
            #print(stu.getName(), str(stu.getAge()), str(stu.getGpa()))
            print'%-25s'%(stu.getName()), '%3s'%(str(stu.getAge())), '%4s'%(str(stu.getGpa()))
            outfile.write('%-25s'%(stu.getName()) + ('%3s'%(str(stu.getAge())) + " " + ('%3s'%(str(stu.getGpa())))) + '\n')
            i += 1
        break

outfile.close()
quit()