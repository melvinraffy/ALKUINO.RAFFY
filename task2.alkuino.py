class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, I'm {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"And currently studying {self.course}.")


student1 = Student("Vina", 18, "Education")
student2 = Student("Mikhaela", 18, "Tourism")
student3 = Student("Jose", 22, "Information Technology")


student1.introduce()
print()  
student2.introduce()
print()  
student3.introduce()