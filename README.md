# CS32-FP
CS 32 Final Project: Rules-based Golf Shot Optimizer

This is a golf shot optimizer that helps a user select the appropriate club for a given shot. The program will take as input the user’s average yardages for each club, the distance to the target, and environmental factors such as headwind or tailwind, temperature, and elevation. Using simplified kinematics in a 2D plane that considers wind as vector components which exert a constant force on the ball through it's time of flight, the program will adjust the effective playing distance based on these conditions and recommend the best club to use. The program will also use rules-based formulas to calculate the effect of temperature and eleveation on the golf ball. The goal is to implement a clear algorithm that processes inputs and produces a practical recommendation for club selection and aim direction.

Generative AI was utilized to help build the code to implement the kinematics for this program. The code in the functions compute_displacement and calculate_adjustments were written

To run the code, simply run the program in the IDE by navigating to the CS32-FP folder and typing in the command python3 project.py in the terminal. From there, follow the instructions on screen and type in input when requested.
