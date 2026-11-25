marks=int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    
age = int(input("Enter your age: "))
print(check_age(age))


class Student:
    # Class attribute (shared by all students)
    school = "Al Amaal School"

    # Constructor
    def __init__(self, name, age, grade):
        # Instance attributes
        self.name = name
        self.age = age
        self.grade = grade

    # Method
    def introduce(self):
        return f"My name is {self.name} and I am in grade {self.grade}."

    # Special method
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Creating objects
student1 = Student("Zainab", 17, "12")
student2 = Student("Ahmed", 18, "12")


# Using methods
print(student1.introduce())
print(student2.introduce())

print()


# Using __str__ special method
print(student1)
print(student2)

print()


# Accessing class attribute
print("School:", Student.school)

print()


# ------------------------------
# Dynamic Attributes
# ------------------------------

# getattr() - Get attribute dynamically

attribute_name = "name"

print("Using getattr:")
print(getattr(student1, attribute_name))


print()


# setattr() - Create a new attribute dynamically

setattr(student1, "city", "Sharjah")

print("After using setattr:")
print(student1.city)


print()


# hasattr() - Check if attribute exists

print("Checking attributes:")

print(hasattr(student1, "age"))      # True
print(hasattr(student1, "phone"))    # False


print()


# delattr() - Delete an attribute

print("Deleting city attribute:")

delattr(student1, "city")

print(hasattr(student1, "city"))     # False


print()


# dir() - Show all attributes

print("All student attributes:")

for item in dir(student1):
    if not item.startswith("__"):
        print(item)