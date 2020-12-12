class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        s = 0
        for m in self.scores:
            s += m
        s = s//len(self.scores)
        o = 'T'
        if 90 <= s and s<= 100:
            o = 'O'
        elif 80 <= s and s< 90:
            o = 'E'
        elif 70 <= s and s< 80:
            o = 'A'
        elif 55 <= s and s< 70:
            o = 'P'
        elif 40 <= s and s< 55:
            o = 'D'
        else:
            o = 'T'
        return o

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())