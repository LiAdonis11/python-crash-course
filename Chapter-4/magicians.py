magicians = ['alice', 'david', 'carolina', 'harley', 'joker']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick.')
    print(f'I cant wait to see your next week trick, {magician.title()}.\n')
    print('Thank you, everyone. That was a great magic show!')


print("The first three items in the list:")
print(magicians[0:3])

print("Three items from the middle of the list are:")
print(magicians[1:4])

print("The last three items in the list are:")
print(magicians[-3:])