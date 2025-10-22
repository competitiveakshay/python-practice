import random

subjects = [
    "Donald Trump",
    "Elon Musk",
    "Georgia Meloni",
    "Mark Zukerberg",
    "Sam Altman"
]

actions = [
    "is having fun with friends",
    "asking people to buy crackers",
    "got caught smuggling candies",
    "has a home",
    "was seeing selling iphones"
]

locations = [
    "at the white house",
    "under the sea",
    "in the airplane",
    "in america",
    "in the neighbouhood"
]

while True:
    sub = random.choice(subjects)
    act = random.choice(actions)
    loc = random.choice(locations)

    ans = input("Do you want more headlines?(Yes/No): ").strip().lower()

    print()
    if ans == "yes":
        print(f"{sub} {act} {loc}")
    elif ans == "no":
        print("I hope you had fun!","Bye")
        break
    elif ans != "yes" and ans != "no":
        print("Please enter the correct input!!!")

