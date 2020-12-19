from random import sample
from exercises import *

class Generator(object):
    def get_difficulty(self):
        difficulty = input("Which exercise difficulty would you like to do? (easy, medium, hard)\n>>> ")
        while True:
            if "easy" in difficulty:
                self.sets = "1-3"
                self.target_reps = "1-6"
                break
            elif "medium" in difficulty:
                self.sets = "4-6"
                self.target_reps = "7-13"
                break
            elif "difficult" in difficulty:
                self.sets = "7-10"
                self.target_reps = "13-19"
                break
            else:
                print ("Please enter easy, medium, hard.")
                difficulty = input("Which exercise difficulty would you like to do? (easy, medium, hard)\n>>> ")
                difficulty = difficulty.lower()
        return self.sets, self.target_reps

    def workout_title(self):
        if difficulty == "easy":
            print("Easy Workout")
        elif difficulty == "medium":
            print("Medium Workout")
        elif difficulty == hard:
            print("Hard Workout")

    def generate_easy(self):
        Generator.title("Easy Workout")
        Generator.section("Warmup")
        Generator.print_exercises(self, warmup_exercises)
        Generator.section("Workout")
        Generator.print_exercises(self, easy_exercises)
        Generator.print_exercises(self, easy_exercises)
        Generator.print_exercises(self, easy_exercises)
        Generator.section("Cooldown")
        Generator.print_exercises(self, cooldown_exercises)

    def generate_medium(self):
        Generator.title("Easy Workout")
        Generator.section("Warmup")
        Generator.print_exercises(self, warmup_exercises)
        Generator.print_exercises(self, warmup_exercises)
        Generator.section("Workout")
        Generator.print_exercises(self, easy_exercises)
        Generator.print_exercises(self, medium_exercises)
        Generator.print_exercises(self, medium_exercises)
        Generator.print_exercises(self, medium_exercises)
        Generator.section("Cooldown")
        Generator.print_exercises(self, cooldown_exercises)

    def generate_hard(self):
        Generator.title("Easy Workout")
        Generator.section("Warmup")
        Generator.print_exercises(self, warmup_exercises)
        Generator.section("Workout")
        Generator.print_exercises(self, easy_exercises)
        Generator.print_exercises(self, medium_exercises)
        Generator.print_exercises(self, difficult_exercises)
        Generator.print_exercises(self, difficult_exercises)
        Generator.print_exercises(self, difficult_exercises)
        Generator.section("Cooldown")
        Generator.print_exercises(self, cooldown_exercises)

class Engine(object):
    def start(self):
        self.get_difficulty()
        self.create_workout()
        log.close()

self1 = self(), Generator()
Engine.start(self1)
