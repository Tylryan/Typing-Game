#/usr/bin/python
import statistics
import math
from help import Help
from os import system
import pandas as pd
from datetime import date

class CSV():
    """
    A class to do with saving, reading, parsing CSV documents.
    """
    def __init__(self):
        self.new_game_data = pd.DataFrame()
        self.previous_game_data = pd.DataFrame()

    def readPreviousGameData(self):
        """
        Brings previous games data in scope for this class via a csv file
        """
        try:
            previous_games = pd.read_csv("out.csv")
            self.previous_game_data = previous_games
            return 0
        except Exception:
            print("No game file saved to pick from")
            return 2
    def setPreviousGameData(self, new_data):
        self.previous_game_data = new_data
        
    def getPreviousGameData(self):
        return self.previous_game_data


    def setCurrentGameData(self, data):
        self.new_game_data = data
    def getCurrentGameData(self):
        return self.new_game_data
    def setCombineGameData(self):
        self.setPreviousGameData(self.getPreviousGameData().append(self.getCurrentGameData()))
        #self.previous_game_data.append(self.new_game_data)
    def save_to_csv(self, existing = False):
        if existing == False:
            self.new_game_data.to_csv("out.csv",index=False)
        else:
            self.getPreviousGameData().to_csv("out.csv", index = False)

if __name__ == '__main__':
    pass
