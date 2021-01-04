# Home-Workout-Generator
The Home Workout Generator is a tool that generates exercises in a list that can be done at home without any equipment. Users are able to select the difficulty of the exercises that they want to do. 

## Installation of the service
In terminal, copy and paste the following commands: 
```git clone https://github.com/your-username/Home-Workout-Generator```

## Running the Product Step by Step
1. After cloning the product, it should be in your desktop. 
2. Enter the folder. 
  On mac: ```cd Home-Workout-Generator```
  On Windows: ```cd c:\Home-Workout-Generator```
3. Run the code. 
  Simply type in ```Python workoutgenerator.py```
4. Select a difficulty
  1 = Easiest Excercise
  2 = Medium Exercises
  3 = Hardest Exercises
5. Each will return a complete workout. 
This Includes: Warmup, The Main Exercises and Cooldown. 

__Each exercise should last about 1 minute and should be repeated 3~5 times.__

## How To Do Each Exercise Correctly (Step by Step Procedures, Includes Gifs): 
Here is a link to the google slides: https://docs.google.com/presentation/d/12tO3w2Anmual1wTOHjvfOnerPUWhwn7iHRN-SDyVAdU/edit?usp=sharing

## Not Enough? Add Your Own Exercises to the Code. 
1. Enter the folder. 
  On mac: ```cd Home-Workout-Generator```
  On Windows: ```cd c:\Home-Workout-Generator```
2. Open the Code in Terminal
  ```atom workoutgenerator.py```
3. Add your exercise to the list included. 
Eg: 
**Original Code**
```cooldown = [
    "Squats",
    "Side Lunges",
    "Lunge",
    "Calf Raise",
    "Walking Lunges",
]
```

Adding an Exercise Such as Pull Ups. 
Add "Pull up", into the code

**After Adding it In:**
```cooldown = [
    "Squats",
    "Side Lunges",
    "Lunge",
    "Calf Raise",
    "Walking Lunges",
   ```diff
 - "Pull Up",
 ```
]
```
