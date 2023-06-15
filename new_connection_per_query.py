import psycopg2
import time

#import datetime
#from dateutil.relativedelta import relativedelta

def get_connection():
    connection = psycopg2.connect(user="yugabyte",
                                  password="***",
                                  host="10.200.0.43",
                                  port="5433",
                                  database="yugabyte")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_test_data(id):
    # get test data
    try:
        # Get joining date
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select value from test where k = %s"""
        cursor.execute(select_query, (id,))
        value = cursor.fetchone()
        print("k:", id, " value:", value)
        close_connection(connection)

    except (Exception, psycopg2.Error) as error:
        print("Error while getting test data", error)

print("Get test data  \n")

for i in range(1,100):
   get_test_data(i)
