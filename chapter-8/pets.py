def describe_pet(pet_name='har',animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('dog', 'willie')
describe_pet('whitey')