import pdb
import json
import sys
import csv
import pymysql.cursors

# -----------------------------------------------------
# CLASS
#     - object that represents a single mushroom 
# -----------------------------------------------------
class PyMushroom:
    def __init__(self):
        self.attributes = {}

    def grow(self, columns, row):
        for column, element in zip(columns, row):
            self.attributes[column] = element 
        # self.print_mushroom() # NOTE: comment out

    def print_mushroom(self):
        print(json.dumps(self.attributes, indent=4))

    def harvest(self, columns):
        # return [self.attributes[key] for key in self.attributes]
        values = []
        for column in columns:
            values.append(self.attributes[column])
        return values

# -----------------------------------------------------
# CLASS
#     - object that represents a collection of mushrooms
# -----------------------------------------------------
class PyTroop:
    def __init__(self, db=None, table=None):
        self.db = db 
        self.table = table
        self.columns = []
        self.mushrooms = []
        self.mysql = None
        
    def grow(self, csv_path):
        with open(csv_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            self.columns = rows[0]
            for i in range(1, len(rows)):
                row = rows[i]
                mushroom = PyMushroom()
                mushroom.grow(self.columns, row)
                self.mushrooms.append(mushroom)

    def harvest(self):
        self.mysql = self.__connect()
        try:
            with self.mysql.cursor() as cursor:
                self.__create_db(cursor)
                self.__use_db(cursor)
                self.__create_table(cursor)
                self.__insert_mushrooms(cursor)
        finally:
            self.mysql.close()

    def analyze(self, constant_column=None, constant_value=None, variable_column=None):
        self.mysql = self.__connect()
        analyzation = {}
        try:
            with self.mysql.cursor() as cursor:
                self.__use_db(cursor)
                sql = "SELECT DISTINCT {} from {}".format(variable_column, self.table)
                cursor.execute(sql)
                values = [row[0] for row in cursor]
                for value in values:
                    distinct_value = value[0]
                    sql = "SELECT COUNT(*) FROM {} WHERE {}='{}' AND {}='{}'".format(self.table, 
                                                                                    constant_column, 
                                                                                    constant_value, 
                                                                                    variable_column, 
                                                                                    distinct_value
                                                                                )
                    cursor.execute(sql)
                    count = [row[0] for row in cursor][0]
                    analyzation[distinct_value] = count
        finally:
            self.mysql.close()
        print(json.dumps(analyzation, indent=4))

    # HIDDEN METHODS -----------------

    def __connect(self):
        return pymysql.connect(
                                        host="localhost",
                                        user="root"
                                    )

    def __create_db(self, cursor):
        sql = "CREATE DATABASE {}".format(self.db)
        cursor.execute(sql)
        self.mysql.commit()

    def __use_db(self, cursor):
        sql = "USE {}".format(self.db)
        cursor.execute(sql)
        self.mysql.commit()

    def __create_table(self, cursor):
        sql = "CREATE TABLE `{}` (".format(self.table)
        for i in range(len(self.columns)-1):
            column = self.columns[i]
            sql += "`{}` char(32), ".format(column)
        sql += "`{}` char(32))".format(self.columns[-1])
        cursor.execute(sql)
        self.mysql.commit()

    def __insert_mushrooms(self, cursor):
        for mushroom in self.mushrooms:
            values = mushroom.harvest(self.columns)
            sql = "INSERT INTO {} (`{}`) VALUES ('{}')".format(
                                                            self.table,
                                                            "`, `".join(self.columns),
                                                            "', '".join(values))
            cursor.execute(sql)
        self.mysql.commit()

# -----------------------------------------------------
# MAIN 
# -----------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print("usage: python main.py {path to csv file}")
        sys.exit()

    csv_path = sys.argv[1]
    mushroom_troop = PyTroop(db="kagglethings", table="mushrooms")
    mushroom_troop.grow(csv_path)
    mushroom_troop.harvest()
    mushroom_troop.analyze(constant_column="habitat", constant_value="d", variable_column="odor")

if __name__ == "__main__":
    main()
