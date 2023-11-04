#import enum for Job and traits,removed auto so picking random is easier 
from enum import Enum

class Job(Enum):
    Unemployed = 0
    Builder = 1
    Hunter = 2
    Medic = 3
    Cheff = 4

class Traits(Enum):
    Ugly = 1
    Dumb = 2
    Smart = 3
    Pretty = 4

class Genders(Enum):
    Male = 0
    Female = 1

#Declaring the citizen structure
class Citizen:
    def __init__(self, first_name: str, last_name: str, age: int, job: Job, traits: list, happiness: int, hunger: int,gender: Genders):
        if not isinstance(job, Job):
            raise ValueError("Job must be an instance of the Job enumeration.")
        if not all(isinstance(trait, Traits) for trait in traits):
            raise ValueError("Traits must be valid Traits enums!")
        if not isinstance(gender, Genders):
            raise ValueError("Gender must be an instance of the Gender enumeration.")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.traits = traits
        self.happiness = happiness
        self.hunger = hunger
        self.gender = gender


female_first_names = [
        "Sophia", "Olivia", "Riley", "Emma", "Ava", "Isabella", "Aria", "Aaliyah", "Amelia", "Mia",
        "Layla", "Zoe", "Camila", "Charlotte", "Eliana", "Mila", "Everly", "Luna", "Avery", "Evelyn",
        "Harper", "Lily", "Ella", "Gianna", "Chloe", "Adalyn", "Grace", "Hannah", "Lillian", "Natalie",
        "Sofia", "Aubrey", "Madison", "Scarlett", "Victoria", "Penelope", "Aurora", "Lucy", "Nova",
        "Brooklyn", "Paisley", "Savannah", "Emilia", "Stella", "Caroline", "Genesis", "Willow", "Hazel",
        "Leah", "Naomi", "Avery", "Ella"
]

male_first_names = [
        "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
        "Sebastian", "Matthew", "Daniel", "Carter", "Jayden", "John", "David", "Joseph", "Michael", "Logan",
        "Ethan", "Isaac", "Owen", "Jack", "Caleb", "Gabriel", "Luke", "Anthony", "Aiden", "Dylan",
        "Wyatt", "Jackson", "Eli", "Levi", "Mason", "Nathaniel", "Andrew", "Nicholas", "Connor", "Samuel",
        "Ezekiel", "Josiah", "Theodore", "William", "Harrison", "Austin", "Maverick", "Maxwell", "Ezra",
        "Asher", "Lincoln", "Hudson", "Jackson"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Perez", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "King", "Green",
    "Hill", "Turner", "Clark", "Edwards", "Collins", "Stewart", "Morris", "Nguyen", "Murphy", "Cook",
    "Rogers", "Bell", "Bailey", "Kelly", "Alexander", "Gomez", "Carter", "Reed", "Harrison", "Wright",
    "Sanchez", "Ward", "Cox", "Rivera", "Parker", "Wood", "Long", "Reyes", "Gray", "Foster", "Gutierrez",
    "Morgan", "Scott", "Powell", "Ross", "Russell", "Sullivan", "Henderson", "Coleman", "Jenkins", "Perry",
    "Powell", "Bryant", "Cruz", "Pierce", "Chavez", "Ramos", "Phillips", "Watson", "Sanders", "Price", "Bennett",
    "Woodward", "Barnes", "Fisher", "Ross", "Mason", "Griffin", "Diaz", "Hayes", "Reed", "West", "Lynch", "Sullivan"
]
