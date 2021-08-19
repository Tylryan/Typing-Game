#!/usr/bin/env python3
import statistics
import math
from help import Help
from os import system
import sys

import pandas as pd
from datetime import date
from Game import Game
from CSV import CSV

    

#TODO 1. Let me see the last 5 day's scores
#TODO 2. Remove last entry with something like "rm -l"
#TODO 3. Show me rolling averages of all scores
class Analysis():
    """
    A class that takes in a csv file and performs analysis on it.
    """

class Graphs():
    """
    A class that gives a visual representation to an analysis
    """

if __name__ == '__main__':
    game = Game()
    game.clearScreen()
    csv_class = CSV()

    # Check if there have been any previous games. returns 0 (success) or 2 (failed)
    previous_games = csv_class.readPreviousGameData()
    cont = True
    max_streak = input("What was your max streak?: ")
    game.setMaxStreak(max_streak)

    n_rounds = input("How many rounds were in your game?: Default = 5: ")
    game.setRounds(n_rounds)
    print("""
(h) Help
(s) Show Score
(c) Clear The Terminal
(rm) Remove an Entry

    """)
    while cont:
        ui = game.userInput()
        if "e" == ui:
            break
        elif "n" == ui:
            cont = False
        elif "s" == ui:
            # If no existing csv, create one and save results
            if previous_games == 2:

                print("Game Results")
                print(game.getResults())
                csv_class.setCurrentGameData(game.getResults())
                csv_class.save_to_csv()
                print("No previous games")
                cont = False

            else:
                # save current data
                csv_class.setCurrentGameData(game.getResults())
                csv_class.readPreviousGameData()
                # combine with old data
                csv_class.setCombineGameData()
                # save combined data to file
                csv_class.save_to_csv(existing=True)
                cont = False

            # Else, append results to existing one
        elif ui is None:
            pass
        else:
            pass
