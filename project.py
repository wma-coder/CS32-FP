# project.py

import json
import os

# build a bag
# have an option for the user to store the bag

class GolfBag:

    def __init__(self):
        self.clubs = {}

    def build_bag(self):
        num_clubs = int(input("How many clubs are in your bag? "))

        for i in range(num_clubs):
            club = input("Enter club name: ")
            distance = int(input(f"How far do you hit your {club}? "))
            self.clubs[club] = distance

    def show_bag(self):
        print("\nYour bag:")
        for club, dist in self.clubs.items():
            print(f"{club}: {dist} yards")

    def save_bag(self, filename="bag.json"):
        with open(filename, "w") as f:
            json.dump(self.clubs, f)
        print("\nBag saved!")


    def load_bag(self, filename="bag.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.clubs = json.load(f)
            print("Bag loaded!")
            return True
        return False


class ShotConditions:
    def __init__(self):
        self.wind = 0

    def get_conditions(self):
        self.wind = int(input("Enter wind speed (mph, positive = headwind, negative = tailwind): "))

    # add some more conditions rather than just wind


'''
class ClubRecommendation Engine:
    def __init__(self):
'''

def main():

    bag = GolfBag()

    # Try to load existing bag
    if bag.load_bag():
        bag.show_bag()
        choice = input("\nDo you want to rebuild your bag? (y/n): ").lower()
        if choice == 'y':
            bag.build_bag()
            bag.save_bag()
    else:
        # No saved bag → create one
        bag.build_bag()
        bag.save_bag()

    bag.show_bag()


if __name__ == "__main__":
    main()
