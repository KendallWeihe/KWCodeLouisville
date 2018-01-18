

# TODO:
#     - read CSV file
#     - establish mySQL connection
#     - create db
#     - create table
#     - insert into db table

import pdb
import sys
import csv
import MySQLdb

def read_data(file_name):
    column_names = []
    data = []
    with open(file_name, "r") as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        first_row = True
        for row in rows:
            if first_row:
                columns = row
                first_row = False
            else:
                data.append(row)

    return columns, data

def create_db(cursor):
    sql_cmd = "CREATE DATABASE KaggleThings"
    cursor.execute(sql_cmd)

def create_table(cursor, columns):
    pdb.set_trace()
    sql_cmd = "CREATE TABLE `Mushrooms` ("
    for i in range(len(columns)-1):
        column = columns[i]
        sql_cmd += "`{}` char, ".format(column)
    sql_cmd += "`{}` char)".format(columns[-1])
    pdb.set_trace()
    print
    # cursor.execute("USE KaggleThings")
    cursor.execute(sql_cmd)

def insert(cursor, row):
    sql_cmd = "INSERT INTO Mushrooms VALUES ("
    for element in row:
        sql_cmd += "{}, ".format(element)
    sql_cmd.strip(",")
    sql_cmd += ")"
    cursor.execute(sql_cmd)

def main():
    # TODO: hard code this
    data_file = sys.argv[1]
    columns, data = read_data(data_file)

    mysql = MySQLdb.connect(
                            host="localhost",
                            user="root"                            )
    cursor = mysql.cursor()
    create_db(cursor)
    cursor.execute("USE KaggleThings")
    create_table(cursor, columns)

    for row in data:
        insert(cursor, row)


main()





# ...
