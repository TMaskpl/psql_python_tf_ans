#! /usr/bin/evn python3

from env import *
import psycopg2
import json, jsonpath_ng

 
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

    list = []

    for row in data:
        id = str(row[0]).replace('(','').replace(')','').replace("'","").replace(',','')
        nazwa = str(row[1]).replace('(','').replace(')','').replace("'","").replace(',','')

        list.append(f'id: {id}')
        list.append(f'nazwa: {nazwa}')

    j = json.dumps({'results': list})
    print(j)

    conn.close()
    
def get_var_from_json():
    with open("output.json") as json_file:
        json_data = json.load(json_file)

    y = json.dumps(json_data)
    print(type(y))
    
if __name__=='__main__':
    # conn = get_connection()
    # get_select(conn)
    get_var_from_json()