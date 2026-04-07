# project.py

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

class ShotCalculator:
    def __init__(self):
        self.wind = 0

    def get_conditions(self):
        self.wind = int(input("Enter wind speed (mph, positive = headwind, negative = tailwind): "))

    def adjust_distance(self, distance):
        # simple rule: every 1 mph wind = 1 yard adjustment
        adjusted = distance + self.wind
        return adjusted


def main():
    bag = GolfBag()
    bag.build_bag()
    bag.show_bag()


if __name__ == "__main__":
    main()
