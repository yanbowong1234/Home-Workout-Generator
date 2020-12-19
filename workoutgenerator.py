from random import sample
from exercises import *

class Generator(object):
    def difficulty(self):
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
