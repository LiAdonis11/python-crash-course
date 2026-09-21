current_users = ['admin', 'hr','osas', 'clinic', 'registrar', 'cd office', 'graduate school', 'library', 'CAS']

new_current_users = [current_user.lower() for current_user in current_users]

new_users = ['cd office', 'graduate school', 'cas', 'lhs', 'cte', 'cbme']


for new_user in new_users:
    if new_user in new_current_users:
        print(f"{new_user} is not available, please enter a new username")
    else:
        print(f"The user name {new_user} is available")
print("You have created your account!")

