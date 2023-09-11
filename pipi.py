with open('pupu.txt', 'r') as file:
    lines = file.readlines()

class EducationClass:
    def __init__(self, type, data, auditoria, teacher):
        self.type = type
        self.data = data
        self.auditoria = auditoria
        self.teacher = teacher

    def pr(self):
        print(type, self.type, self.data, self.auditoria, self.teacher)

mylist = []
for string in lines:
    buff = string.split()
    day = EducationClass(buff[0], buff[1], buff[2], buff[3])
    mylist.append(day)


for t in mylist:
    print(t.type, t.data, t.auditoria, t.teacher)

