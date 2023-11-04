from Classes import *
import random
from main import *

# Creating a Citizen instance with a Job and an array of Traits, forgot gender, I added it
joe = Citizen("Joe", "Doe", 30, Job.Builder, [Traits.Appearence_Traits.Pretty, Traits.Inteligence_Traits.Smart], 75, 50,Genders.Male)
# Accessing Citizen attributes
print(joe.first_name)
print(joe.job)
print(joe.traits)

#name test
for i in range(10):
    chosen_gender = Genders.Male
    if random.randint(0,1) == 0:
        chosen_gender = Genders.Female
        print("Female")
    else:
        chosen_gender = Genders.Male 
        print("Male")
    first_name,last_name = generate_name(chosen_gender)
    print(f"{first_name} {last_name}")

#job test
print("job test")
for i in range(10):
    # Generate a job and print it using enum_to_string to make it
    print(enum_to_string(generate_job(), Job))

#traits test
print("trait test")
for i in range(10):
    traits = generate_traits(1)
    enum_class = traits[0].__class__
    print(enum_to_string(traits[0],enum_class))
# Test of generating person
print("person test")
for i in range(3):
    citizen = generate_person()
    traits_str = ", ".join(enum_to_string(trait, trait.__class__) for trait in citizen.traits)
    print(f"Name: {citizen.first_name} {citizen.last_name}\nAge: {citizen.age}\nJob: {enum_to_string(citizen.job, Job)}\nTraits: {traits_str}\nHunger: {citizen.hunger}\nHappiness: {citizen.happiness}\nGender: {enum_to_string(citizen.gender, Genders)}")

