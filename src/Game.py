#!/usr/bin/python

import pandas as pd
import os
from datetime import date
import statistics
import sys

#TODO Create a function that checks the current operating system and clears their screen
#TODO Make this program work on Windows
class Game:
    def __init__(self):
        self._successful = []
        self._unsuccessfull = []
        self._rounds = 5
        self._results = pd.DataFrame()
        self._maxStreak = 0

#####################   GAME FLOW #############################################
    def userInput(self):
        ui = input("WPM Successful: ").lower().strip()
        ui_list = list(ui.split(" "))

        quit = ["q", "quit", "exit"]
        next = ["n", "next"]
        clear = ["c","clear"]
        history = ["history","ls","print"]
        remove = ["rm","remove","delete","del"]
        list_inputs = ["ls", "list"]
        score = ["score", "s"]

        if len(ui_list) == 1:
            if ui in quit:
                print("Exiting")
                return "e"
            elif ui in score:
                # I'm thinking don't return anything, just let them check what their
                # Current game score is
                try:
                    self.printResults()
                    self.saveResults()
                    return "s"
                except Exception as e:
                    print(e)
                    print("\033[93mYou have not entered anything yet.\033[0m")
            elif ui == "h":
                Help().getHelp()
            elif "" == ui:
                self.add_to_unsuccessful_list(0)
                self.printInputs()
            elif ui in clear:
                self.clearScreen()
            elif ui in history:
                self.printInputs()
            elif ui in remove:
                print("\nSuccessful List: [1,2,3,4,5]")
                print("Unsuccessful List: [5,4,3,2,1]")
                print("\nRemove '3' from the SUCCESSFUL list: \nEntry -> s 3")
                print("Remove '2' from the UNSUCCESSFUL list: \nEntry -> u 4")
                chosen_list, index = list(input("Enter here: ").lower().split(" "))
                self.removeEntry(chosen_list,index)
            else:
                try:
                    wpm = int(ui_list[0])
                    self.add_to_success_list(wpm)
                    self.printInputs()
                except:
                    print("Something went wrong with that entry")
                    pass
        elif len(ui_list) == 2:
            one, two = ui_list[0], ui_list[1]
            if "n" == two:
                self.add_to_unsuccessful_list(int(one))
                self.printInputs()
            if ("rm" == one) and ("-sl" == two ) or ("-ls" == two):
                self.removeEntry("s", 0)

            elif ("rm" == one) and ("-ul" == two) or ("-lu" == two):
                self.removeEntry("u", 0)

        elif len(ui_list) == 3:
            one, two, three = ui_list[0], ui_list[1], ui_list[2]
            # This seems like it would be a faster way to remove something.
            # The other one stays, because it walks you through it.

            if "rm" == one:
                try:
                    chosen_list, index = two, int(three)
                    self.removeEntry(chosen_list, index)
                except Exception as e:
                    print("\nError Removing that entry. Try again.")
        else:
            print("You must've entered in something incorrect")

################## GETTERS AND SETTERS ######################################
    def getResults(self):
        return self._results
    def setResults(self, results):
        self._results = pd.DataFrame(results)

    def getRounds(self):
        return self._rounds

    def setRounds(self, rounds):
        try:
            rounds = int(rounds)
            self._rounds = rounds
        except Exception as e:
            pass
        finally:
            print(f"Rounds = {self._rounds}")

    def add_to_success_list(self, wpm):
        self._successful.append(wpm)

    def add_to_unsuccessful_list(self, wpm):
        self._unsuccessfull.append(wpm)

    def getSuccessful(self):
        successful_list = self._successful
        return successful_list

    def getUnsuccessful(self):
        unsuccessful_list = self._unsuccessfull
        return unsuccessful_list
    def setMaxStreak(self, streak):
        try:
            self._maxStreak = int(streak)
        except ValueError:
            print("You need to enter in a valid integer")
            sys.exit()


    def getMaxStreak(self):
        return self._maxStreak

