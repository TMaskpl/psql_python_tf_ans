#! /usr/bin/evn python3

from env import *
import psycopg2
import json
import re

 
def get_connection():
    try:
        return psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
    except:
        return False
 

def get_select(conn):
    curr = conn.cursor()
    curr.execute("SELECT id, nazwa FROM public.customer;")
    data = curr.fetchall()

    dict = {}
    parameters = []
    
    for row in data:
        id = str(row[0]).replace('(','').replace(')','').replace("'","").replace(',','')
        nazwa = str(row[1]).replace('(','').replace(')','').replace("'","").replace(',','')
        
        dict.update({"id": id})
        dict.update({"nazwa": nazwa})
        parameters.append(dict)

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(parameters, f, ensure_ascii=False, indent=4)

    conn.close()
    

def get_jason_data():
    pass

if __name__=='__main__':
    # conn = get_connection()
    # get_select(conn)
    get_jason_data()