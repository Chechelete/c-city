import random
from Classes import *

#Temporary array to hold citizens, may change to SQL database
people = []


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

def generate_traits(amount):
    traits = []
    possible_classes = [Traits.Appearence_Traits,Traits.Inteligence_Traits]
    for _ in range(amount):
        class_to_check = random.choice(possible_classes)
        possible_classes.remove(class_to_check)
        trait = random.choice(list(class_to_check))
        traits.append(trait)
    return traits

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
    traits = []
    num_of_traits = random.randint(1,2)
    traits = generate_traits(num_of_traits)

    happiness = random.randint(20, 80)
    hunger = random.randint(20, 80)
    new_citizen = Citizen(first_name, last_name, age, job, traits, happiness, hunger, gender)
    people.append(new_citizen)

    return new_citizen

