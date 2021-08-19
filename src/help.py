#!/usr/bin/python3

import os


class Help:

    def getHelp(self):
        print("""
(1) Entries
(2) See Score: (s)

(9) Go Back
        """)
        cont = True
        while cont:

            try:
                option = int(input("What would you like help with? ").strip())
                if option == 1:
                    self.entries()
                elif option == 2:
                    self.seeScore()
                elif option == 9:
                    os.system("clear")
                    cont = False
                else:
                    print("You must enter in a valid option")

            except Exception as e:
                print("You must enter in a valid option")

    def entries(self):
        print("""
Successful Entry: 77 
Unsuccesful Entry: <Enter in Nothing>
              """)

    def seeScore(self):
        print("Press \"s\" to see your score")


if __name__ == '__main__':
    pass
