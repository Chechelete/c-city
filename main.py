import random
from Classes import *

#Temporary array to hold citizens, may change to SQL database
people = []

# Creating a Citizen instance with a Job and an array of Traits, forgot gender, I added it
joe = Citizen("Joe", "Doe", 30, Job.Builder, [Traits.Pretty, Traits.Smart], 75, 50,Genders.Male)
# Accessing Citizen attributes
print(joe.first_name)
print(joe.job)
print(joe.traits)

def generate_name(gender):
    first_name = ""
    last_name = ""
    if gender == Genders.Male:
        first_name = random.choice(male_first_names)
    else:
        first_name = random.choice(female_first_names)
    last_name = random.choice(last_names)
    return first_name,last_name

def generate_job():
    return random.choice(list(Job))

def generate_traits():
    contradictory_pairs = {('Ugly', 'Pretty'), ('Smart', 'Dumb')}
    traits = set()
    while len(traits) < 3:
        new_trait = generate_traits()
        if all((new_trait, prev_trait) not in contradictory_pairs and (prev_trait, new_trait) not in contradictory_pairs for prev_trait in traits):
            traits.add(new_trait)
    return list(traits)

def enum_to_string(enum_value, enum_class):
    if isinstance(enum_value, enum_class):
        return enum_value.name
    else:
        raise ValueError(f"{enum_value} is not a member of {enum_class.__name__}")

def generate_person():
    gender = random.choice(list(Genders))
    first_name, last_name = generate_name(gender)
    age = random.randint(16, 50)
    job = generate_job()

    all_traits = list(Traits)
    contradictory_pairs = {('Ugly', 'Pretty'), ('Smart', 'Dumb')}

    for pair in contradictory_pairs:
        if all(trait in all_traits for trait in pair):
            trait_to_remove = random.choice(pair)
            all_traits.remove(trait_to_remove)

    traits = random.sample(all_traits, 3)

    happiness = random.randint(20, 80)
    hunger = random.randint(20, 80)
    new_citizen = Citizen(first_name, last_name, age, job, traits, happiness, hunger, gender)
    people.append(new_citizen)

    return new_citizen

