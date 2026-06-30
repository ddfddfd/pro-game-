class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")


student1 = Student("Alex", 19)
student2 = Student("Bella", 21)
student3 = Student("Chris", 18)

# Calling the method for each student
student1.introduce()
student2.introduce()
student3.introduce()
