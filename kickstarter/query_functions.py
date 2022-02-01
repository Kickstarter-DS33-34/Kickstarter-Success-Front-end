import psycopg2
from os import getenv
import pandas as pd
from kickstarter.queries import create_prediction_table

DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

def connect_cursor(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    pg_cursor = pg_conn.cursor()
    return pg_conn, pg_cursor

CONN, CURSOR = connect_cursor()

def insert_table(data_df, prediction):
    data_df['prediction'] = prediction
    for row in data_df.itertuples():
        temp_tuple = (row.projectname, 
                      row.category,
                      row.description, 
                      row.city, 
                      row.country,
                      float(row.goal), 
                      row.currency, 
                      int(row.duration),
                      row.month,
                      bool(row.prediction))
        CURSOR.execute(f'''
            INSERT INTO model_prediction ("projectname", "category", "description", "city", "country", "goal", "currency", "duration", "month", "prediction")       
            VALUES {temp_tuple};''')
        CONN.commit()
    return

if __name__ == '__main__':
    CURSOR.execute(create_prediction_table)
    CONN.commit()