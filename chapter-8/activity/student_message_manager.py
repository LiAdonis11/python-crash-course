student_messages = ['bsit', 'bsi', 'bs', 't']
archived_messages = []

def display_messages(student_messages):
    for student_message in student_messages:
        print(student_message)
def archive_messages(archived_messages, student_messages):
    while student_messages:
        current_message = student_messages.pop()
        print(f"Sending the message: {current_message}")
        archived_messages.append(current_message)



display_messages(student_messages)
archive_messages(archived_messages, student_messages[:])

print(student_messages)
print(archived_messages)
