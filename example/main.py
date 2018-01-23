import pdb
import json
import sys
import csv
import MySQLdb

class PyMushroom:
    def __init__():
        pass 

class PyTroop:
    def __init__(self):
        self.mushrooms = []

        mysql = MySQLdb.connect(
                            host="localhost",
                            user="root"                            )
        self.cursor = mysql.cursor()
    
    def grow(self, csv_path):
        with open(csv_path, "r") as csv_file:
            rows = csv.reader(csvfile, delimiter=",")
            pdb.set_trace()

    def harvest(self, db, table):
        pass

    def analyze(self):
        pass

    # HIDDEN METHODS -----------------

    def __create_db(self):
        pass 

    def __create_table(self):
        pass

    def __sql_insert(self):
        pass
    
    def __sql_select(self):
        pass

# FUNCTIONS --------------------------------

def main():
    if len(sys.argv) != 2:
        print("usage: python main.py {path to csv file}")
        sys.exit()

    csv_path = sys.argv[1]
    mushroom_troop = PyTroop()
    mushroom_troop.grow(csv_path)
    mushroom_troop.harvest()
    mushroom_troop.analyze(constant="habitat", variable="odor")

if __name__ == "__main__":
    main()
