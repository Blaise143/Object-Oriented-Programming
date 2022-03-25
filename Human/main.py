from student import*

def get_info(student : Student):
    print("Hello! My name is ", student.get_name())

blaise = Student("Blaise Appolinary", 23, 7, 100)

get_info(blaise)

