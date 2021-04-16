import sqlite3
from sqlite3 import Error
import pandas as pd

#function to create connection to database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        curs = conn.cursor()
        curs.execute(create_table_sql)
        curs.execute("SELECT * FROM table1")
    except Error as e:
        print(e)

def main():
    database = r"JapanTownDoorSchedule.sqlite"

    sql_create_Doorschedule_table = """ CREATE TABLE IF NOT EXISTS table1 (
                                        id integer PRIMARY KEY, 
                                        doorNumber text, 
                                        width text, 
                                        height text, 
                                        dtype text, 
                                        material text, 
                                        fireRating text, 
                                        hardwareSet text
                                        ); """
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_Doorschedule_table)
        df = pd.read_excel("JapanTownDoorSchedule.xlsx", usecols = [1,2,3,4,5,13,14], skiprows=6)
        df.rename(columns = {"id":"id", 
                            "doorNumber": "doorNumber", 
                            "width":"width", 
                            "height":"height", 
                            "dtype":"dtype", 
                            "material":"material", 
                            "fireRating": "fireRating", 
                            "hardwareSet":"hardwareSet"})
        print(df)
        df.to_sql(name = "table1", con = conn, if_exists= 'append')
        # # create hardware table table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()



