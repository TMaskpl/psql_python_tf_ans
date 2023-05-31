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

    list = []
    
    for row in data:
        id = str(row[0]).replace('(','').replace(')','').replace("'","").replace(',','')
        nazwa = str(row[1]).replace('(','').replace(')','').replace("'","").replace(',','')
        
        list.append({"id": id})
        list.append({"nazwa": nazwa})

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

    conn.close()
    
def get_json_data(file):
    with open(file) as json_data:
        data = json.load(json_data)
    print(data[0])

if __name__=='__main__':
    conn = get_connection()
    get_select(conn)
    # get_json_data("output.json")