###################### CONVENIENCE FUNCTIONS ###################################
    def printInputs(self):
        if (not bool(self._successful)) and (not bool(self._unsuccessfull)):
            print("You have not entered anything")
        if bool(self._successful):
            print(f"Successes: {self._successful}")
        if bool(self._unsuccessfull):
            print(f"Not Successful: {self._unsuccessfull}\n")

    def clearScreen(self):
        return os.system("cls" if os.name == "nt" else "clear")

    def removeEntry(self, which_list, index):
        try:
            # Check if they entered a number
            index = int(index)
            correct_list = ["s","u"]
            if which_list in correct_list: 
                if which_list == "s":
                    self._successful.pop(index-1)
                elif which_list == "u":
                    self._unsuccessfull.pop(index -1)
            else:
                print("Your first entry was neither \"s\" or \"u\"")
        except Exception as e:
            print("Either your first entry was not an \"s\" or \"u\""\
                    "or your second entry was not an integer")

##################### CALCULATE GAME STATS ###################################
    def getTotalWPM(self):
        """
        Returns total base score of the game.
        Adds up all the WPM entries
        """
        total = sum(self.getSuccessful())
        return total

    def getCountSuccessful(self):
        """
        Returns the number of the successful entries
        """
        count = len(self.getSuccessful())
        return count

    def getCountUnsuccessful(self):
        """
        Returns the number of unsucessfull entries
        """
        count = len(self.getUnsuccessful())
        return count

    def getAverageWPM(self):
        """
        Returns the average WPM of the game
        """
        average = round(self.getTotalWPM() / self.getCountSuccessful(),4)
        return average

    def getWPMStd(self):
        """
        Return the average Standard Deviation of the Game
        """

        std = round(statistics.stdev(self.getSuccessful()), 4)
        return std

    def getStdMultiplier(self):
        """
        Calculates and Returns the Standard Deviation Penalty
        """
        std = self.getWPMStd()
        multiplier = 1

        if std > 15:
            multiplier = 1.15
        elif std > 10:
            multiplier = 1.10
        elif std > 3:
            multiplier = 1.05
        else:
            multiplier = 1

        return multiplier

    def getAccuracy(self):
        """
        Returns the player's accuracy during the round
        """
        success = self.getCountSuccessful()
        unsuccess = self.getCountUnsuccessful()

        accuracy = round(int(success) / (int(success) + int(unsuccess)),4)
        return accuracy

    def getGameScore(self):
        """
        Returns the average score per round after pentalties.
        I.e. the game score
        """
        totalWPM = self.getTotalWPM() / self.getRounds()
        stdMultiplier = self.getStdMultiplier()
        accuracy = self.getAccuracy()

        game_score = round((totalWPM / stdMultiplier) * accuracy, 4)
        return game_score

    def saveResults(self):
        """
        Sets the data from the game just played to be an attribute of the class
        """
        current_date = date.today()

        results = pd.DataFrame({

                "Date": [current_date],
                "End_Score":[self.getGameScore()],
                "Score_Before_Discount":[self.pre_penalty_game_score],
                "Accuracy":[self.getAccuracy()],
                "WPM_STD": [self.getWPMStd()],
                "STD_Multiplier":[self.getStdMultiplier()],
                "Max_Streak":[self.getMaxStreak()],
                "Max_WPM": [max(self.getSuccessful())],
                "Min_WPM":[min(self.getSuccessful())],
                "Average_WPM":[self.getAverageWPM()]

                })
        self.setResults(results)
    def printResults(self):
        a = self.getGameScore()
        b = self.getCountSuccessful()
        c = self.getCountUnsuccessful()
        d = self.getAccuracy()
        e = self.getWPMStd()
        f = self.getAverageWPM()
        g = self.getStdMultiplier()
        h = max(self.getSuccessful())
        i = min(self.getSuccessful())
        self.pre_penalty_game_score = round(self.getTotalWPM() / self.getRounds(),4)

        current_date = date.today()
        print(f"\nDate: {current_date}")
        print(f"\nGame Score: {a}")
        print(f"Pre Penalty Score: {self.pre_penalty_game_score}")
        print(f"Accuracy: {d}")
        print(f"WPM STD: {e}")
        print(f"STD Mult: {g}")
        print(f"Max: {h}")
        print(f"Min: {i}")
        print(f"Average: {f}")


if __name__ == '__main__':
    pass
