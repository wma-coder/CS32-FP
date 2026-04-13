# project.py

import json
import os
import math

ball_mass_g = 45.93 # grams
drag_coeff = 0.25
air_density = 1.225 # kg/m^3
ball_radius = 0.02135 # m

# build a bag
# store the bag, and have an option for the user to create a new one
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
        self.distance = 0
        self.wind_speed = 0
        self.wind_angle = 0

    def get_distance(self):
        while True:
            try:
                self.distance = float(input("\nEnter shot distance (yards): "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_conditions(self):

        while True:
            try:
                self.distance = float(input("\nEnter wind speed (mph): "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("\nWind direction options:")
        print("0   = tailwind")
        print("90  = left-to-right")
        print("180 = headwind")
        print("270 = right-to-left")

        while True:
            try:
                self.wind_angle = float(input("Enter wind direction (degrees): "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_wind_components(self):
        theta_rad = math.radians(self.wind_angle)

        wind_x = self.wind_speed * math.cos(theta_rad)  # forward/back
        wind_y = self.wind_speed * math.sin(theta_rad)  # sideways

        return wind_x, wind_y

    # add some more conditions rather than just wind


class ClubRecommendationEngine:
    def __init__(self):
        # Just initialize empty/default values
        self.results = None

    def calculate_adjustments(self, shot_conditions):
        # Skeleton only for now
        self.results = {
            "playing_distance": 151,
            "aim_direction": "right",
            "aim_offset": 5
        }
        return self.results

    def recommend_club(self, bag):
        playing_distance = self.results["playing_distance"]

        best_club = None
        smallest_diff = float("inf")

        for club, distance in bag.clubs.items():
            diff = abs(distance - playing_distance)
            if diff < smallest_diff:
                smallest_diff = diff
                best_club = club

        return best_club

    def show_recommendation(self, bag):
        club = self.recommend_club(bag)

        print("\nRecommendation:")
        print(f"  Play for: {self.results['playing_distance']} yards")
        print(f"  Aim: {self.results['aim_offset']} yards {self.results['aim_direction']}")
        print(f"  Recommended club: {club}")


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

    shot_conditions = ShotConditions()
    engine = ClubRecommendationEngine()

    while True:

        shot_conditions.get_distance()
        shot_conditions.get_conditions()

        engine.calculate_adjustments(shot_conditions)
        engine.show_recommendation(bag)

        choice = input("\nDo you want to take another shot? (y/n): ").lower()
        if choice != 'y':
            print("Hit 'em straight!")
            break

if __name__ == "__main__":
    main()
