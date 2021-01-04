import random
import sys

warmups = [
    "Jumping Jacks",
    "Arm Circles",
    "Walking Knee Hugs",
    "Wrist Circles",
    "Neck Rolls",
]

easy_exercises = [
    "Extended Leg Pulse",
    "Sit-Ups",
    "Lateral Leg Raise",
    "Plank Taps",
    "Step Up",
    "Tuck Jump",
    "Wall Sits",
    "But Kicks",
    "High Knees",
    "Sprinting on the spot",
]

medium_exercises = [
    "Mountain climber",
    "High Knees",
    "Plank up",
    "Shoulder Bridge",
    "Superman",
    "Plank Knee to Elbow",
    "Prisoner Walkup",
    "Push ups",
    "Squat Thrusts",
]

difficult_exercises = [
    "Burpees",
    "Plank jacks",
    "Bicycle Crunch",
    "Side Planks",
    "Russian Twist",
    "Burpees with Push-Ups",
    "Reverse Crunch",
    "Crunch",
    "Glute Bridge",
]

cooldown = [
    "Squats",
    "Side Lunges",
    "Lunge",
    "Calf Raise",
    "Walking Lunges",
]

try:
    diff = int(input("Input a difficulty: [1/2/3] "))
except:
    sys.exit("Invalid difficulty.")

generated = []

number_of_warmups = 1
number_of_exercises = 2
number_of_cooldowns = 1

exercises = easy_exercises

if diff < 1 or diff > 3:
    sys.exit("Invalid difficulty.")

if diff >= 2:
    number_of_warmups += 1
    number_of_cooldowns += 1
    number_of_exercises += 2
    exercises += medium_exercises

if diff == 3:
    number_of_exercises += 2
    exercises += difficult_exercises

generated.append(random.sample(warmups, number_of_warmups))
generated.append(random.sample(exercises, number_of_exercises))
generated.append(random.sample(cooldown, number_of_cooldowns))


print("Workout:")
print("Warmup:")
for i in generated[0]:
    print(i)
print("Exercises:")
for i in generated[1]:
    print(i)
print("Cooldown:")
for i in generated[2]:
    print(i)
