import psycopg2
from os import getenv
import pandas as pd
from kickstarter.queries import create_prediction_table

# Grabbing environment variables for establishing
# PostgreSQL database connection.
DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')


# Creating a cursor and connection object.
def connect_cursor(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    pg_cursor = pg_conn.cursor()
    return pg_conn, pg_cursor

CONN, CURSOR = connect_cursor()


# Function that inputs the form data and a prediction
# and commits the data to the PostgreSQL database.
def insert_table(data_dict, prediction):
    # Creating a tuple of the information to be inserted.
    temp_tuple = (data_dict['project_name'], 
                  data_dict['category'],
                  data_dict['description'], 
                  data_dict['city_name'], 
                  data_dict['country'],
                  data_dict['goal'], 
                  data_dict['currency'], 
                  int(data_dict['days_of_campaign']),
                  int(data_dict['launch_month']),
                  prediction)
    # Inserting the tuple.
    CURSOR.execute(f'''
        INSERT INTO model_prediction ("projectname", "category", "description", "city", "country", "goal", "currency", "duration", "month", "prediction")       
        VALUES {temp_tuple};''')
    # Committing the changes to the database.
    CONN.commit()
    return


# Use this to create the database if it does not already exist
if __name__ == '__main__':
    CURSOR.execute(create_prediction_table)
    CONN.commit()