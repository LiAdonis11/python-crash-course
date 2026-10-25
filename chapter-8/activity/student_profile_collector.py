def make_student(name, course):
    student = {
        'name' : name,
        'course' : course
    }
    
    return student

while True:
    print("Type (quit) to end the program.")
    name = input("Enter your name: ")
    if name == 'quit':
        break
    course = input("Enter your course: ")
    if course == 'quit':
        break
    
    student_profile = f"\nHello {name.title()} from {course.upper()}.\n"
    print(student_profile)
    
    student_profile = make_student(name, course)
    print(student_profile)
    
    
    
    
    