def make_sandwich(*items):
    print('\nMaking a sandwich with: ')
    for item in items:
        print(f"- {item}")

make_sandwich('cheese')
make_sandwich('ham', 'lettuce')
make_sandwich('meatballs', 'Mozzarella', 'chicken')    
    